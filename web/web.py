import re
import os
from bs4 import BeautifulSoup
from sanic import Sanic, response
from sanic_jinja2 import SanicJinja2

app = Sanic()
jinja = SanicJinja2(app)
jinja = SanicJinja2(app, pkg_name='web')

app.static("/static","./static")

@app.route("/")
@jinja.template("about.html")  # decorator method is static method
async def homepage(request):
    return

@app.route("/blog1.html")
@jinja.template("blog1.html")  # decorator method is static method
async def blog1(request):
    return

@app.route("/blog2.html")
@jinja.template("blog2.html")  # decorator method is static method
async def blog2(request):
    return

@app.route("/blog3.html")
@jinja.template("blog3.html")  # decorator method is static method
async def blog3(request):
    return

@app.route("/contact.html")
@jinja.template("contact.html")  # decorator method is static method
async def contact(request):
    return

@app.route("/index.html")
@jinja.template("index.html")  # decorator method is static method
async def index(request):
    return

@app.route("/login.html")
@jinja.template("login.html")  # decorator method is static method
async def login(request):
    return

@app.route("/register.html")
@jinja.template("register.html")  # decorator method is static method
async def register(request):
    return

@app.route("/single.html")
@jinja.template("single.html")  # decorator method is static method
async def single(request):
    return

users = [{
    "id": 1,
    "name": "Sybilla Brodie",
    "email": "sbrodie0@digg.com",
    "pass": "uulHL0X"
}, {
    "id": 2,
    "name": "Imogen Nisby",
    "email": "inisby1@wikimedia.org",
    "pass": "AMOIBJ5rFcG"
}, {
    "id": 3,
    "name": "Dorise Oosthout de Vree",
    "email": "doosthout2@about.me",
    "pass": "RwFgqSYT"
}, {
    "id": 4,
    "name": "Pattin Bauchop",
    "email": "pbauchop3@ning.com",
    "pass": "fbUOAY0Ys"
}, {
    "id": 5,
    "name": "Sayer Hamper",
    "email": "shamper4@sourceforge.net",
    "pass": "6gFiaf"
}]


# Get all users
@app.route("/user")
async def test(request):
    return response.json(users)


# Get an user by ID
@app.route("/user/<id:int>")
async def get_user_by_id(request, id):
    for user in users:
        if user["id"] == id:
            return response.json(user)
    return response.json("")


# Get an user by email
@app.route("/user/<email:string>")
async def get_user_by_email(request, email):
    for user in users:
        if user["email"] == email:
            return response.json(user)
    return response.json("")


# Delete user by id
@app.route("/user/<id:int>", methods=['DELETE'])
async def delete_user_by_id(request, id):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return response.json("success")
    return response.json({
        "error": "user is not found"
    })


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


@app.route("/user/", methods=['POST'])
async def add_user(request):
    new_user = {}
    validate = True
    err_mess = ""
    new_user["id"] = users[-1]["id"] + 1
    new_user["name"] = request.form["name"][0]
    new_email = request.form["email"][0]
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, new_email):
        for user in users:
            if user["email"].lower() == new_email.lower():
                validate = False
                err_mess = "Email duplicate"

        new_user["email"] = new_email
    else:
        validate = False
        err_mess = "Invalid email"

    new_pass = request.form["pass"][0]
    if len(new_pass) < 6 or not hasNumbers(new_pass):
        err_mess = "Length pass is too short"
        validate = False
    else:
        new_user["pass"] = new_pass
    if validate:
        users.append(new_user)
        return response.json("success")
    else:
        return response.json({"error": err_mess})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
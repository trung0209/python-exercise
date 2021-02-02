import re
import os
from flask import Flask, render_template, request, json, redirect, url_for
from flaskext.mysql import MySQL

from sanic import Sanic, response
from sanic_jinja2 import SanicJinja2
# app = Sanic()
app = Flask(__name__,static_url_path='/static')
# jinja = SanicJinja2(app)
# jinja = SanicJinja2(app, pkg_name='web')

# app.static("/static","./static")
mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '881995sj'
app.config['MYSQL_DATABASE_DB'] = 'login_info'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
conn = mysql.connect()
cursor = conn.cursor()

users = [{
    "name": "Sybilla Brodie",
    "email": "sbrodie0@digg.com",
    "pass": "uulHL0X"
}, {
    "name": "Imogen Nisby",
    "email": "inisby1@wikimedia.org",
    "pass": "AMOIBJ5rFcG"
}, {
    "name": "Dorise Oosthout de Vree",
    "email": "doosthout2@about.me",
    "pass": "RwFgqSYT"
}, {
    "name": "Pattin Bauchop",
    "email": "pbauchop3@ning.com",
    "pass": "fbUOAY0Ys"
}, {
    "name": "Sayer Hamper",
    "email": "shamper4@sourceforge.net",
    "pass": "6gFiaf"
}]
sub_email = []

@app.route("/")
# @jinja.template("index.html")
def home():
    return render_template("index.html")

@app.route("/index.html")
# @jinja.template("index.html")  # decorator method is static method
def homepage():
    return render_template("index.html")

@app.route("/about.html")
# @jinja.template("about.html")  # decorator method is static method
def about():
    return render_template("about.html")

@app.route("/blog1.html")
# @jinja.template("blog1.html")  # decorator method is static method
def blog1():
    return render_template("blog1.html")

@app.route("/blog2.html")
# @jinja.template("blog2.html")  # decorator method is static method
def blog2():
    return render_template("blog2.html")

@app.route("/blog3.html")
# @jinja.template("blog3.html")  # decorator method is static method
def blog3():
    return render_template("blog3.html")

@app.route("/contact.html")
# @jinja.template("contact.html")  # decorator method is static method
def contact():
    return render_template("contact.html")

@app.route("/login.html")
# @jinja.template("login.html")  # decorator method is static method
def login():
    return render_template("login.html")

@app.route("/register.html")
# @jinja.template("register.html")  # decorator method is static method
def register():
    return render_template("register.html")

@app.route("/single.html")
# @jinja.template("single.html")  # decorator method is static method
def single():
    return render_template("single.html")

@app.route('/login.html', methods = ['POST'])
def signUp():
    if request.method == 'POST':
        email = request.form["Email"]
        password = request.form["Password"]
        cursor.callproc('CheckUser', (email, password))
        data = cursor.fetchall()
        print(data)
        if len(data) is 0:
            conn.commit()
            return json.dumps({'error': "login fail"})
        else:
            return redirect(url_for('homepage'))



# def hasNumbers(inputString):
#     return any(char.isdigit() for char in inputString)

@app.route('/register.html', methods = ['POST'])
def signIn():
    if request.method == 'POST':
        new_user = {}
        validate = True
        name = request.form["Name"]
        email = request.form["Email"]
        password1 = request.form["Password1"]
        # password2 = request.form["Password2"]
        cursor.callproc('create_User', (name, email, password1))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})

        # new_user["name"] = name
        # regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        # if email and password1 == password2 and name:
        #     if re.search(regex,email):
        #         for user in users:
        #             if user["email"].lower() == email.lower():
        #                 validate = False
        #                 return json.dumps({'message': "Invalid email"})
        #         new_user["email"] = email
            # if len(password1) < 6 or not hasNumbers(password1):
            #     validate = False
            #     return json.dumps({'message': "Length pass is too short"})
            # else:
            #     new_user["pass"] = password1
            # if validate:
            #     users.append(new_user)
            #     return json.dumps(users)
            #
            # else:
            #     return json.dumps({'message': "err_info"})
            # return redirect(url_for('homepage'))
        # else:
        #     return json.dumps({'message': "Invalid info"})

@app.route('/', methods = ['POST'])
def Summit():
    if request.method == 'POST':
        # email = request.form["email"]
        # regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        # if re.search(regex, email):
        #     sub_email.append(email)
        #     return json.dumps({'message': "Sumit successful"})
        # else:
        #     return json.dumps({'message': "Missing info"})
        email = request.form["email"]
        cursor.callproc('Addemail', (email))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({'message': 'Sumit successfully !'})
        else:
            return json.dumps({'error': str(data[0])})


@app.route('/index.html', methods = ['POST'])
def Summit1():
    if request.method == 'POST':
        # email = request.form["email"]
        # regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        # if re.search(regex, email):
        #     sub_email.append(email)
        #     return json.dumps({'message': "Sumit successful"})
        # else:
        #     return json.dumps({'message': "Missing info"})
        email = request.form["email"]
        cursor.callproc('Addemail', (email))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({'message': 'Sumit successfully !'})
        else:
            return json.dumps({'error': str(data[0])})

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8000, debug=True)
    app.run(debug=True)
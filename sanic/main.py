from sanic import Sanic
from sanic import response
from sanic_jinja2 import SanicJinja2   # pip install sanic_jinja2

app = Sanic()
jinja = SanicJinja2(app)
app.static("/image", "./photo")

@app.route("/")
@jinja.template('text.html')  # decorator method is static method
async def homepage(request):
    # return response.html("<h1>Chao anh Son</h1><p>Hôm nay trời mưa</p>")
    return


@app.route("/data")
async def test(request):
    return response.json(
        [{
            "first_name": "Geno",
            "last_name": "Leitche",
            "email": "gleitche0@newsvine.com"
        }, {
            "first_name": "Onofredo",
            "last_name": "Newtown",
            "email": "onewtown1@homestead.com"
        }, {
            "first_name": "Jareb",
            "last_name": "Freiberg",
            "email": "jfreiberg2@dyndns.org"
        }])


if __name__ == "__main__":
  app.run(debug=True, access_log=True)

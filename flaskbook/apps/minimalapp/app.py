from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return"hello, flaskbook!"

@app.route("/hello/<name>", methods=["GET","POST"], endpoint="hello-endpoint")
def hello(name):
    return "return f""HELLO,{name}!"

#show name
@app.route("/name/<name>")
def show_name(name):
    return render_template("indax.html",name=name)


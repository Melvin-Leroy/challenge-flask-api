from flask import Flask, redirect, render_template, request, url_for
from random import randint
import os


app = Flask(__name__)

@app.route("/")
def home():
    """
    The homepage of the website.
    """
    return "<h1>Welcome to MadCompany's website!</h1>"

@app.route("/status")
def status():
    """
    A page to get the status of the website.
    """
    return "Alive!"

@app.route("/predict/<seller_available>/<month>/<customer_visiting_website>")
def prediction(seller_available:int, month:str, customer_visiting_website:int):
    """
    Page that gives a random prediction.
    """
    prediction = randint(2000, 5000)
    return f"The prediction is {prediction}"

@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Page to login, then redirect you towards the logged in page.
    """
    if request.method == "POST":
        username = request.form["username"]
        password_length = len(request.form["password"])
        return redirect(url_for("logged_in", username=username, password_length=password_length))
    else:
        return render_template("login.html")

@app.route("/<username>/<password_length>")
def logged_in(username:str, password_length:int):
    """
    Logged in page where you see the username and the password's length.
    """
    return f"<h2>Login success for user '{username}' with password of length: {password_length}</h2>"

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 4000))
   app.run(host='0.0.0.0', port=port)
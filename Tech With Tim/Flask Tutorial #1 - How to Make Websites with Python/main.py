from datetime import timedelta
from flask import Flask, redirect, url_for, render_template, request, session, flash
from werkzeug.datastructures import ContentRange

app = Flask(__name__)
app.secret_key = "bonnie"
app.permanent_session_lifetime = timedelta(minutes=9999)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("new.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("Login"))

if __name__ == "__main__":
    app.run(debug = True)
    
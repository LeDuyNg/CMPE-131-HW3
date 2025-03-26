from app import myapp_obj
from flask import render_template
from flask import redirect
from app.forms import LoginForm
from app.models import User
from app import db


@myapp_obj.route("/")
def main():
    recipes = Recipe.query.all()
    return render_template("home.html", title = "Home Page", recipes = recipes)

@myapp_obj.route("/accounts")
def users():
    return "My USER ACCOUNTS"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("login.html", form=form)


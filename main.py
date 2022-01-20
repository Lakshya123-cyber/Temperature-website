from flask import Flask, render_template, request, redirect, url_for
from flask_navigation import Navigation

app = Flask(__name__)
nav = Navigation(app)

# initializing Navigations
nav.Bar('top', [
    nav.Item('Signup', 'signup'),
    nav.Item('Login', 'login', {'page': 1}),
])


@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for("login"))

    # show the form, it wasn't submitted
    return render_template("signup.html")


@app.route("/home")
def home():
    return render_template("home.html")


# Route for handling the login page logic
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("home"))
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)

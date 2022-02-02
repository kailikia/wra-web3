from distutils.log import debug
from flask import Flask, request, render_template

app = Flask(__name__)

## Frontend Routes

@app.route("/")
def home():
    return render_template("frontend/index.html")

@app.route("/about-us")
def about():
    return render_template("frontend/about.html")

@app.route("/projects")
def projects():
    return render_template("frontend/projects.html")

@app.route("/contact-us")
def contact():
    return render_template("frontend/contact.html")

@app.route("/tenders")
def tenders():
    return render_template("frontend/tenders.html")

@app.route("/publications")
def publications():
    return render_template("frontend/publications.html")

## End Frontend Routes

## Backend Routes



## Backend Roues


if __name__ == '__main__':
    app.run(debug=True)
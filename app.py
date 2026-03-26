import os
from modules.vector_store import add_pdf
from flask import Flask, render_template, request, redirect, url_for, session
from modules.llm_generator import generate_explanation
from modules.image_generator import generate_image

app = Flask(__name__)
# Secret key for session

from dotenv import load_dotenv
import os

load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")
# ---- ADD LOGIN CREDENTIALS HERE ----
USERNAME = "admin"
PASSWORD = "1234"

# ADD LOGIN ROUTE HERE
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:

            session["user"] = username

            return redirect(url_for("home"))

    return render_template("login.html")


# Home route (protected page)
@app.route("/", methods=["GET","POST"])
def home():

    if "user" not in session:
        return redirect(url_for("login"))

    explanation = None
    image_url = None

    if request.method == "POST":

        topic = request.form["topic"]

        explanation = generate_explanation(topic)
        image_url = generate_image(topic)
       
    return render_template(
        "index.html",
        explanation=explanation,
        image_url=image_url,
        user=session["user"]
    )


# Logout route
@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("login"))


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":
        file = request.files["file"]

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            add_pdf(filepath)

            return "✅ PDF uploaded and processed!"

    return '''
    <h2>Upload PDF</h2>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit">
    </form>
    '''
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, use_reloader=False)
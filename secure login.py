from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
import sqlite3
import re

app = Flask(__name__)

# Secret key for session management
app.secret_key = "change-this-to-a-random-secret-key"

bcrypt = Bcrypt(app)


# Database connection
def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create users table
def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Basic input validation
def valid_username(username):
    return re.match(r"^[A-Za-z0-9_]{3,30}$", username)


def valid_password(password):
    return len(password) >= 8


# Home page
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# Registration
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not valid_username(username):
            return "Invalid username. Use 3-30 letters, numbers or underscores."

        if not valid_password(password):
            return "Password must contain at least 8 characters."

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        try:
            conn = get_db()

            # Parameterized query prevents SQL injection
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()
            conn.close()

            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            return "Username already exists."

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        conn = get_db()

        # Parameterized query
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        conn.close()

        if user and bcrypt.check_password_hash(
            user["password"], password
        ):
            session.clear()
            session["username"] = user["username"]

            return redirect(url_for("dashboard"))

        return "Invalid username or password."

    return render_template("login.html")


# Protected dashboard
@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


# Logout
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)

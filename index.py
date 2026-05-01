from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def home():

    india = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(india).strftime("%d-%m-%Y %H:%M:%S")

    return f"""
    <html>

    <head>
        <title>Flask Interactive App</title>

        <style>

            body {{
                background-color: #0f172a;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }}

            .container {{
                width: 60%;
                margin: auto;
                background: #1e293b;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0px 0px 20px rgba(255,255,255,0.1);
            }}

            h1 {{
                color: #38bdf8;
                font-size: 50px;
            }}

            p {{
                font-size: 22px;
            }}

            .btn {{
                display: inline-block;
                margin-top: 20px;
                padding: 12px 25px;
                background: #38bdf8;
                color: black;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
            }}

            .btn:hover {{
                background: #0ea5e9;
                color: white;
            }}

        </style>

    </head>

    <body>

        <div class="container">

            <h1>🚀 Welcome to Flask App</h1>

            <p>Hello Suresh 👋</p>

            <p>Your Flask application is running successfully inside Docker.</p>

            <p>🕒 Current Server Time:</p>

            <h2>{current_time}</h2>

            <a class="btn" href="/about">About App</a>

        </div>

    </body>

    </html>
    """

@app.route("/about")
def about():

    return """
    <html>

    <head>

        <title>About</title>

        <style>

            body {
                background-color: #111827;
                color: white;
                font-family: Arial;
                text-align: center;
                padding-top: 100px;
            }

            h1 {
                color: #22c55e;
            }

            a {
                color: #38bdf8;
                text-decoration: none;
                font-size: 20px;
            }

        </style>

    </head>

    <body>

        <h1>📘 About This Project</h1>

        <p>This is an Interactive Flask Web Application.</p>

        <p>Created using Python + Flask + Docker 🐳</p>

        <br>

        <a href="/">⬅ Back to Home</a>

    </body>

    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
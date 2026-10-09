from flask import Flask, request, render_template
import mysql.connector
from dotenv import load_dotenv
import os
import hashlib

load_dotenv()

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test-db")
def test_db():
    cursor = db.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    cursor.close()
    return str(result)

@app.route("/add-data", methods=["POST"])
def add_data():
    data = request.json["data"]
    if not data or not data.strip():
        return {
            "status": "invalid",
            "message": "Invalid data"
        }
    data = " ".join(data.split())
    data_hash = hashlib.sha256(data.encode()).hexdigest()
    cursor = db.cursor()

    cursor.execute(
        "SELECT id FROM data_entries WHERE data_hash = %s",
        (data_hash,)
    )

    existing = cursor.fetchone()

    if existing:
        cursor.close()
        return {
                "status": "duplicate",
                "message": "Duplicate data detected"
        }

    cursor.execute(
        "INSERT INTO data_entries (data_value, data_hash) VALUES (%s, %s)",
        (data, data_hash)
    )

    db.commit()
    cursor.close()

    return {
    "status": "verified",
    "message": "Unique data added successfully"
    }

if __name__ == "__main__":
    app.run(debug=True)


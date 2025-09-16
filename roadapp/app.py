from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect("reports.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reports
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  lat REAL,
                  lng REAL,
                  description TEXT)''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_report", methods=["POST"])
def add_report():
    data = request.get_json()
    lat, lng, description = data["lat"], data["lng"], data["description"]

    conn = sqlite3.connect("reports.db")
    c = conn.cursor()
    c.execute("INSERT INTO reports (lat, lng, description) VALUES (?, ?, ?)", (lat, lng, description))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

@app.route("/get_reports")
def get_reports():
    conn = sqlite3.connect("reports.db")
    c = conn.cursor()
    c.execute("SELECT id, lat, lng, description FROM reports")
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

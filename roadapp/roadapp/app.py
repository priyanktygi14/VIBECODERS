from flask import Flask, render_template, request, jsonify
import json, os

app = Flask(__name__)

DATA_FILE = "reports.json"

def load_reports():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_reports(reports):
    with open(DATA_FILE, "w") as f:
        json.dump(reports, f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_reports")
def get_reports():
    return jsonify(load_reports())

@app.route("/report", methods=["POST"])
def report():
    data = request.get_json()
    reports = load_reports()
    reports.append(data)
    save_reports(reports)
    return jsonify({"status": "success"})

@app.route("/resolve", methods=["POST"])
def resolve():
    data = request.get_json()
    reports = load_reports()
    reports = [r for r in reports if not (r["lat"] == data["lat"] and r["lng"] == data["lng"] and r["issue"] == data["issue"])]
    save_reports(reports)
    return jsonify({"status": "resolved"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "James", "role": "DevOps Engineer"},
    {"id": 2, "name": "Sarah", "role": "Cloud Engineer"},
    {"id": 3, "name": "Michael", "role": "System Administrator"}
]

@app.route("/")
def home():
    return """
    <h1>Employee Management Application</h1>
    <p>Application is running successfully.</p>
    """

@app.route("/employees")
def get_employees():
    return jsonify(employees)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


    

jobs = load_jobs_from_db()


@app.route("/")
def index():
    return render_template("home.html", jobs=jobs)


# Returning the data in the form of an api
@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)
"""Week 4 DevSecOps dependency scanning demonstration."""

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    """Return project information."""
    return jsonify(
        project="DevSecOps Engineering",
        week=4,
        topic="Dependency Scanning and Software Composition Analysis",
        status="running",
    )


@app.get("/health")
def health():
    """Return application health information."""
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
    )
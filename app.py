from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1Updated Application Using CI/CD!</h1>
    <h2>Application Deployed Successfully!</h2>
    <p>This application uses:</p>
    <ul>
        <li>Python Flask</li>
        <li>GitHub</li>
        <li>Docker</li>
        <li>GitHub Actions</li>
        <li>Render Cloud</li>
    </ul>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
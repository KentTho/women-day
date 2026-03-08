"""
💐 International Women's Day Greeting Card - Flask Backend
A simple Flask app to serve a beautiful animated greeting card.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """Serve the main greeting card page."""
    return render_template("index.html")

if __name__ == "__main__":
    # Run locally for testing
    app.run(debug=True, host="0.0.0.0", port=5000)

from flask import Flask, render_template, request
from analyzer import checkUrl

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        raw_urls = request.form.get("urls", "")
        urls = [line.strip() for line in raw_urls.splitlines() if line.strip()]
        results = [checkUrl(url) for url in urls]

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

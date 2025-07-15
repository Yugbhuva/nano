from flask import Flask, redirect, abort, request, jsonify
from nanourls import expand_url, shorten_url

app = Flask(__name__)

@app.route("/")
def index():
    return "🚀 NanoURLs is alive!"

# 🔧 THIS is what you need!
@app.route("/shorten")
def shorten_route():
    long_url = request.args.get("url")
    if not long_url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    short = shorten_url(long_url)
    return jsonify({"short_url": short})

@app.route("/<short_code>")
def redirect_short_url(short_code):
    url = expand_url(short_code)
    if url:
        return redirect(url, code=302)
    return abort(404)

if __name__ == "__main__":
    app.run(debug=True)

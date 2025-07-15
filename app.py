from flask import Flask, redirect, abort
from nanourls import expand_url

app = Flask(__name__)

@app.route("/")
def index():
    return "🚀 Welcome to NanoURLs! Visit /<short_code> to be redirected."

@app.route("/<short_code>")
def redirect_short(short_code):
    url = expand_url(short_code)
    if url:
        return redirect(url, code=302)
    return abort(404)

if __name__ == "__main__":
    app.run(debug=True)
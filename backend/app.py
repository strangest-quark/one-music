from flask import Flask, request, jsonify
from handler.spotify.callback_handler import callback
from handler.spotify.auth_handler import auth

app = Flask(__name__)
app.config.from_object("config.config.DevelopmentConfig")

@app.route("/spotify/")
def spotify_auth():
    return auth()


@app.route("/spotify/callback/q")
def spotify_callback():
    return jsonify(callback(request))


if __name__ == "__main__":
    app.run(debug=True)

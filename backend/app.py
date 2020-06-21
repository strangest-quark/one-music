from flask import Flask, request, jsonify
from handler.spotify.callback_handler import callback
from handler.spotify.auth_handler import auth
from handler.spotify.playlists_handler import get_spotify_playlists

app = Flask(__name__)
app.config.from_object("config.config.ProductionConfig")

@app.route("/spotify/")
def spotify_auth():
    return auth()

@app.route("/spotify/callback/q")
def spotify_callback():
    return callback(request)

@app.route("/spotify/playlists/")
def spotify_playlists():
    return jsonify(get_spotify_playlists(request))

if __name__ == "__main__":
    app.run(debug=True)

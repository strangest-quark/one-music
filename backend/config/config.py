class Config(object):
    SPOTIFY_API_BASE_URL = "https://api.spotify.com"
    API_VERSION = "v1"

    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)
    SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
    USER_PROFILE_API_ENDPOINT = "{}/me".format(SPOTIFY_API_URL)
    PLAYLIST_API_ENDPOINT = "{}/playlists"

    #  Client Keys
    CLIENT_ID = "6d48227f162e4ce2a90bbf26de9e5237"
    CLIENT_SECRET = "283efbd6be4044e58198e30fd906ce2f"

    # CLIENT_SIDE_URL = "https://rx00516zgh.execute-api.us-west-2.amazonaws.com/dev"
    CLIENT_SIDE_URL = "http://127.0.0.1"
    # REDIRECT_URI = "{}/callback/q".format(CLIENT_SIDE_URL)
    REDIRECT_URI = "{}:{}/spotify/callback/q".format(CLIENT_SIDE_URL, 5000)
    SCOPE = "playlist-modify-public playlist-modify-private"

    auth_query_parameters = {
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        # "state": STATE,
        # "show_dialog": SHOW_DIALOG_str,
        "client_id": CLIENT_ID
    }


class DevelopmentConfig(Config):
    CLIENT_SIDE_URL = "http://127.0.0.1"
    REDIRECT_URI = "{}:{}/spotify/callback/q".format(CLIENT_SIDE_URL, 5000)


class ProductionConfig(Config):
    CLIENT_SIDE_URL = "https://rx00516zgh.execute-api.us-west-2.amazonaws.com/dev"
    REDIRECT_URI = "{}/callback/q".format(CLIENT_SIDE_URL)

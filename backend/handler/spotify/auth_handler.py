from flask import current_app, redirect
from urllib.parse import quote


def auth():
    SCOPE = current_app.config['SCOPE']
    auth_query_parameters = {
        "response_type": "code",
        "redirect_uri": current_app.config['REDIRECT_URI'],
        "scope": SCOPE,
        # "state": STATE,
        # "show_dialog": SHOW_DIALOG_str,
        "client_id": current_app.config['CLIENT_ID']
    }
    url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(current_app.config['SPOTIFY_AUTH_URL'], url_args)
    return redirect(auth_url)

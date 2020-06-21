from client.spotify.client import get_spotify_auth_header
from client.spotify.client import get_profile_data
from client.spotify.client import get_playlist_data
from urllib.request import urlretrieve
from urllib.parse import urlencode
from flask import current_app, redirect


def callback(request):
    access_token, refresh_token, expires_in = get_spotify_auth_header(request)
    query_dict = {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'expires_in': expires_in
    }
    qstr = urlencode(query_dict)
    return redirect(current_app.config['CLIENT_SIDE_URL']+'?' + qstr)

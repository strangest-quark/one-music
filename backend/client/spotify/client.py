import json
import requests
from flask import current_app
from util.spotify_parse import playlist_response_parse


def get_spotify_auth_header(callback_payload):
    auth_token = callback_payload.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": current_app.config['REDIRECT_URI'],
        'client_id': current_app.config['CLIENT_ID'],
        'client_secret': current_app.config['CLIENT_SECRET'],
    }
    post_request = requests.post(current_app.config['SPOTIFY_TOKEN_URL'], data=code_payload)
    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    # Auth Step 6: Use the access token to access Spotify API
    authorization_header = {"Authorization": "Bearer {}".format(access_token)}

    return authorization_header


def get_profile_data(authorization_header):
    profile_response = requests.get(current_app.config['USER_PROFILE_API_ENDPOINT'], headers=authorization_header)
    profile_data = json.loads(profile_response.text)
    return profile_data


def get_playlist_data(authorization_header, profile_href):
    playlists_response = requests.get(current_app.config['PLAYLIST_API_ENDPOINT'].format(profile_href), headers=authorization_header)
    playlist_data = json.loads(playlists_response.text)
    return playlist_response_parse(playlist_data)

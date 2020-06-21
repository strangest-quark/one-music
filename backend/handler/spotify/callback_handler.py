from client.spotify.client import get_spotify_auth_header
from client.spotify.client import get_profile_data
from client.spotify.client import get_playlist_data


def callback(request):
    authorization_header = get_spotify_auth_header(request)
    # Get profile data
    profile_data = get_profile_data(authorization_header)
    callback_response = dict()
    callback_response['name'] = profile_data['display_name']
    return callback_response

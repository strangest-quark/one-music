from client.spotify.client import get_spotify_auth_header
from client.spotify.client import get_profile_data
from client.spotify.client import get_playlist_data


def callback(request):
    authorization_header = get_spotify_auth_header(request)
    # Get profile data
    profile_data = get_profile_data(authorization_header)
    # Get user playlist data
    playlist_data = get_playlist_data(authorization_header, profile_data['href'])
    callback_response = dict()
    callback_response['name'] = profile_data['display_name']
    callback_response['playlists'] = playlist_data
    return callback_response

from util.common_util import give_emoji_free_text

def playlist_response_parse(playlist_res):
    playlist_names=[]
    for item in playlist_res['items']:
        playlist_names.append(give_emoji_free_text(item['name'].encode('utf-8')))
    return playlist_names
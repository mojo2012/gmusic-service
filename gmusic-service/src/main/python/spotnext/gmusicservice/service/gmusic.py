from gmusicapi import Mobileclient
from gmusicapi.clients import Musicmanager
from gmusicapi.clients import Webclient
import os

#musicManager = Musicmanager()
oauthPath = os.path.expanduser(
    '~/Library/Application Support/gmusicapi/mobileclient.cred')

# if not os.path.isfile(oauthPath):
#	auth = musicManager.perform_oauth(oauthPath, True)

#webClient = Webclient();
#webClient.login('meister.fuchs@gmail.com', 'gjxkaafjnelwjqsw')

#devices = webClient.get_registered_devices()

api = Mobileclient()

if not os.path.isfile(oauthPath):
    print('Creating oauth token ...')
    auth = musicManager.perform_oauth(oauthPath, True)

print('Logging in ...')
api.oauth_login(
    '0d13904bfde464ca3111034dff1b1353ecbf84984eb14967d3ce3347d4505103', oauthPath)

devices = api.get_registered_devices()

print('Registered devices:')

for device in devices:
    print(' ' + device['id'])

songs = api.get_all_songs()

for song in songs:
    print(song['artist'] + " - " + song['title'])

# library = api.get_all_songs()
# sweet_track_ids = [track['id'] for track in library
#                    if track['artist'] == 'The Cat Empire']

# playlist_id = api.create_playlist('Rad muzak')
# api.add_songs_to_playlist(playlist_id, sweet_track_ids)

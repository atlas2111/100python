import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random


def generate_playlist(sp, genres, mood, duration):
    # Fetch music data based on user preferences
    results = sp.recommendations(seed_genres=genres, target_valence=mood, limit=duration)

    # Extract track names and artists from results
    playlist = [(track['name'], ', '.join(artist['name'] for artist in track['artists'])) for track in
                results['tracks']]

    return playlist


if __name__ == "__main__":
    # Spotify API authentication
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    # Example preferences
    genres = ['pop', 'rock']
    mood = 0.8  # Valence (0-1) representing positivity of mood
    duration = 10  # Number of tracks in the playlist

    playlist = generate_playlist(sp, genres, mood, duration)

    # Create a new playlist
    user_id = sp.me()['id']
    playlist_name = "Generated Playlist"
    sp.user_playlist_create(user=user_id, name=playlist_name, public=True)

    # Add tracks to the new playlist
    playlist_id = sp.user_playlists(user_id)['items'][0]['id']  # Get the ID of the newly created playlist
    track_uris = [track['uri'] for track in results['tracks']]
    sp.playlist_add_items(playlist_id, track_uris)

    print(f"Playlist '{playlist_name}' created and populated with {duration} tracks:")
    for i, (track, artists) in enumerate(playlist, 1):
        print(f"{i}. {track} - {artists}")

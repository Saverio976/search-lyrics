from search_lyrics import search_lyrics
import argparse

def entrypoint():
    parser = argparse.ArgumentParser("Search for song containing lyrics")
    parser.add_argument("--artist", nargs=1, metavar="artist", type=str, help="Artist to search text into")
    parser.add_argument("--text", nargs=1, metavar="text", type=str, help="text to search")
    parser.add_argument("--genius-access-token", nargs=1, metavar="genius_access_token", type=str, default=[None], help="access token to use for genius api (by default, search for GENIUS_ACCESS_TOKEN in ENV variables)")
    parser.add_argument("--verbose", action="store_const", const=True, default=False, help="Enable verbose output")
    args = parser.parse_args()
    songs = search_lyrics(args.artist[0], args.text[0], args.genius_access_token[0], args.verbose)
    for song in songs:
        print(song.title)

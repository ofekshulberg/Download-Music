from pytube import Playlist

def get_playlist(playlists):
    # Initialize an empty list to store URLs
    urls = []

    # Loop through each playlist URL provided
    for playlist in playlists:
        # Create a Playlist object using pytube library
        playlist_url = Playlist(playlist)

        # Iterate through each video URL in the playlist
        for url in playlist_url:
            # Append each video URL to the 'urls' list
            urls.append(url)

    # Return the list of URLs
    return urls


# Define the URL of the playlist on YouTube
# Insert here the url of your desired playlist
playlist = ['https://www.youtube.com/playlist?list=PLl...']

# Call the get_playlist function to extract video URLs from the playlist
pl_url = get_playlist(playlist)

# Open a file named 'url_list.txt' in write mode
with open('url_list.txt', 'w') as f:
    # Initialize an empty list to store formatted URLs
    lst = []

    # Loop through each URL extracted from the playlist
    for url in pl_url:
        # Format each URL and write it to the file
        f.write("'" + url + "'" + '\n')

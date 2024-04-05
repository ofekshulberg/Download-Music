import os
import shutil
from pytube import YouTube


def url_to_mp3(video_url: str):
    # Using pytube library to access YouTube video and extract audio only
    video_file = YouTube(video_url).streams.filter().get_audio_only()

    # Downloading the audio-only file from the YouTube video
    video_file.download()

    # Extracting the file names for mp4 and mp3 files
    mp4_file: str = video_file.default_filename
    mp3_file: str = mp4_file.replace('.mp4', '.mp3')

    # Renaming the downloaded file from .mp4 to .mp3
    os.rename(mp4_file, mp3_file)

    # Moving the mp3 file to the 'audio' directory
    shutil.move(mp3_file, 'audio')


def main():
    # Opening a file containing a list of YouTube video URLs
    with open('url_list.txt', 'r') as f:
        # Iterating through each URL in the file
        for i in f:
            # Calling the url_to_mp3 function to download and convert each video to mp3
            url_to_mp3(i)


if __name__ == '__main__':
    # Calling the main function when the script is executed directly
    main()


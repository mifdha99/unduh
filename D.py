```python
import os
import subprocess
import requests
from pytube import YouTube
from facebook_scraper import get_posts
from instaloader import Instaloader
import tweepy
import tiktokapi

def download_youtube_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(output_path='downloads')
    print("YouTube video downloaded successfully!")

def download_facebook_video(post_url):
    for post in get_posts(post_url, pages=1):
        if 'video' in post:
            video_url = post['video']
            response = requests.get(video_url, stream=True)
            with open('downloads/facebook_video.mp4', 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            print("Facebook video downloaded successfully!")

def download_instagram_video(username, post_url):
    L = Instaloader()
    L.download_post(post_url, target='downloads')
    print("Instagram video downloaded successfully!")

def download_twitter_video(tweet_url):
    api_key = 'your_api_key'
    api_secret_key = 'your_api_secret_key'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweet = api.get_status(tweet_url)
    video_url = tweet.extended_entities['media'][0]['video_info']['variants'][0]['url']
    response = requests.get(video_url, stream=True)
    with open('downloads/twitter_video.mp4', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    print("Twitter video downloaded successfully!")

def download_tiktok_video(video_url):
    api = tiktokapi.TikTokAPI()
    video_data = api.get_video_info(video_url)
    video_url = video_data['video']['download_addr']['url_list'][0]
    response = requests.get(video_url, stream=True)
    with open('downloads/tiktok_video.mp4', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    print("TikTok video downloaded successfully!")

def main():
    os.makedirs('downloads', exist_ok=True)
    print("Social Media Video Downloader")
    print("1. YouTube")
    print("2. Facebook")
    print("3. Instagram")
    print("4. Twitter")
    print("5. TikTok")
    choice = input("Select a platform: ")

    if choice == '1':
        url = input("Enter YouTube video URL: ")
        download_youtube_video(url)
    elif choice == '2':
        url = input("Enter Facebook post URL: ")
        download_facebook_video(url)
    elif choice == '3':
        username = input("Enter Instagram username: ")
        post_url = input("Enter Instagram post URL: ")
        download_instagram_video(username, post_url)
    elif choice == '4':
        url = input("Enter Twitter tweet URL: ")
        download_twitter_video(url)
    elif choice == '5':
        url = input("Enter TikTok video URL: ")
        download_tiktok_video(url)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
```

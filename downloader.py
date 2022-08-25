
#for if this code does not works I recommand you to install pytube first
# So you can go directly on Powershell and type: pip install pytube
from pytube import YouTube
#Enter youtube video's Url that you want to download
video_url = "Replace Url here "
video = YouTube(video_url)
print("Video title:",video.title)
video = video.streams.get_highest_resolution()
video.download()
#Node: The video that have downloaded will be the same sile of your code 

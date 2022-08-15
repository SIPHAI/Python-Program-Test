
#for if this code does not works I recommand you to install pytube first
# So you can go directly on Powershell and type: pip install pytube
from pytube import YouTube
video_url = "https://www.youtube.com/watch?v=gdNW548KFVE "
video = YouTube(video_url)
print("Video title:",video.title)
video = video.streams.get_highest_resolution()
video.download()

#Youtube video downloader

from pytube import YouTube

link = input("Enter video URL : ")
youtube_1 = YouTube(link)

videos = youtube_1.streams.all()
vid = list(enumerate(videos)) 
                     
for i in vid:
    print(i)
print()

strm = int(input("enter video type number : "))

videos[strm].download()

print("Video Successfully Downloaded")
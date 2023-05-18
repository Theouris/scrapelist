#pip install pytube

my_file = open("videolinks.txt", "r")
data = my_file.read()
i = data.split("\n")
print(i)
my_file.close()

listt = []
listy = []

for item in i:
    if len(item) == 52:
        listy.append(item)
    else:
        listt.append(item)

print(listy)
print(listt)

from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

for item in listy:
    youtube = YouTube(item)
    my_video = youtube.streams.first()
    my_video.download('~Downloads')

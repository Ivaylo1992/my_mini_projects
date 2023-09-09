from pytube import YouTube

link = input('Enter the link of the video that you want to download: ')

yt = YouTube(link)

#download the stream with the highest resulution
yd = yt.streams.get_highest_resolution()

#in the brackets enter the directory in which you want to store the videos
yd.download('/Users\Ivaylo\Desktop')
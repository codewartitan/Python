from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=4nCshJBODT4")
yt = yt.streams.first()
yt.download('/home/codewar/Videos/Down_Vidoes')

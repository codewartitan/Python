from pytube import YouTube
# install don't install pytube but instead use pytube3
yt = YouTube("https://www.youtube.com/watch?v=tSF0NoG90-E&t=276s")


def show_progress_bar(self, chunk,  bytes_remaining):
    progress = round((1 - bytes_remaining / self.filesize) * 100, 2), '% done...'
    print (progress)



yt.register_on_progress_callback(show_progress_bar)
yt = yt.streams.first()
yt.download('C:/Users/msame/OneDrive/Camera Roll/Documents/Videos')
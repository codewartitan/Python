from pytube import YouTube
# install don't install pytube but instead use pytube3

yt = YouTube("https://www.youtube.com/watch?v=2lMTvmsP55U")


def show_progress_bar(self, chunk, bytes_remaining):
    progress = round((1 - bytes_remaining / self.filesize) * 100, 2), '% done...'
    print(progress)
    # if progress == '100.0':
    #     print('Download Completed')


yt.register_on_progress_callback(show_progress_bar)
# yt = yt.streams
# print(yt)
# yt.download('/Users/sameer/Downloads')


yt_mp4 = yt.streams.filter(subtype='mp4')
print(yt_mp4)
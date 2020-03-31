import sys
from pytube import YouTube
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

if __name__ == "__main__":
    app = QApplication([])
    w = QWidget()
    # First Group Inputs
    VideoUrl = QLabel(w)
    VideoUrl.setText('videoURL')
    # VideoUrl.move(100, 40)
    InputText = QLineEdit(w)
    # InputText.setFixedWidth(330)
    # InputText.move(100, 60)
    DownloadButton = QPushButton(w)
    DownloadButton.setText('Download')
    # CancelButton = QPushButton(w)
    # CancelButton.setText('Cancel')

    # Second Group Inputs
    Outputlabel = QLabel(w)
    Outputlabel.setText('Output Directory')
    Outputinput = QLineEdit(w)
    BrowseButton = QPushButton(w)
    BrowseButton.setText('Browse')

    # First Group
    hbox = QHBoxLayout()
    # hbox.addStretch(1)
    hbox.addWidget(VideoUrl)
    hbox.addWidget(InputText)
    hbox.addWidget(DownloadButton)
    # hbox.addWidget(CancelButton)
    # w.setLayout(hbox)

    # Second Group
    hbox1 = QHBoxLayout()
    hbox1.addWidget(Outputlabel)
    hbox1.addWidget(Outputinput)
    hbox1.addWidget(BrowseButton)

    vbox = QVBoxLayout()
    # vbox.addStretch(1)
    vbox.addLayout(hbox)
    vbox.addLayout(hbox1)
    w.setLayout(vbox)


def clickMethod():
    # print("You clicked PushButton")
    YouTubeURL = InputText.text()

    def show_progress_bar(self, chunk, bytes_remaining):
        progress = round((1 - bytes_remaining / self.filesize) * 100, 2), '% done...'
        print(progress)

    output = QLabel(w)
    if YouTubeURL == '':
        output.setText('Please Enter the Youtube URL')
        output.setFixedWidth(330)
        output.move(200, 300)
        output.show()
    else:
        yt = YouTube(YouTubeURL)
        yt.register_on_progress_callback(show_progress_bar)
        yt = yt.streams.first()
        yt.download('/Users/sameer/Downloads')
        output.setText('Download Completed')
        output.move(150, 150)
        output.show()


DownloadButton.clicked.connect(clickMethod)

w.resize(700, 500)

w.show()
sys.exit(app.exec_())

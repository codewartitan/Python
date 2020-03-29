import sys
from pytube import YouTube
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

if __name__ == "__main__":
    app = QApplication([])
    w = QWidget()
    VideoUrl = QLabel(w)
    VideoUrl.setText('videoURL')
    VideoUrl.move(100, 40)
    InputText = QLineEdit(w)
    InputText.setFixedWidth(330)
    # InputText.move(100, 60)
    Button = QPushButton(w)
    Button.setText('Download')
    # Button.move(90, 85)

    # okButton = QPushButton("OK")
    # cancelButton = QPushButton("Cancel")

    hbox = QHBoxLayout()
    hbox.addStretch(1)
    hbox.addWidget(InputText)
    hbox.addWidget(Button)

    vbox = QVBoxLayout()
    vbox.addStretch(1)
    vbox.addLayout(hbox)
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
        output.move(150, 150)
        output.show()
    else:
        yt = YouTube(YouTubeURL)
        yt.register_on_progress_callback(show_progress_bar)
        yt = yt.streams.first()
        yt.download('/Users/sameer/Downloads')
        output.setText('Download Completed')
        output.move(150, 150)
        output.show()


Button.clicked.connect(clickMethod)

w.resize(700, 500)

w.show()
sys.exit(app.exec_())

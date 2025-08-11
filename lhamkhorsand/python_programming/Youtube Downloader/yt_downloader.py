from PyQt5.QtWidgets import QApplication, QMainWindow
import yt_dlp
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from yt_ui import Ui_Dialog
from PyQt5.QtGui import QPixmap
from urllib.request import urlopen
import sys
import os
from pathlib import Path
import platform
import subprocess


class DownloadThread(QThread):
    formats_ready = pyqtSignal(list)
    info_ready = pyqtSignal(tuple)  # (title, thumbnail_url)
    progress = pyqtSignal(str)
    progress_percent = pyqtSignal(int)
    finished_with_path = pyqtSignal(str)

    def __init__(self, url, format_id=None, download=False):
        super().__init__()
        self.url = url
        self.format_id = format_id
        self.download = download

    def run(self):
        try:
            with yt_dlp.YoutubeDL({}) as ydl:
                info = ydl.extract_info(self.url, download=False)
                title = info.get("title", "Unknown Title")
                thumbnail_url = info.get("thumbnail", "")
                self.video_info = (title, thumbnail_url)

                if not self.download:
                    formats = info.get('formats', [])
                    preferred_resolutions = [360, 720, 1080]
                    format_map = {}

                    # for f in formats:
                    #     fmt_id = f.get('format_id')
                    #     ext = f.get('ext')
                    #     height = f.get('height')
                    #     vcodec = f.get('vcodec')
                    #     acodec = f.get('acodec')
                    #
                    #     if not fmt_id or not ext:
                    #         continue
                    #
                    #     if vcodec == 'none' and acodec != 'none':
                    #         label = f"Audio Only - {ext}"
                    #         if label not in format_map:
                    #             format_map[label] = fmt_id
                    #         continue
                    #
                    #     if vcodec != 'none' and isinstance(height, int):
                    #         if height in preferred_resolutions:
                    #             label = f"{height}p.{ext}"
                    #             if label not in format_map:
                    #                 format_map[label] = fmt_id

                    best_format_per_resolution = {}
                    audio_only_formats = {}

                    for f in formats:
                        fmt_id = f.get('format_id')
                        ext = f.get('ext')
                        height = f.get('height')
                        vcodec = f.get('vcodec')
                        acodec = f.get('acodec')
                        bitrate = f.get('tbr') or 0

                        if not fmt_id or not ext:
                            continue

                        if vcodec == 'none' and acodec != 'none':
                            if ext == 'webm':
                                label = f"Audio Only - {ext}"
                                if label not in audio_only_formats or bitrate > (audio_only_formats[label][1] or 0):
                                    audio_only_formats[label] = (fmt_id, bitrate)
                            continue

                        if height and isinstance(height, int):
                            if height in preferred_resolutions:
                                key = f"{height}p.{ext}"
                                if key not in best_format_per_resolution or bitrate > (best_format_per_resolution[key][1] or 0):
                                    if vcodec != 'none' and acodec != 'none':
                                        best_format_per_resolution[key] = (fmt_id, bitrate)
                                    elif vcodec != 'none' and acodec == 'none':
                                        best_format_per_resolution[key] = (f"{fmt_id}+bestaudio", bitrate)

                    selected_formats = [(v[0], k) for k, v in best_format_per_resolution.items()]
                    selected_formats += [(v[0], k) for k, v in audio_only_formats.items()]

                    if not selected_formats:
                        self.progress.emit("No downloadable formats found.")

                    self.formats_ready.emit(selected_formats)

                    self.info_ready.emit(self.video_info)
                else:
                    downloads_folder = str(Path.home() / "Downloads")

                    if "Audio Only" in self.format_id:
                        ydl_opts = {
                            'format': self.format_id,
                            'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
                            'progress_hooks': [self.my_hook],
                        }

                    else:
                        ydl_opts = {
                            'format': self.format_id,
                            'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
                            'progress_hooks': [self.my_hook],
                            'merge_output_format': 'mp4',
                        }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl2:
                        ydl2.download([self.url])
                        self.progress.emit('✅ D o w n l o a d   c o m p l e t e d.')
        except Exception as e:
            self.progress.emit(f'Error: {str(e)}')

    def my_hook(self, d):
        if d['status'] == 'downloading':
            percent_str = d.get('_percent_str')
            if percent_str:
                percent = percent_str.strip().replace('%', '')
                try:
                    self.progress_percent.emit(int(float(percent)))
                except:
                    pass
            else:
                self.progress.emit("Downloading... (progress unknown)")
        elif d['status'] == 'finished':
            self.progress_percent.emit(100)
            self.progress.emit('✅ D o w n l o a d   c o m p l e t e d.')
            if 'filename' in d:
                self.finished_with_path.emit(d['filename'])



class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.progressBar.hide()
        self.ui.pushButton_2.hide()
        self.ui.comboBox.hide()
        self.ui.pushButton.clicked.connect(self.start_fetch_formats)
        self.ui.comboBox.currentIndexChanged.connect(self.format_selected)
        self.ui.pushButton_2.clicked.connect(self.download_video)
        self.ui.pushButton_open_folder.clicked.connect(self.open_folder)
        self.last_download_path = None
        self.selected_format_id = None

    def start_fetch_formats(self):
        url = self.ui.lineEdit.text().strip()
        if not url:
            self.ui.label.setText('Please enter a URL')
            return
        self.ui.label_2.setText('G e t t i n g   I n f o r m a t i o n . . . ')
        self.thread = DownloadThread(url)
        self.thread.formats_ready.connect(self.populate_combo)
        self.thread.info_ready.connect(self.display_info)
        self.thread.progress.connect(self.ui.label_2.setText)
        self.thread.start()

    def populate_combo(self, formats):
        self.ui.comboBox.clear()
        for fmt_id, label in formats:
            self.ui.comboBox.addItem(label, fmt_id)
        self.ui.comboBox.show()
        self.ui.label_2.setText('C h o o s e   Q u a l i t y!')

    def display_info(self, info):
        title, thumb_url = info
        self.ui.label_4.setText(title)
        try:
            data = urlopen(thumb_url).read()
            image = QPixmap()
            image.loadFromData(data)
            self.ui.label_3.setPixmap(image.scaled(480, 270))
        except:
            self.ui.label_3.setText("Failed to load thumbnail.")

    def format_selected(self, index):
        self.selected_format_id = self.ui.comboBox.itemData(index)
        self.ui.pushButton_2.show()
        self.ui.label_2.setText('C l i c k   D o w n l o a d!')

    def download_video(self):
        if not self.selected_format_id:
            self.ui.label_2.setText('Please select a format first!')
            return
        url = self.ui.lineEdit.text().strip()
        self.ui.label_2.setText('D o w n l o a d i n g . . . ')
        self.ui.progressBar.setRange(0, 0)
        self.ui.progressBar.show()

        self.thread = DownloadThread(url, format_id=self.selected_format_id, download=True)
        self.thread.progress.connect(self.ui.label_2.setText, Qt.QueuedConnection)
        self.thread.progress_percent.connect(self.update_progress_bar, Qt.QueuedConnection)
        self.thread.finished_with_path.connect(self.download_finished)
        self.thread.start()

    def update_progress_bar(self, val):
        if self.ui.progressBar.maximum() == 0:
            self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(val)

    def download_finished(self, path):
        self.last_download_path = path
        self.ui.pushButton_open_folder.setVisible(True)

    def open_folder(self):
        if self.last_download_path:
            folder = os.path.dirname(self.last_download_path)
            try:
                if platform.system() == "Windows":
                    os.startfile(folder)
                elif platform.system() == "Darwin":
                    subprocess.Popen(["open", folder])
                else:
                    subprocess.Popen(["xdg-open", folder])
            except Exception as e:
                self.ui.label_2.setText(f"Could not open folder: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    downloader_app = MyApp()
    downloader_app.show()
    sys.exit(app.exec_())



























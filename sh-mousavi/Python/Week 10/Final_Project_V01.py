
from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog, QApplication, QMessageBox, QMainWindow
from PyQt6.QtCore import QStringListModel
import urllib.request
import sys
import os
import os.path

ui,_ = uic.loadUiType('Final_Project.ui')

class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.handle_button()

        self.downloaded_files = []  # List to store downloaded file paths
        self.model = QStringListModel()  # Persistent model for the list view

    def handle_button(self):
        self.push_FD_Browse.clicked.connect(self.handle_browse)
        self.push_FD_DL.clicked.connect(self.download)


    def handle_progress(self, blocknum, blocksize, totalsize):
        read_data = blocknum * blocksize
        if totalsize > 0:
            download_percentage = read_data * 100 / totalsize
            self.progressBar_FD.setValue(int(download_percentage))
            QApplication.processEvents()


    def handle_browse(self):
        # save_location, _ = QFileDialog.getSaveFileName(self, "Save as", "", "All Files (*)")
        # self.lineEdit_FD_SAVE.setText(save_location)
        save_folder = QFileDialog.getExistingDirectory(self, "Select Folder", "")

        # file_name = str(self.lineEdit_FD_URL.text()).split("/")
        # save_location = save_folder + "/" + file_name[-1]
        file_name = os.path.basename(str(self.lineEdit_FD_URL.text()))
        save_location = os.path.normpath(os.path.join(save_folder, file_name))
        if save_location:
            self.lineEdit_FD_SAVE.setText(save_location)


    def download(self):
        download_url = self.lineEdit_FD_URL.text()
        save_location = self.lineEdit_FD_SAVE.text()

        if download_url == "" and save_location == "":
            QMessageBox.warning(self, "Data Error - Empty Boxes", "None of the Boxes can be Left Empty")
        elif download_url == "":
            QMessageBox.warning(self, "Data Error - Empty URL", "Program Requires a Valid URL")
        elif save_location == "":
            QMessageBox.warning(self, "Data Error - Empty Location", "You Must Specify a Valid Location")
        else:
            try:
                urllib.request.urlretrieve(url=download_url, filename=save_location, reporthook=self.handle_progress)
                # urllib.request.urlretrieve(download_url, save_location, self.handle_progress)
                QMessageBox.information(self, "Download Completed", "Download Completed Successfully")

                self.lineEdit_FD_URL.setText("")
                self.lineEdit_FD_SAVE.setText("")
                self.progressBar_FD.setValue(0)

                # Add downloaded file to the list
                self.downloaded_files.append(save_location)
                self.model.setStringList(self.downloaded_files)
                self.listView_FD.setModel(self.model)

            except ValueError:
                QMessageBox.warning(self, "Download Error - Invalid Path", "Check URL or Save Location")
            except Exception:
                QMessageBox.warning(self, "Download Error - Unknown", "Unknown Error Occurred")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

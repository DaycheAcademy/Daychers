from PyQt5 import QtCore, QtGui, QtWidgets
import platform

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        font_family = "Segoe UI" if platform.system() == "Windows" else "Sans Serif"
        font = QtGui.QFont(font_family, 11)
        Dialog.setFont(font)
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 700)
        font_bold = QtGui.QFont(font_family, 11)
        font_bold.setBold(True)
        Dialog.setFont(font_bold)
        Dialog.setStyleSheet("background-color: #1E1E1E;")

        self.centralWidget = QtWidgets.QWidget(Dialog)
        self.centralWidget.setGeometry(QtCore.QRect(0, 0, 900, 700))
        self.centralWidget.setObjectName("centralWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(20, 15, 20, 15)
        self.verticalLayout.setSpacing(25)

        self.label = QtWidgets.QLabel(self.centralWidget)
        font_title = QtGui.QFont(font_family, 22, QtGui.QFont.Bold)
        self.label.setFont(font_title)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("YouTube Video Downloader")
        self.verticalLayout.addWidget(self.label)

        self.hInputLayout = QtWidgets.QHBoxLayout()
        self.hInputLayout.setSpacing(15)

        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setStyleSheet("""
            QLineEdit {
                background-color: #2B2B2B;
                color: #E0E0E0;
                padding: 8px;
                border: none;
                border-radius: 3px;
            }
        """)
        self.lineEdit.setPlaceholderText("Enter YouTube URL")
        self.hInputLayout.addWidget(self.lineEdit)

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #3A3A3A;
                color: #F0F0F0;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
        """)
        self.pushButton.setText("Get Information")
        self.hInputLayout.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.hInputLayout)

        self.hComboLayout = QtWidgets.QHBoxLayout()
        self.hComboLayout.setSpacing(15)

        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setStyleSheet("""
            QComboBox {
                background-color: #2B2B2B;
                color: #E0E0E0;
                padding: 8px;
                border: none;
                border-radius: 3px;
            }
            QComboBox QAbstractItemView {
                background-color: #2B2B2B;
                color: #E0E0E0;
                selection-background-color: #4CAF50;
                selection-color: #000000;
            }
        """)
        self.hComboLayout.addWidget(self.comboBox)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: #3A3A3A;
                color: #F0F0F0;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
        """)
        self.pushButton_2.setText("Download")
        self.hComboLayout.addWidget(self.pushButton_2)

        self.pushButton_open_folder = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_open_folder.setText("Open Folder")
        self.pushButton_open_folder.setStyleSheet("""
            QPushButton {
                background-color: #3A3A3A;
                color: #F0F0F0;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
        """)
        self.pushButton_open_folder.setVisible(False)
        self.hComboLayout.addWidget(self.pushButton_open_folder)

        self.verticalLayout.addLayout(self.hComboLayout)

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont(font_family, 10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #4CAF50;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setText("")
        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setMinimumSize(QtCore.QSize(480, 270))
        self.label_3.setMaximumSize(QtCore.QSize(480, 270))
        self.label_3.setStyleSheet("""
            QLabel {
                background-color: #1E1E1E;
                border: none;
                border-radius: 4px;
            }
        """)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setText("")
        self.verticalLayout.addWidget(self.label_3, alignment=QtCore.Qt.AlignCenter)

        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setFixedHeight(25)
        self.progressBar.setStyleSheet("""
            QProgressBar {
                background-color: #2B2B2B;
                color: white;
                border: none;
                border-radius: 4px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 4px;
            }
        """)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setProperty("value", 0)
        self.verticalLayout.addWidget(self.progressBar)

        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        font_label4 = QtGui.QFont(font_family, 11, QtGui.QFont.Bold)
        self.label_4.setFont(font_label4)
        self.label_4.setStyleSheet("color: #F0F0F0;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setText("")
        self.verticalLayout.addWidget(self.label_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "YouTube Video Downloader"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

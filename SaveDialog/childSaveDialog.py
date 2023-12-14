from PyQt5.QtWidgets import QDialog, QFileDialog
from SaveDialog.SaveDialog import Ui_Dialog


class SaveDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("保存结果")
        self.setFixedSize(520, 400)
        self.connect_signal()

    def connect_signal(self):
        self.saveDirButton.clicked.connect(self.onSaveDirButton)

    def onSaveDirButton(self):
        saveDir = QFileDialog.getExistingDirectory(self, "选择保存文件夹", "./")
        self.saveDirEdit.setText(saveDir)

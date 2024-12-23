import sys
import hashlib
from PyQt5 import QtWidgets
from index import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
import UpdateTxt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self) 
        UpdateTxt.update()

        self.ui.btnSelectFile.clicked.connect(self.select_file)
        self.ui.btnScan.clicked.connect(self.scan_for_malware)

    def select_file(self):
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Select File")
        if self.fileName:
            self.ui.label.setText(f"File Selected.")

    def calculate_hash(self):
        if self.fileName:
            md5_hash = hashlib.md5()
            try:
                with open(self.fileName, "rb") as f:
                    while chunk := f.read(8192):
                        md5_hash.update(chunk)

                self.hashValue = md5_hash.hexdigest()
                self.ui.label.setText(f"md5: {self.hashValue}")
                print(f"md5: {self.hashValue}")
                
            except Exception as e:
                self.ui.label.setText(f"Error: {str(e)}")

    def scan_for_malware(self):
        self.calculate_hash()
        if self.hashValue:
            with open("resources\\md5_hashes.txt", "r") as file:
                hashes = [line.strip().strip('"') for line in file.readlines()]

                if self.hashValue in hashes:
                    self.ui.label.setText("Malware detected!")
                else:
                    self.ui.label.setText("No malware found.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  
    mainWindow = MainWindow()  
    mainWindow.show() 
    sys.exit(app.exec_()) 

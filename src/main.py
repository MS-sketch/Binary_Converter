from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys
from ui import Ui_Dialog

class MainWindow:
    def __init__(self):
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)


        self.css()

        self.ui.pushButton.clicked.connect(self.main_function)
        self.ui.textEdit.textChanged.connect(self.clear_function)


    def clear_function(self):
        self.ui.textEdit_2.setText(str(""))

    def main_function(self):
        string = self.ui.textEdit.toPlainText()
        try:
            num = int(string)

            def DecimalToBinary(num):
                out = bin(num).replace("0b", "")
                out2 = "0" + str(out)
                self.ui.textEdit_2.setText(out2)


            DecimalToBinary(num)

        except:
            if len(string) >= 1:
                output = ''.join(format(ord(i), '08b') for i in string)

                self.ui.textEdit_2.setText(str(output))

            else:
                self.ui.textEdit_2.setText(str(""))

    def css(self):
        self.main_win.setWindowIcon(QIcon("code.svg"))
        self.main_win.setWindowTitle("Binary Converter")

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
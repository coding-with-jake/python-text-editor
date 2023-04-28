import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QToolBar, QStatusBar, QTextEdit, QVBoxLayout, \
    QWidget, QFileDialog, QDialogButtonBox, QDialog, QMessageBox


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shipping Label")

        main_layout = QVBoxLayout()

        self.button = QPushButton("Save!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.onMyToolBarButtonClick)
        self.text_area = QTextEdit()

        main_layout.addWidget(self.button)
        main_layout.addWidget(self.text_area)

        self.setMinimumSize(QSize(1200, 800))

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        toolbar = QToolBar("Tools")
        self.addToolBar(toolbar)

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        # file_menu.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        testing_text = self.text_area.toPlainText()
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText(testing_text)
        dlg.setStandardButtons(QMessageBox.StandardButton.Save)
        dlg.setIcon(QMessageBox.Icon.NoIcon)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.

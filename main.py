import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolBar, QAction, QStatusBar, QTextEdit, QVBoxLayout, QWidget

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shipping Label")

        main_layout = QVBoxLayout()

        button = QPushButton("Press Me!")
        text_area = QTextEdit()

        main_layout.addWidget(button)
        main_layout.addWidget(text_area)

        self.setMinimumSize(QSize(1200, 800))

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        toolbar = QToolBar("Tools")
        self.addToolBar(toolbar)

        button_action = QAction("Your Button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)

    def onMyToolBarButtonClick(selfself, s):
        print("click", s)

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

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class CustomListItem(QWidget):

    def __init__(self, text, importance=False, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        self.button_1 = QCheckBox(self)
        self.button_2 = QPushButton(text, self)

        # 按钮点击后触发的槽函数
        if importance:
            self.important_icon = QLabel(self)
            # 注意修改图片的大小
            self.important_icon.setFixedSize(30, 30)
            icon_pixmap = QPixmap("../icons/TargetArrow.png")
            scaled_pixmap = icon_pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.important_icon.setPixmap(scaled_pixmap)
        else:
            self.important_icon = QLabel(self)

        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        layout.addWidget(self.important_icon)
        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom QListWidget Item Example")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout(self)
        self.list_widget = QListWidget(self)
        layout.addWidget(self.list_widget)

        # 添加自定义项
        for i in range(5):
            custom_item = CustomListItem(f"Item {i}", True)
            # 用于设置槽函数
            custom_item.button_1.clicked.connect(lambda: self.delete_task())
            custom_item.button_2.clicked.connect(lambda: self.display_task())

            list_item = QListWidgetItem(self.list_widget)
            list_item.setSizeHint(custom_item.sizeHint())
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, custom_item)

        self.setLayout(layout)

    def delete_task(self):
        print("Delete task")

    def display_task(self):
        print("Display task")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

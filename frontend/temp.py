import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个Figure对象
        self.figure = plt.figure()

        # 创建一个FigureCanvas对象
        self.canvas = FigureCanvas(self.figure)

        # 创建一个布局，并将canvas添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        # 创建一个QWidget，并将布局设置为该QWidget的布局
        container = QWidget()
        container.setLayout(layout)

        # 将QWidget设置为主窗口的中心窗口
        self.setCentralWidget(container)

        # 绘制折线图
        self.plot()

    def plot(self):
        # 清除当前图形
        self.figure.clear()

        # 创建一个新的绘图对象
        ax = self.figure.add_subplot(111)

        # 数据
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]

        # 绘制折线图
        ax.plot(x, y, 'r-')

        # 设置标题和标签
        ax.set_title('简单折线图')
        ax.set_xlabel('X轴')
        ax.set_ylabel('Y轴')

        # 更新canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PlotWindow()
    main_window.show()
    sys.exit(app.exec_())

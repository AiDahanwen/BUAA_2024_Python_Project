import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QPropertyAnimation, QTimer, QEasingCurve

class AnimatedWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Animated Window')
        self.resize(400, 300)
        self.show()

        # 创建动画
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(2000)  # 动画持续时间2秒
        self.animation.setStartValue(0)  # 开始透明度为0
        self.animation.setEndValue(1)  # 结束透明度为1
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)  # 设置缓动曲线
        self.animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnimatedWindow()
    sys.exit(app.exec_())

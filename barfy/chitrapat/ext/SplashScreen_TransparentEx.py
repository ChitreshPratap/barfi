import sys
import time
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from barfy.chitrapat.SplashConfig import SplashConfig
from barfy.chitrapat.SplashScreen_Transparent import SplashScreen_Transparent

class SplashScreen_TransparentEx(SplashScreen_Transparent):

    def __init__(self,app=None,timeoutSeconds:int=10,
                 appIconPath:str="",
                 appIconSize:tuple=(150,150),
                 appTitle: str = "App Title",
                 appTitleFontSize: int = 36,
                 appTitleFontColor="#03468b",
                 appTagLine="App Tag Line",
                 appTagLineFontSize: int = 18,
                 appTagLineFontColor="#0570da",
                 progressBarColor="rgb(1,136,166)",
                 ):
        super(SplashScreen_TransparentEx, self).__init__()

        title=appTitle
        titleDesc=appTagLine
        appIconPath=appIconPath
        appTitleFontSize=str(appTitleFontSize)
        appTagLineFontSize=str(appTagLineFontSize)

        self.label_2.setText("""<html><head/><body><p align="center"><span style=" font-size:{appTitleFontSize}pt; font-weight:600; color:{appTitleFontColor};">{title}</span></p></body></html>""".format(title=title,appTitleFontSize=appTitleFontSize,appTitleFontColor=appTitleFontColor))
        self.label_2.setStyleSheet("background-color: transparent;")
        self.label_3.setText("""<html><head/><body><p align="center"><span style=" font-size:{appTagLineFontSize}pt; text-decoration: underline; color:{appTagLineFontColor};">{titleDesc}</span></p></body></html>""".format(titleDesc=titleDesc,appTagLineFontSize=appTagLineFontSize,appTagLineFontColor=appTagLineFontColor))
        self.label_3.setStyleSheet("background-color: transparent;")

        self.label.setPixmap(QtGui.QPixmap(appIconPath))
        self.label.setScaledContents(True)
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setMinimumSize(QtCore.QSize(appIconSize[0], appIconSize[1]))
        self.label.setMaximumSize(QtCore.QSize(appIconSize[0], appIconSize[1]))

        self._app=app
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        s = """
            QProgressBar {
                background-color: transparent;
                border-radius: 15px;
            }

            QProgressBar::chunk {
                background-color: """+progressBarColor+ """ ;                
                width: 20px;
            }
        """
        self.progressBar.setStyleSheet(s)
        self.progressBar.setMaximum(10)
        qr=self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.show()

        for i in range(1, 11):
            self.progressBar.setValue(i)
            t = time.time()
            while time.time() < t + 0.1:
                if self._app is not None:
                    self._app.processEvents()

        # Simulate something that takes time
        time.sleep(timeoutSeconds)

    def finish(self,mainWindow):
        super(SplashScreen_TransparentEx, self).finish(mainWindow)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    dlg=SplashScreen_TransparentEx(app,1)
    dlg.show()
    app.exec()



# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QSplashScreen
#
#
# class SplashScreen_Transparent(QSplashScreen):
#
#     def __init__(self):
#         super(SplashScreen_Transparent, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Dialog = self
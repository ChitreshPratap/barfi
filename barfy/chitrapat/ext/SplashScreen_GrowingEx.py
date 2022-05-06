import sys
import time
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from barfy.chitrapat.SplashScreen_Growing import SplashScreen_Growing

class SplashScreen_GrowingEx(SplashScreen_Growing):

    def __init__(self,app=None,timeoutSeconds:int=2,
                appIconPath = r"C:\Users\DELL\Desktop\calendarPng.png",
                appTitle:str="App Title",
                appTitleFontSize:int=58,
                appTitleFontColor = "#2914c6",
                appTagLine = "App Tag Line",
                appTagLineFontSize:int = 16,
                appTagLineFontColor = "#2111ff",
                initialWidth = 10,
                initialHeight = 10,
                finalWidth = 240
                ):
        super(SplashScreen_GrowingEx, self).__init__()
        appTitleFontSize=str(appTitleFontSize)
        appTagLineFontSize=str(appTagLineFontSize)

        appBackgroundPath="C:/Users/DELL/Downloads/bgImg.png"

        self._labelAppIcon = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._labelAppIcon.sizePolicy().hasHeightForWidth())
        self._labelAppIcon.setSizePolicy(sizePolicy)
        self._labelAppIcon.setMinimumSize(QtCore.QSize(40, 40))
        self._labelAppIcon.setAutoFillBackground(False)
        self._labelAppIcon.setText("")
        self._labelAppIcon.setScaledContents(True)
        self._labelAppIcon.setAlignment(QtCore.Qt.AlignCenter)
        self._labelAppIcon.setObjectName("_labelAppIcon")

        self._labelAppName.setText("<html><head/><body><p><span style=\" font-size:{appTitleFontSize}pt; font-weight:600; color:{appTitleFontColor};\">{appTitle}</span></p></body></html>".format(appTitleFontSize=appTitleFontSize,appTitleFontColor=appTitleFontColor,appTitle=appTitle))
        self._labelTagLine.setText( "<html><head/><body><p><span style=\" font-size:{appTagLineFontSize}pt; font-style:italic; color:{appTagLineFontColor};\">{appTagLine}</span></p></body></html>".format(appTagLineFontSize=appTagLineFontSize,appTagLineFontColor=appTagLineFontColor,appTagLine=appTagLine))

        finalHeight=int(finalWidth/int((initialWidth/initialHeight)))
        initialPositionX=int((self.geometry().width()/2)-(initialWidth/2))
        initialPositionY=int((self.geometry().height()/2)-(initialHeight/2))-60
        diffWidth=(finalWidth-initialWidth)/2
        diffHeight = (finalHeight - initialHeight) / 2

        # self.setStyleSheet("""background-color: transparent;""")
        # self.setStyleSheet("background-image: url('{appBackgroundPath}');".format(appBackgroundPath=appBackgroundPath))
        # self.label_2.setStyleSheet("background-image: url('{appBackgroundPath}');".format(appBackgroundPath=appBackgroundPath))
        # self.label_2.setStyleSheet("background-color: rgba(255, 255, 255);")
        # self.setStyleSheet("background-color: rgb(54, 43, 46);")

        self.label_2.setAttribute(Qt.WA_TranslucentBackground)
        self._labelAppIcon.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self._labelTagLine.setAttribute(Qt.WA_TranslucentBackground)


        self._app=app
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self._labelAppIcon.setMinimumSize(initialWidth,initialHeight)
        self._labelAppIcon.setPixmap(QtGui.QPixmap(appIconPath))
        self._labelAppIcon.setScaledContents(True)

        # self._labelAppIcon.setText("Yes")
        # self._labelAppIcon.setStyleSheet("background: red;")
        # geo=self._labelAppIcon.geometry()
        # print(geo)

        self.anim = QPropertyAnimation(self._labelAppIcon, b"geometry")
        # self.anim.setDuration(3000)
        animDuration=1000*timeoutSeconds
        self.anim.setDuration(animDuration)
        # self.anim.setStartValue(QRect(150, 30, 100, 100))
        self.anim.setStartValue(QRect(initialPositionX,initialPositionY, initialWidth, initialHeight))
        # self.anim.setEndValue(QRect(150, 30, 200, 200))
        self.anim.setEndValue(QRect(int(initialPositionX-diffWidth), int(initialPositionY-diffHeight), finalWidth, finalHeight))
        self.anim.start()

        qr=self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.show()

        # for i in range(1, 11):
        #     self.progressBar.setValue(i)
        #     t = time.time()
        #     while time.time() < t + 0.1:
        #         if self._app is not None:
        #             self._app.processEvents()

        # Simulate something that takes time
        time.sleep(timeoutSeconds)

    def finish(self,mainWindow):
        super(SplashScreen_GrowingEx, self).finish(mainWindow)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dlg=SplashScreen_GrowingEx(app,2)
    dlg.show()
    app.exec()

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QSplashScreen
# class SplashScreen_Growing(QSplashScreen):
#     def __init__(self):
#         super(SplashScreen_Growing, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Dialog = self
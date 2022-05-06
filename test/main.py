import sys
from PyQt5.QtWidgets import QApplication
from barfy.chitrapat.ext.SplashScreen_DarkEx import SplashScreen_DarkEx
from barfy.chitrapat.ext.SplashScreen_GrowingEx import SplashScreen_GrowingEx
from barfy.chitrapat.ext.SplashScreen_TransparentEx import SplashScreen_TransparentEx

def splashScreenDarkDemoEx():
    app = QApplication(sys.argv)
    splash = SplashScreen_DarkEx(app,5,appIconPath = r"C:\Users\DELL\Desktop\calendarPng.png")
    splash.show()
    app.exec()

def splashScreenGrowingEx():
    app = QApplication(sys.argv)
    splash = SplashScreen_GrowingEx(app,3,appIconPath = r"C:\Users\DELL\Desktop\calendarPng.png")
    splash.show()
    app.exec()

def splashScreenTransparentEx():
    app = QApplication(sys.argv)
    splash = SplashScreen_TransparentEx(app,3,appIconPath = r"C:\Users\DELL\Desktop\calendarPng.png")
    splash.show()
    app.exec()


if __name__ == '__main__':
    # splashScreenDarkDemoEx()
    # splashScreenTransparentEx()
    splashScreenGrowingEx()

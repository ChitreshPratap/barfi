import sys
from PyQt5.QtWidgets import QApplication
from barfi.chitrapat.SplashConfig import SplashConfig
from barfi.chitrapat.SplashScreen_Dark import SplashScreen_Dark
from barfi.chitrapat.SplashScreen_Transparent import SplashScreen_Transparent
from barfi.chitrapat.ext.SplashScreen_DarkEx import SplashScreen_DarkEx
from barfi.chitrapat.ext.SplashScreen_TransparentEx import SplashScreen_TransparentEx

def splashScreenDarkDemo():
    app = QApplication(sys.argv)
    dlg = SplashScreen_Dark()
    dlg.show()
    app.exec()

def splashScreenDarkDemoEx():
    app = QApplication(sys.argv)
    splashConfig=SplashConfig().setAppTitle("TechNicalSaaNd").setAppTagLine("Building Skills").setIcon(r"C:\Users\DELL\Downloads\flutter_projects\PDFSecure\pdf_secure\assets\images\_AboutAppImage.png")
    dlg = SplashScreen_DarkEx(app,splashConfig=splashConfig)
    dlg.show()
    app.exec()

def splashScreenTransparent():
    app = QApplication(sys.argv)
    dlg = SplashScreen_Transparent()
    dlg.show()
    app.exec()

def splashScreenTransparentEx():
    app = QApplication(sys.argv)
    splashConfig = SplashConfig().setAppTitle("TechNicalSaaNd").setAppTagLine("Building Skills").setIcon(r"C:\Users\DELL\Downloads\flutter_projects\PDFSecure\pdf_secure\assets\images\_AboutAppImage.png")
    dlg = SplashScreen_TransparentEx(app,splashConfig=splashConfig)
    dlg.show()
    app.exec()


if __name__ == '__main__':
    # splashScreenDarkDemoEx()
    splashScreenTransparentEx()

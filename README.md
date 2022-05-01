# barfy

This is python package is used to for different sweet splash screens. 
This package uses <b>PyQt5</b> and is application only for the applications,
which are build using <b>PyQt5</b>

<br><b>This package splash screen is only for pyqt5 projects.</b>

<hr>
<h4>Installing</h4>
<code>pip install barfy</code>



#### Available Splash Screen Class
    - SplashScreen_TransparentEx
    - SplashScreen_DarkEx

<hr>

#### Examples
<code>

Example 1

    import sys
    from PyQt5.QtWidgets import QApplication
    from barfy.chitrapat.SplashConfig import SplashConfig
    from barfy.chitrapat.ext.SplashScreen_DarkEx import SplashScreen_DarkEx

    def splashScreenDarkDemoEx():
        app = QApplication(sys.argv)
        splashConfig=SplashConfig().setAppTitle("AppTitle").setAppTagLine("App Tag Line").setIcon("path/to/app/icon/file.png")\
            .setProgressBarColor("yellow")\
            .setAppTitleFontColor("yellow")\
            .setAppTagLineFontColor("lime")\
            .setAppIconSize(300,100)\
            .setAppBackgroundColor("brown")
        splash = SplashScreen_DarkEx(app,splashConfig=splashConfig)
        window=YourWindowOfPyQT5()
        window.show()
        splash.finish(window)
        app.exec()

Example 2:

    import sys
    from PyQt5.QtWidgets import QApplication
    from barfy.chitrapat.SplashConfig import SplashConfig
    from barfy.chitrapat.ext.SplashScreen_TransparentEx import SplashScreen_TransparentEx

    def splashScreenTransparentEx():
        app = QApplication(sys.argv)
        splashConfig = SplashConfig().setAppTitle("App Title")\
            .setAppTagLine("App Tag Line")\
            .setIcon(r"path/to/app/icon/file.png")\
            .setProgressBarColor("brown")\
            .setAppTitleFontColor("brown")\
            .setAppTagLineFontColor("brown")\
            .setAppIconSize(400,200)
        splash = SplashScreen_TransparentEx(app,splashConfig=splashConfig)
        window=YourWindowOfPyQT5()
        window.show()
        splash.finish(window)
        app.exec()



Example 3

    import sys
    from PyQt5.QtWidgets import QApplication
    from barfy.chitrapat.SplashConfig import SplashConfig
    from barfy.chitrapat.ext.SplashScreen_TransparentEx import SplashScreen_TransparentEx

    def example1():
        app = QApplication(sys.argv)
        splashConfig = SplashConfig().setAppTitle("App Title").setAppTagLine("App Tag Line").setIcon(r"path/to/app/icon/file.png")
        splash = SplashScreen_TransparentEx(app,5,splashConfig=splashConfig)
        window=YourWindowOfPyQT5()
        window.show()
        splash.finish(window)

</code>




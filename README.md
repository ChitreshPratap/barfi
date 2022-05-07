# barfy
## version 1.0.0

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
    - SplashScreen_GrowingEx
    - SplashScreen_LoadEx

<hr>

#### Examples
<code>

Example 1

    import sys
    from PyQt5.QtWidgets import QApplication
    from barfy.chitrapat.ext.SplashScreen_DarkEx import SplashScreen_DarkEx
    from test.TestingWindow import TestingWindow

    def splashScreenDarkDemoEx():
        app = QApplication(sys.argv)
        splash = SplashScreen_DarkEx(app,5,appIconPath = r"path/to/app/icon.png")
        testWindow=TestingWindow()
        testWindow.show()
        splash.finish(testWindow)
        app.exec()

Example 2:

    import sys
    from PyQt5.QtWidgets import QApplication
    from barfy.chitrapat.ext.SplashScreen_TransparentEx import SplashScreen_TransparentEx
    from test.TestingWindow import TestingWindow

    def splashScreenTransparentEx():
        app = QApplication(sys.argv)
        splash = SplashScreen_TransparentEx(app,7,appIconPath = r"path/to/app/icon.png")
        testWindow=TestingWindow()
        testWindow.show()
        splash.finish(testWindow)
        app.exec()

Example 3

    import sys
    from PyQt5.QtWidgets import QApplication
    from barfy.chitrapat.ext.SplashScreen_GrowingEx import SplashScreen_GrowingEx
    from test.TestingWindow import TestingWindow

    def splashScreenGrowingEx():
        app = QApplication(sys.argv)
        splash = SplashScreen_GrowingEx(app,5,appIconPath = r"path/to/app/icon.png",appTitle="Ffilfo")
        testWindow=TestingWindow()
        testWindow.show()
        splash.finish(testWindow)
        app.exec()

Example 4:

    import sys
    from PyQt5.QtWidgets import QApplication
    from barfy.chitrapat.ext.SplashScreen_LoadEx import SplashScreen_LoadEx
    from test.TestingWindow import TestingWindow

    def splashScreenLoadEx():
        app = QApplication(sys.argv)
        splash = SplashScreen_LoadEx(app,5,appIconPath = r"path/to/app/icon.png",appTitle="Ffilfo",loaderGifPath=r"path/to/loader.gif")
        testWindow=TestingWindow()
        testWindow.show()
        splash.finish(testWindow)
        app.exec()

</code>


<ul><h4>Old Versions<h4>
    <li><a href="https://github.com/ChitreshPratap/barfy/blob/main/README_V1.0.0.md">barfy v0.0.1</a></li>
</ul>


# barfi
<hr>
This is python package is used to for different sweet splash screens. 
This package uses <b>PyQt5</b> and is application only for the applications,
which are build using <b>PyQt5</b>
<hr>
<h4>Installing</h4>
<code>pip install barfi</code>


#### Available Splash Screen Class
    - SplashScreen_TransparentEx
    - SplashScreen_DarkEx

<hr>

####Examples
<code>
Example1
    
    import sys
    from PyQt5.QtWidgets import QApplication
    from barfi.chitrapat.SplashConfig import SplashConfig
    from barfi.chitrapat.SplashScreen_Transparent import SplashScreen_Transparent
    def example1():
        app = QApplication(sys.argv)
        splashConfig = SplashConfig().setAppTitle("TechNicalSaaNd").setAppTagLine("Building Skills").setIcon(r"C:\Users\DELL\Downloads\flutter_projects\PDFSecure\pdf_secure\assets\images\_AboutAppImage.png")
        splash = SplashScreen_TransparentEx(app,5,splashConfig=splashConfig)
        window=YourWindowOfPyQT5()
        window.show()
        splash.finish(window)

Example2:

    import sys
    from PyQt5.QtWidgets import QApplication
    from barfi.chitrapat.SplashConfig import SplashConfig
    from barfi.chitrapat.SplashScreen_Dark import SplashScreen_Dark
    def example1():
        app = QApplication(sys.argv)
        splashConfig = SplashConfig().setAppTitle("TechNicalSaaNd").setAppTagLine("Building Skills").setIcon(r"C:\Users\DELL\Downloads\flutter_projects\PDFSecure\pdf_secure\assets\images\_AboutAppImage.png") 
        splash = SplashScreen_TransparentEx(app,5,splashConfig=splashConfig)
        window=YourWindowOfPyQT5()
        window.show()
        splash.finish(window)
</code>




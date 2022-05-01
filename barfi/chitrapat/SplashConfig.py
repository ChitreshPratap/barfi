
class SplashConfig:

    def __init__(self):
        self._appTitle=""
        self._appIcon=""
        self._appTagLine=""
        self._companyName=""
        self._companyIcon=""

    def setAppTitle(self,appTitle:str="App Title"):
        self._appTitle=appTitle
        return self

    def setIcon(self,iconPath):
        self._appIcon=iconPath
        return self

    def setAppTagLine(self,tagLine):
        self._appTagLine=tagLine
        return self

    def setCompanyName(self,companyName:str="Company Name"):
        self._companyName=companyName
        return self

    def setCompanyIcon(self,companyIcon:str):
        self._companyIcon=companyIcon
        return self

    def getAppTitle(self)->str:
        appTitle=self._appTitle
        return appTitle

    def getAppTagLine(self)->str:
        tagLine=self._appTagLine
        return tagLine

    def getAppIcon(self)->str:
        iconPath=self._appIcon
        return iconPath

    def getCompanyName(self)->str:
        name=self._companyName
        return name

    def getCompanyIcon(self)->str:
        iconPath=self._companyIcon
        return iconPath
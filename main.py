# 12 Februari 2023 by Mhd Afizha Aw
# Created by: PyQt5 UI code generator 5.15.1
Author = "Crafted by seimpairiyun"

# MODULES
from pkg_resources import require
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from pyproc import Lpse
from selenium import webdriver
import urllib3
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import SessionNotCreatedException
from requests.exceptions import ReadTimeout as TIMEOUT_3, ConnectionError as TIMEOUT_4
from urllib3.exceptions import ReadTimeoutError as TIMEOUT_2, NewConnectionError as TIMEOUT_6, MaxRetryError as TIMEOUT_7
from socket import timeout as TIMEOUT_1, gaierror as TIMEOUT_5

def lpseTarget(url):
    link = Lpse(f'{url}', timeout=30)
    token = link.session.cookies['SPSE_SESSION'].split('___')[1].split('=')[1].strip('&')
    return f'{url}/eproc4/dt/lelang?authenticityToken={token}'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Layout
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Label --------------------------------------------------------------------------------------------
        #Tahun
        self.label_Tahun = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Tahun.sizePolicy().hasHeightForWidth())
        self.label_Tahun.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Tahun.setFont(font)
        self.label_Tahun.setObjectName("label_Tahun")
        self.gridLayout.addWidget(self.label_Tahun, 0, 0, 1, 1)

        #URL
        self.label_URL = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_URL.sizePolicy().hasHeightForWidth())
        self.label_URL.setSizePolicy(sizePolicy)
        self.label_URL.setFont(font)
        self.label_URL.setStyleSheet("")
        self.label_URL.setObjectName("label_URL")
        self.gridLayout.addWidget(self.label_URL, 1, 0, 1, 1)

        #Label Engine
        self.label_Engine = QtWidgets.QLabel(self.centralwidget)
        self.label_Engine.setFont(font)
        self.label_Engine.setObjectName("label_Engine")
        self.gridLayout.addWidget(self.label_Engine, 3, 0, 1, 1)

        #Programmer
        self.label_Author = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Author.sizePolicy().hasHeightForWidth())
        self.label_Author.setSizePolicy(sizePolicy)
        self.label_Author.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Author.setObjectName("label_Author")
        self.label_Author.setToolTip("https://github.com/seimpairiyun")
        self.gridLayout.addWidget(self.label_Author, 5, 3, 1, 1) 
        
        # -------------------------------------------------------------------------------------------- Label

        #Input Tahun
        self.Tahun = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tahun.sizePolicy().hasHeightForWidth())
        self.Tahun.setSizePolicy(sizePolicy)
        self.Tahun.setMinimumSize(QtCore.QSize(0, 0))
        self.Tahun.setObjectName("Tahun")
        self.Tahun.setFocus()
        self.gridLayout.addWidget(self.Tahun, 0, 1, 1, 2)

        tahunNow = int(self.getTime().year) + 1

        for th in reversed(range(tahunNow)):
            if th >= 2012: #Data LPSE mulai tahun 2012
                self.Tahun.addItem(str(th))

        #Input URL
        self.URL = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.URL.sizePolicy().hasHeightForWidth())
        self.URL.setSizePolicy(sizePolicy)
        self.URL.setClearButtonEnabled(True)
        self.URL.setObjectName("URL")
        self.gridLayout.addWidget(self.URL, 1, 1, 1, 2)

        #Button Download
        self.btn_Download = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.btn_Download.sizePolicy().hasHeightForWidth())
        self.btn_Download.setSizePolicy(sizePolicy)
        self.btn_Download.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_Download.setStyleSheet("")
        self.btn_Download.setObjectName("btn_Download")
        self.gridLayout.addWidget(self.btn_Download, 0, 3, 2, 1)
           
        #Button Batch Download
        self.btn_Batch = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Batch.sizePolicy().hasHeightForWidth())
        self.btn_Batch.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_Batch.setFont(font)
        self.btn_Batch.setObjectName("btn_Batch")
        self.gridLayout.addWidget(self.btn_Batch, 5, 0, 1, 1)        

        #Engine 1
        self.engine_PyProc = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engine_PyProc.sizePolicy().hasHeightForWidth())
        self.engine_PyProc.setSizePolicy(sizePolicy)
        self.engine_PyProc.setObjectName("engine_PyProc")
        self.engine_PyProc.setToolTip('https://github.com/wakataw/pyproc')
        self.gridLayout.addWidget(self.engine_PyProc, 3, 1, 1, 1)

        #Engine 2
        self.engine_Selenium = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engine_Selenium.sizePolicy().hasHeightForWidth())
        self.engine_Selenium.setSizePolicy(sizePolicy)
        self.engine_Selenium.setObjectName("engine_Selenium")
        self.engine_Selenium.setToolTip('Lambat namun pasti')
        self.gridLayout.addWidget(self.engine_Selenium, 3, 2, 1, 1)

        #Log Process
        self.text_Log = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_Log.sizePolicy().hasHeightForWidth())
        self.text_Log.setSizePolicy(sizePolicy)
        self.text_Log.setObjectName("text_Log")
        self.gridLayout.addWidget(self.text_Log, 4, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Controller -----------------------------------------------------------------------------------------------------------
        #test selenium
        #browser = self.seleniumConfig()

        #browser.get('https://github.com/seimpairiyun')
        #browser.capabilities['browserVersion']


        #auto run after enter clicked while input URL
        self.URL.returnPressed.connect(self.btnDownload)

        #self.engine_PyProc.stateChanged.connect(lambda:self.engineSetup(self.engine_PyProc))
        #self.engine_Selenium.toggled.connect(lambda:self.engineSetup(self.engine_Selenium))
        self.engine_PyProc.stateChanged.connect(self.engineSetup)
        self.engine_Selenium.toggled.connect(self.engineSetup)

        self.btn_Download.clicked.connect(self.btnDownload)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LPSE 2E"))
        self.label_Tahun.setText(_translate("MainWindow", "Tahun"))
        self.label_URL.setText(_translate("MainWindow", "URL"))
        self.label_Engine.setText(_translate("MainWindow", "Engine  "))
        self.label_Author.setText(_translate("MainWindow", Author))
        self.URL.setPlaceholderText(_translate("MainWindow", "https://lpse.bireuenkab.go.id"))
        self.btn_Download.setText(_translate("MainWindow", "Download"))
        self.btn_Batch.setText(_translate("MainWindow", "Batch"))
        self.engine_PyProc.setText(_translate("MainWindow", "PyProc"))
        self.engine_Selenium.setText(_translate("MainWindow", "Scrapping"))

    # UTILITY
    def getTime(self):
        return datetime.now()

    def btnDownload(self):
        self.text_Log.setText(str(self.Tahun.currentText()))
        self.text_Log.append(str(self.URL.text()))
        self.text_Log.append(self.engineSetup())
        self.text_Log.append(self.seleniumConfig().capabilities['browserVersion'])
        #self.seleniumConfig().close()
        #self.seleniumConfig().quit()

        if self.URL.text() == '':
            self.URL.setFocus()
        elif self.engineSetup() == '':
            self.text_Log.setText('Silahkan pilih salah satu engine')

    def engineSetup(self):  
        if self.engine_PyProc.isChecked():
            self.engine_Selenium.setDisabled(True)
            engine = 'Pyproc'
        elif self.engine_Selenium.isChecked():
            self.engine_PyProc.setDisabled(True)
            engine = 'Scrapping'
        else:
            self.engine_PyProc.setDisabled(False)
            self.engine_Selenium.setDisabled(False)
            engine = ''

        return engine
        #print(f'{i.text()}: {i.isChecked()}')

    def seleniumConfig(self):
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_argument("--window-size=800x600")
        options.add_argument("--log-level=0")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--blink-settings=imagesEnabled=false")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)
            
        return driver

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# 12 Februari 2023 by Mhd Afizha Aw
# Created by: PyQt5 UI code generator 5.15.1

# ABOUT
Author = "Crafted by <b>Mhd Afizha Aw</b>"
Logo = "log.opng"
Version = "0.1.3"

# MODULES
from datetime import datetime as time
from sys import argv as sysARGV, exit as sysEXIT
from pandas import DataFrame, ExcelWriter
from requests import exceptions as exc_Req
from urllib3 import disable_warnings, exceptions as exc_URL

from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication, QSize, QEventLoop, QTimer
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QGridLayout,
    QSizePolicy,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QTextBrowser,
    QCheckBox,
    QProgressDialog,
    QMessageBox,
)

from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver, __version__ as seleniumVersion
from pyproc import Lpse, __version__ as pyprocVersion
from pyproc.utils import json
from pyproc.utils import re

#!URLLIB3 DISABLE WARNING
disable_warnings(
    category=(
        exc_URL.InsecureRequestWarning,
        exc_URL.NewConnectionError,
        exc_URL.MaxRetryError,
        exc_URL.HTTPError,
        exc_URL.HTTPWarning,
        exc_Req.ConnectionError,
        exc_Req.RetryError,
        exc_Req.HTTPError,
        exc_Req.ConnectTimeout,
    )
)


# LAYOUT
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # UI
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 600)
        MainWindow

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Label Tahun
        self.label_Tahun = QLabel(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Tahun.sizePolicy().hasHeightForWidth())
        self.label_Tahun.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Tahun.setFont(font)
        self.label_Tahun.setObjectName("label_Tahun")
        self.gridLayout.addWidget(self.label_Tahun, 0, 0, 1, 1)

        # Label URL
        self.label_URL = QLabel(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_URL.sizePolicy().hasHeightForWidth())
        self.label_URL.setSizePolicy(sizePolicy)
        self.label_URL.setFont(font)
        self.label_URL.setStyleSheet("")
        self.label_URL.setObjectName("label_URL")
        self.gridLayout.addWidget(self.label_URL, 1, 0, 1, 1)

        # Label Engine
        self.label_Engine = QLabel(self.centralwidget)
        self.label_Engine.setFont(font)
        self.label_Engine.setObjectName("label_Engine")
        self.gridLayout.addWidget(self.label_Engine, 3, 0, 1, 1)

        # Label Programmer
        self.label_Author = QLabel(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Author.sizePolicy().hasHeightForWidth())
        self.label_Author.setSizePolicy(sizePolicy)
        self.label_Author.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_Author.setObjectName("label_Author")
        # self.label_Author.setToolTip("https://github.com/seimpairiyun")
        self.gridLayout.addWidget(self.label_Author, 5, 3, 1, 1)

        # -------------------------------------------------------------------------------------------- LABEL

        # Input Tahun
        self.Tahun = QComboBox(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tahun.sizePolicy().hasHeightForWidth())
        self.Tahun.setSizePolicy(sizePolicy)
        self.Tahun.setMinimumSize(QSize(0, 0))
        self.Tahun.setObjectName("Tahun")
        self.Tahun.setFocus()
        self.gridLayout.addWidget(self.Tahun, 0, 1, 1, 2)

        # Generate Tahun
        tahunNow = int(self.getTime().year) + 1
        for th in reversed(range(tahunNow)):
            if th >= 2012:  # Data LPSE mulai tahun 2012
                self.Tahun.addItem(str(th))

        # Input URL
        self.URL = QLineEdit(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.URL.sizePolicy().hasHeightForWidth())
        self.URL.setSizePolicy(sizePolicy)
        self.URL.setClearButtonEnabled(True)
        self.URL.setObjectName("URL")
        self.gridLayout.addWidget(self.URL, 1, 1, 1, 2)

        # Button CSS
        btnCSS = """
        QPushButton::hover{
            background-color: rgb(88, 103, 221);
            border-radius:2px;
            color:white;
            font:bold;
        }

        QPushButton::pressed{
            background-color: rgb(65, 82, 216);
            border-radius:2px;
            color:white;
            font:bold;
        }
        """

        # Button Download
        self.btn_Download = QPushButton(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.btn_Download.sizePolicy().hasHeightForWidth())
        self.btn_Download.setSizePolicy(sizePolicy)
        self.btn_Download.setLayoutDirection(Qt.RightToLeft)
        self.btn_Download.setObjectName("btn_Download")
        self.btn_Download.setStyleSheet(btnCSS)
        self.gridLayout.addWidget(self.btn_Download, 0, 3, 2, 1)

        # Button Batch Download
        self.btn_Batch = QPushButton(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Batch.sizePolicy().hasHeightForWidth())
        self.btn_Batch.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_Batch.setFont(font)
        self.btn_Batch.setObjectName("btn_Batch")
        self.btn_Batch.setStyleSheet(btnCSS)
        self.gridLayout.addWidget(self.btn_Batch, 5, 0, 1, 1)

        # Engine 1
        self.engine_PyProc = QCheckBox(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.engine_PyProc.sizePolicy().hasHeightForWidth()
        )
        self.engine_PyProc.setSizePolicy(sizePolicy)
        self.engine_PyProc.setObjectName("engine_PyProc")
        self.engine_PyProc.setToolTip("https://github.com/wakataw/pyproc")
        self.gridLayout.addWidget(self.engine_PyProc, 3, 1, 1, 1)

        # Engine 2
        self.engine_Selenium = QCheckBox(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.engine_Selenium.sizePolicy().hasHeightForWidth()
        )
        self.engine_Selenium.setSizePolicy(sizePolicy)
        self.engine_Selenium.setObjectName("engine_Selenium")
        self.engine_Selenium.setToolTip(
            "Lambat tapi pasti, namun tidak ada yg pasti di dunia ini"
        )
        self.gridLayout.addWidget(self.engine_Selenium, 3, 2, 1, 1)

        # font Bahnschrift Condensed
        LogCSS = (
            """
            QTextBrowser{
                background-color: white;
                background-image: url('data/"""
            + Logo
            + """');
                background-repeat: no-repeat;
                background-position: center;
            }
            """
        )

        # Log Process
        self.text_Log = QTextBrowser(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_Log.sizePolicy().hasHeightForWidth())
        self.text_Log.setSizePolicy(sizePolicy)
        self.text_Log.setObjectName("text_Log")
        self.text_Log.setStyleSheet(LogCSS)

        # END
        self.gridLayout.addWidget(self.text_Log, 4, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # Controller -----------------------------------------------------------------------------------------------------------
        # test selenium
        # browser = self.seleniumConfig()

        # browser.get('https://github.com/seimpairiyun')
        # browser.capabilities['browserVersion']

        # auto run after enter clicked while input URL
        ##self.URL.returnPressed.connect(self.btnDownload)

        # self.engine_PyProc.stateChanged.connect(lambda:self.engineSetup(self.engine_PyProc))
        # self.engine_Selenium.toggled.connect(lambda:self.engineSetup(self.engine_Selenium))

        self.engine_PyProc.stateChanged.connect(self.engineSetup)
        self.engine_Selenium.toggled.connect(self.engineSetup)
        self.btn_Download.clicked.connect(self.btnDownload)
        self.btn_Batch.clicked.connect(self.yearQuestion)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LPSE 2E"))
        MainWindow.setWindowIcon(QIcon(f"data\\{Logo}"))
        self.label_Tahun.setText(_translate("MainWindow", "Tahun"))
        self.label_URL.setText(_translate("MainWindow", "URL"))
        self.label_Engine.setText(_translate("MainWindow", "Engine  "))
        self.label_Author.setText(_translate("MainWindow", Author))
        self.URL.setPlaceholderText(
            _translate("MainWindow", "https://lpse.bireuenkab.go.id")
        )
        self.btn_Download.setText(_translate("MainWindow", "Download"))
        self.btn_Batch.setText(_translate("MainWindow", "Batch"))
        self.engine_PyProc.setText(_translate("MainWindow", "PyProc"))
        self.engine_Selenium.setText(_translate("MainWindow", "Scrapping"))

        # Home
        self.text_Log.setText(f"<b>LPSE 2E v{Version}</b>")
        self.text_Log.append(
            "Engine:"
            + f"\n- Pyproc v{pyprocVersion}"
            + f"\n- Selenium v{seleniumVersion} "
        )
        self.text_Log.append(
            "<br><b>Catatan:</b>"
            + "<br>- Pilih scrapping jika data LPSE tidak bisa diambil menggunakan PyProc"
            + "<br>- Pastikan google chrome sudah versi terbaru apabila menggunakan Scrapping"
            + "<br>- Lapor bug atau bantu ngembangin aplikasi https://github.com/seimpairiyun/LPSE-2E"
        )


# MAIN APP
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # CONTROLLERS
        self.URL.returnPressed.connect(self.btnDownload)

    def closeEvent(self, event):
        event.accept()
        print("Close")

    def getTime(self):
        return time.now()

    def validJSON(data):
        return json.loads(json.dumps(data))

    def durasi(self, app_start):
        app_stop = time.now()
        selisih = app_stop - app_start
        getDurasi = divmod(selisih.seconds, 60)
        durasi = f"Done. {getDurasi[0]} menit {getDurasi[1]} detik"
        return durasi

    def yearQuestion(self):
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon(f"data\\{Logo}"))
        self.msg.setWindowTitle("Info")
        self.msg.setText(f"Download sampai dengan tahun {self.getTime().year}?")
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msg.exec()

        if self.msg == QMessageBox.Yes:
            self.text_Log.setText("Yes")
        else:
            self.text_Log.setText("No")

    def timer(self, n=100):
        loop = QEventLoop()
        QTimer.singleShot(n, loop.quit)
        loop.exec_()

    def loadBar(self, value):
        app_start = time.now()

        self.loading = QProgressDialog("Loading..", None, 0, value)
        self.loading.setWindowModality(Qt.ApplicationModal)  # Deactive MainWindow
        self.loading.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.loading.setAutoClose(True)

        for i in range(value + 1):
            self.loading.setValue(i)
            self.timer(500)
            if self.loading.wasCanceled():
                break

        self.text_Log.append(self.durasi(app_start))
        self.timer(1000)

    def btnDownload(self):

        # self.text_Log.setText(str(self.Tahun.currentText()))
        # self.text_Log.append(str(self.URL.text()))
        # self.text_Log.append(self.engineSetup())
        # self.text_Log.append(self.seleniumConfig().capabilities['browserVersion'])
        # self.seleniumConfig().close()
        # self.seleniumConfig().quit()

        # Engine
        url = self.URL.text()
        engine = self.engineSetup()
        tahun = str(self.Tahun.currentText())

        # URL Validation
        regex = r"https?://lpse\..+\.(?:go|ac)\.id"
        isLPSE = re.findall(regex, self.URL.text())

        if url == "":
            self.URL.setFocus()
        elif isLPSE == []:
            self.text_Log.setText("URL tidak benar")
        elif engine == "":
            self.text_Log.setText("Silahkan pilih salah satu engine")
        else:
            self.text_Log.clear()
            self.text_Log.setText(f"Engine: {engine}")
            self.timer(500)
            self.text_Log.append(f"Trying to access {url}")
            self.timer(500)
            self.text_Log.append(f"Trying to download data LPSE {tahun}\n")
            self.timer(500)
            self.loadBar(20)

    def engineSetup(self):
        if self.engine_PyProc.isChecked():
            self.engine_Selenium.setDisabled(True)
            engine = "Pyproc"
        elif self.engine_Selenium.isChecked():
            self.engine_PyProc.setDisabled(True)
            engine = "Scrapping"
        else:
            self.engine_PyProc.setDisabled(False)
            self.engine_Selenium.setDisabled(False)
            engine = ""

        # print(f'{i.text()}: {i.isChecked()}')
        return engine

    # ENGINE PYPROC
    def openLPSE(self, url):
        # Pyproc Settings
        return Lpse(f"{url}", timeout=60)

    def getData(self, url, id_paket):
        # GET DETAIL TENDER
        lpse = self.openLPSE(url)

        detil = lpse.detil_paket_tender(id_paket)
        detil.get_all_detil()

        # Manual gettting detil data and cleansing into valid Dict(JSON)
        """ 
        removeQuote = str(detil).replace("'", '"')
        removeBoolNone = r'True|False|None'
        detilPaket = re.sub(removeBoolNone, '""', removeQuote)
        dataDetilPaket = json.loads(detilPaket) 
        """

        id = detil.id_paket
        link = f"{url}/eproc4/lelang/{id}/pengumumanlelang"
        # rup = detil.pengumuman['rencana_umum_pengadaan'][0]['kode_rup']

        try:
            winner = detil.pemenang[0]
        except Exception as e:
            winner = ""

        try:
            lokasi = detil.pengumuman["lokasi_pekerjaan"][0]
        except Exception as e:
            lokasi = ""

        try:
            # Set into Dict(JSON)
            dataSet = dict(link_lpse=link)
            dataSet.update(detil.pengumuman)
            dataSet["lokasi_pekerjaan"] = lokasi
            dataSet.update(winner)

            # handler error when try to remove this column
            dataSet["alasan_pembatalan"] = ""
            dataSet["alasan_di_ulang"] = ""

            return dataSet

        except TypeError as e:
            self.text_Log.setText(e)
            print(e)
            return dict(link_lpse="download failed")
        except Exception as e:
            self.text_Log.setText(e)
            print(e)

    # ENGINE SELENIUM
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

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )

        return driver


if __name__ == "__main__":
    app = QApplication(sysARGV)
    main = MainWindow()
    main.show()

    sysEXIT(app.exec_())

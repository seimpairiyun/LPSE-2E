from selenium import webdriver, __version__ as seleniumVersion
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time


def seleniumConfig():
    options = Options()
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
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

def waitElement(driver, name):
    WebDriverWait(driver, 60).until(
        condition.presence_of_element_located((By.CLASS_NAME, name))
    )

web = seleniumConfig()

web.get("https://lpse.bandaacehkota.go.id/eproc4/lelang")

# Filter Tahun
web.find_element(By.XPATH, '//select[@name="tahun"]/option[text()="2022"]').click()

# Show All
web.find_element(
    By.XPATH, '//select[@name="tbllelang_length"]/option[text()="Semua"]'
).click()

# Get Kode Tender
waitElement(web, 'sorting_1')
id = web.find_elements(By.CLASS_NAME, "sorting_1")

idTender = []
for i in id:
    idTender.append(i.text)

print(idTender)

time.sleep(2)
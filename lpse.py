from sys import stdout
from pprint import pprint
from pyproc import Lpse, exceptions as exc_LPSE
from pyproc.utils import json, re
from datetime import datetime as time
from pandas import DataFrame, ExcelWriter
from requests import exceptions as exc_Req
from urllib3 import disable_warnings, exceptions as exc_URL

# ------------------------------------------------------------

#!URLLIB3 DISABLE WARNING
disable_warnings(category=(
    exc_URL.InsecureRequestWarning,
    exc_URL.NewConnectionError,
    exc_URL.MaxRetryError,
    exc_URL.HTTPError,
    exc_URL.HTTPWarning,
    exc_Req.ConnectionError,
    exc_Req.RetryError,
    exc_Req.HTTPError,
    exc_Req.ConnectTimeout,
))


def clear_line():
    stdout.write("\033[F")  # back to previous line
    stdout.write("\033[K")  # clear line


def durasi(app_start):
    app_stop = time.now()
    selisih = app_stop - app_start
    getDurasi = divmod(selisih.seconds, 60)
    durasi = f'Done. {getDurasi[0]} menit {getDurasi[1]} detik'
    return durasi


def validJSON(data):
    return json.loads(json.dumps(data))


def openLPSE(url):
    # Pyproc Settings
    return Lpse(f'{url}', timeout=60)


def getData(url, id_paket):
    # GET DETAIL TENDER
    lpse = openLPSE(url)

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
    link = f'{url}/eproc4/lelang/{id}/pengumumanlelang'
    # rup = detil.pengumuman['rencana_umum_pengadaan'][0]['kode_rup']

    try:
        winner = detil.pemenang[0]
    except Exception as e:
        winner = ''

    try:
        lokasi = detil.pengumuman['lokasi_pekerjaan'][0]
    except Exception as e:
        lokasi = ''

    try:
        # Set into Dict(JSON)
        dataSet = dict(link_lpse=link)
        dataSet.update(detil.pengumuman)
        dataSet['lokasi_pekerjaan'] = lokasi
        dataSet.update(winner)

        # handler error when try to remove this column
        dataSet['alasan_pembatalan'] = ''
        dataSet['alasan_di_ulang'] = ''

        return dataSet

    except TypeError as e:
        print(e)
        return dict(link_lpse='download failed')
    except Exception as e:
        print(e)


def saveDataLPSE(url, tahun=None, length=9999):
    try:
        lpse = openLPSE(url)

        # GET TENDER
        tender = lpse.get_paket_tender(tahun=tahun, length=length)
        getTender = validJSON(tender)

        total = getTender['recordsTotal']
        data = getTender['data']

        if data != []:
            # RUN APP
            try:
                dataList = []
                n = 0
                for i in data:
                    n = n+1
                    process = n/total*100
                    print(f'{n}|{total} - {process:.2f}%')
                    clear_line()

                    target = getData(url, i[0])
                    dataList.append(target)

                # REMOVE USELESS COLUMNS
                uselessCol = [
                    "kode_tender",
                    "rencana_umum_pengadaan",
                    # "label_paket",
                    "peserta_tender",
                    'khusus_orang_asli_papua_(oap)',
                    'alasan_pembatalan',
                    'alasan_di_ulang',
                    'reverse_auction?',
                    'uraian_singkat_pekerjaan',
                    'bobot_teknis',
                    'bobot_biaya'
                ]

                try:
                    df = DataFrame(dataList)  # DataFrame

                    try:
                        # RemoveColumns
                        [df.pop(key) for key in uselessCol]
                        # Fix Position
                        col = df.pop("lokasi_pekerjaan")
                        df.insert(13, 'lokasi_pekerjaan', col)
                    except:
                        pass

                    # Export to Excel
                    fileName = url.split('.')[1]

                    excel = ExcelWriter(f'lpse_{fileName}_{tahun}.xlsx', 'openpyxl')
                    df.to_excel(excel, index=False)
                    # excel.book.set_properties({'author': 'seimpairiyun'}) #xlsxwriter
                    excel.book.properties.creator = 'seimpairiyun'
                    excel.close()

                    return df

                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)

        else:
            print('Data LPSE masih kosong')

    except Exception as e:
        print('URL Failed to Open')
        # print(e)


# --------------------------------------------------

app_start = time.now()

url = 'https://lpse.bireuenkab.go.id'
regex = r"https?://lpse\..+\.(?:go|ac)\.id"
isLPSE = re.findall(regex, url)

if isLPSE != []:
    saveDataLPSE(url, 2022, 5)
    print(durasi(app_start))
else:
    print('URL tidak benar')


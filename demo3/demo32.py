#@author Lauri Poikolainen 24.1.2019
#Sheets on jaettu opettajaryhmälle

import gspread
import Adafruit_DHT
import time
from oauth2client.service_account import ServiceAccountCredentials

sensor = Adafruit_DHT.DHT11
pin=4
#odotus sekunneissa kuinka usein päivittää sheetti
odotus=300

kello = time.time()
#OAuth löytyy tuolta, heitetty FileZillalla sftp:n kautta
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("/home/pi/tiea345-lajopoik-bdce5badba64.json",scope)

gc = gspread.authorize(credentials)
wks=gc.open("TIEA345 demo2").sheet1
#worksheetin lähtörivi
rivi = 2


while True:
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    kello = time.asctime(time.localtime(time.time()))
    wks.update_cell(rivi,1,kello)
    wks.update_cell(rivi,2,temp)
    wks.update_cell(rivi,3,hum)
    rivi +=1
    time.sleep(300)

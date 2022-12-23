from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as soup
from songline import Sendline
import time

token = 'QyCCptwKhNb5oKQIeKPJuCRHXbttGGKnkGD0de8dwkj'

messenger = Sendline(token)

opt = webdriver.ChromeOptions() #สร้างออปชั่น
opt.add_argument('headless') #สั่งให้โปรแกรมไม่ต้องเปิด Chrome ขึ้นมา

path = r'D:\Coding\Basic Python Course\Automated Website\chromedriver_win32\chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(service=service,options=opt) #Create Driver

url = 'https://www.pttor.com/th/oil_price'

driver.get(url) #Open Web
time.sleep(10)
page_html = driver.page_source
driver.close()
data = soup(page_html,'html.parser') #scan data
table = data.find_all('div',{'class':'section-filter__table'})
table = table[0].find_all('tbody')
rows = table[0].find_all('tr')
todayprice = rows[0].find_all('td')
#print(todayprice)

oiltitle = ['วันที่',
            'DieselB20',
            'Diesel',
            'DieselB7',
            'E85',
            'E20',
            'Gasohol91',
            'Gasohol95',
            'Benzene',
            'Super Power Diesel B7',
            'Super Power Gasohol 95']
oilprice = []


for ol in todayprice:
    oilprice.append(ol.text.strip())

result = {}

for t,o in zip(oiltitle,oilprice):
    result[t] = o

#print(result)

#messenger.sendtext('ราคาดีเซลวันนี้: '+ result['Diesel'] + ' บาท')
'''
for name, pr in result.items():
    if name == 'วันที่':
        print(f'ราคาน้ำมันประจำวันที่ {pr}')
    else:
        print(f'ราคา {name} : {pr} บาท')
'''

for name, pr in result.items():
    if name == 'วันที่':
        messenger.sendtext(f'ราคาน้ำมันประจำวันที่ {pr}')
    else:
        messenger.sendtext(f'ราคา {name} : {pr} บาท')
    time.sleep(0.5)
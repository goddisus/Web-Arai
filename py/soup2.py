import requests
import bs4
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from urllib.parse import urljoin
import os
import codecs
from urllib.parse import unquote


def WebScrap():
    data = []
    url = ('https://finance.yahoo.com/quote/%5EDJI/history?period1=1546300800&period2=1613779200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true')

    raw = requests.get(url)
    #print(raw.text)
    #path = "./eiei"
    #os.makedirs(path, 0o755, exist_ok=True)
    ## Write content into a file
    #abs_file = path + '/data.html'
    #f = codecs.open(abs_file, 'w', 'utf-8')
    #f.write(raw.text)
    #f.close()
    # if ex == raw.text :
    #    print("hello")
    #ex = raw.text
    web_content = BeautifulSoup(raw.text, "lxml")
    price = web_content.find_all('tr')
    for i in range(1, len(price)-1):
        # print(i)
        ex = {}
        ex["date"] = price[i].find_all('td')[0].find('span').text
        ex["open"] = price[i].find_all('td')[1].find('span').text
        ex["high"] = price[i].find_all('td')[2].find('span').text
        ex["low"] = price[i].find_all('td')[3].find('span').text
        ex["close"] = price[i].find_all('td')[4].find('span').text
        ex["adjclose"] = price[i].find_all('td')[5].find('span').text
        ex["volumn"] = price[i].find_all('td')[6].find('span').text
        data.append(ex)
    # print(raw.text)
    #print(price[3].find('td', {'class':'text-right'}).text)

    # print(s,'HELO')
    # print(price[32])
    #price = price[2].find('a')
    # print(price.text)
    #ex = ex + '{' + "\"name\":\"" + price.text + "\","
    # print(ex)
    # print(len(price))
    return data


def mongo(data):
    import pymongo

    myc = pymongo.MongoClient(
        "mongodb+srv://ohmygod:sjR9s82s8CO1L1SO@ohmygod.z5xeb.mongodb.net/test")
    mydb = myc["stock"]
    mycol = mydb["dowjonehistory"]
    mycol.delete_many({})
    mycol.insert_many(data)

data = WebScrap()
mongo(data)
#path = "./src"
#os.makedirs(path, 0o755, exist_ok=True)
# Write content into a file
#abs_file = path + '/data.json'
#f = codecs.open(abs_file, 'w', 'utf-8')
#f.write(str(data))
#f.close()

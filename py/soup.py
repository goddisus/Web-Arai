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
    url = ('https://markets.businessinsider.com/index/components/dow_jones')

    raw = requests.get(url)
    # if ex == raw.text :
    #    print("hello")
    #ex = raw.text
    web_content = BeautifulSoup(raw.text, "lxml")
    price = web_content.find_all('tr')
    for i in range(2, len(price)):
        # print(i)
        ex = {}
        ex["name"] = price[i].find('a').text
        #ex = ex + '{' + "\"name\":\"" + price[i].find('a').text + "\","
        x = price[i].find('td', {'class': 'text-right'})
        s = ''
        x = x.text
        for j in range(2, len(x)):
            if x[j] == '\r':
                continue
            elif x[j] == '\n':
                s += ','
                continue
            elif x[j] == '\t':
                break
            s += x[j]
        l = s.split(',')
        #ex = ex + "\"lastestprice\":\"" + l[0] + "\","
        #ex = ex + "\"previouseprice\":\"" + l[1] + "\","
        ex["lastestprice"] = l[0]
        ex["previouseprice"] = l[1]
        x = price[i].find_all('td', {'class': 'text-right'})[1]
        s = ''
        x = x.text
        for j in range(2, len(x)):
            if x[j] == '\r':
                continue
            elif x[j] == '\n':
                s += ','
                continue
            elif x[j] == '\t':
                break
            s += x[j]
        l = s.split(',')
        #ex = ex + "\"low\":\"" + l[0] + "\","
        #ex = ex + "\"high\":\"" + l[1] + "\","
        ex["low"] = l[0]
        ex["high"] = l[1]
        #ex = ex + "\"nowpricediff\":\"" + price[i].find_all('span')[0].text + "\","
        #ex = ex + "\"nowperdiff\":\"" + price[i].find_all('span')[1].text + "\","
        ex["nowpricediff"] = price[i].find_all('span')[0].text
        ex["nowperdiff"] = price[i].find_all('span')[1].text
        x = price[i].find_all('span')[3]
        s = ' '
        x = x.text
        for j in range(len(x)):
            if x[j] == ' ':
                break
            s += x[j]
        #ex = ex + "\"time\":\"" + price[i].find_all('span')[2].text + s + "\","
        ex["time"] = price[i].find_all('span')[2].text + s
        #ex = ex + "\"threepricediff\":\"" + price[i].find_all('span')[4].text + "\","
        #ex = ex + "\"threeperdiff\":\"" + price[i].find_all('span')[5].text + "\","
        #ex = ex + "\"sixpricediff\":\"" + price[i].find_all('span')[6].text + "\","
        #ex = ex + "\"sixperdiff\":\"" + price[i].find_all('span')[7].text + "\","
        #ex = ex + "\"yearpricediff\":\"" + price[i].find_all('span')[8].text + "\","
        #ex = ex + "\"yearperdiff\":\"" + price[i].find_all('span')[9].text + "\"}"
        ex["threepricediff"] = price[i].find_all('span')[4].text
        ex["threeperdiff"] = price[i].find_all('span')[5].text
        ex["sixpricediff"] = price[i].find_all('span')[6].text
        ex["sixperdiff"] = price[i].find_all('span')[7].text
        ex["yearpricediff"] = price[i].find_all('span')[8].text
        ex["yearperdiff"] = price[i].find_all('span')[9].text
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
    mycol = mydb["dowjone"]
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

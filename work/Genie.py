import requests
from bs4 import BeautifulSoup

# Basic Setting
import certifi
from pymongo import MongoClient
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.r0t0c.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
#rank
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number

#title
#body-content > div.newest-list > div > table > tbody > tr:nth-child(15) > td.info > a.title.ellipsis

#artist
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

music = soup.select('#body-content > div.newest-list > div > table > tbody > tr');

for i in music:
    a = i.select_one('td.info > a.title.ellipsis')
    if a is not None:
        rank = i.select_one('td.number');
        title = a.text;
        artist = i.select_one('td.info > a.artist.ellipsis');

        print(rank.text[0:2].strip(), title.strip(), artist.text.strip())
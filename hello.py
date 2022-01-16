import requests
from bs4 import BeautifulSoup

# pymongo Basic-Code
import certifi
from pymongo import MongoClient
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.r0t0c.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# Crolling Basic-Code
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
movie = soup.select('#old_content > table > tbody > tr');

#old_content > table > tbody > tr:nth-child(2) > td.point
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img

for i in movie:
    a = i.select_one('td.title > div > a')

    if a is not None:
        title = a.text;
        rank = i.select_one('td:nth-child(1) > img')['alt'];
        rate = i.select_one('td.point').text

        doc = {
            'title':title,
            'rank':rank,
            'rate':rate
        }

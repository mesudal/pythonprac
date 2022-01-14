import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#rank
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img

#title
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a

#rate
#old_content > table > tbody > tr:nth-child(2) > td.point

# 코딩 시작
movie = soup.select('#old_content > table > tbody > tr');


for i in movie:
    rank = i.select_one('td:nth-child(1) > img');
    title = i.select_one('td.title > div > a');
    rate = i.select_one('td.point');

    if title != None or rate != None or rank != None:
        print(rank['alt'], title.text, rate.text)
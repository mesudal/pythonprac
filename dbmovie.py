# Basic Setting
import certifi
from pymongo import MongoClient
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.r0t0c.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# 문제1 : 영화제목 '가버나움' 평점 가져오기
movie = db.movies.find_one({'title':'가버나움'})
#print(movie['rate'])

# 문제2 : '가버나움'의 평점과 같은 평점의 영화 제목들을 가져오
movie_all = list(db.movies.find({},{'_id':False}))
# for i in movie_all:
#     if movie['rate'] == i['rate']:
#         print(i['title'])

# answp3 : '가버나움' 영화의 평점을 0으로 만들기
gabunaum = movie = db.movies.find_one({'title':'가버나움'})
db.users.update_one({'title':'가버나움'},{'$set':{'rate': '0'}})

print(gabunaum)
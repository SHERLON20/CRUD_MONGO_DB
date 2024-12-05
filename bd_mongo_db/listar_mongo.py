from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
mydb= client.dbposts
mycol=mydb.posts

#retornar os documentos de dentro do mongodb
result = mycol.find()
for r in result:
    pprint(r)
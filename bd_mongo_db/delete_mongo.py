from pymongo import MongoClient
client = MongoClient()
mydb= client.dbposts
mycol = mydb.posts
myquery={'categoria':'frontend'}
x= mycol.delete_one(myquery)
print('deletado com sucesso')
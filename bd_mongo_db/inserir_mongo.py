from pymongo import MongoClient
client = MongoClient()
mydb= client.dbposts
mycol = mydb.posts
post1={
    'title':'FastApi',
    'categotia':'backend',
    'autor': {
        'name':'sherlon',
        'email':'sherlonmachado20@gmail.com'
    }
    
}
result=mycol.insert_one(post1)
print('documento salvo com sucesso')
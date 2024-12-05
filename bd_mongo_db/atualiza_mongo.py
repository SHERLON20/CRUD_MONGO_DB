from pymongo import MongoClient
client = MongoClient()
mydb= client.dbposts
mycol = mydb.posts
old = {"categoria":"frontend"}
new = {"$set": {"categoria":"backend"}}
mycol.update_one(old,new)
print("dados atualizados")

#for x in mycol.find():
    #print(x)
import pymongo

client = pymongo.MongoClient("mongodb+srv://hg8655:8655340812@cluster0.mwt706o.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d={
    "name":"shudhanshu",
    "email":"sudhanshu2",
    "surname":"kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

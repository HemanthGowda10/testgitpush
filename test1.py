import pymongo

client = pymongo.MongoClient("mongodb+srv://hg8655:8655340812@cluster0.mwt706o.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["sudh"]

collection.insert_one(data1)

record = collection.find()

for i in record:
    print(i)

import pymongo

client = pymongo.MongoClient("mongodb+srv://hg8655:8655340812@cluster0.mwt706o.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {
    "name" : "sudhanshu",
    "mail_id" : "sudhanshu@ineuron.ai",
    "subject" : ["data scinece" , "big data " , "data analytics "]
}

database=client['myinfo']
collecion=database['sudh']
collection.insert_one(data)
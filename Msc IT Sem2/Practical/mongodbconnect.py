import pymongo
from pymongo import MongoClient
client =pymongo.MongoClient("mongodb+srv://admin:NTflI068WYVfLqEB@cluster0.yqzcyn4.mongodb.net/shop?retryWrites=true&w=majority&appName=Cluster0")
db = client.get_database('Practical')
records = db.Demo
db = client.test
print("Total Records present in this collections is",records.count_documents({}))
print(list(records.find()))

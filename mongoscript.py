from pymongo import MongoClient
import datetime
client = MongoClient("mongodb+srv://qwerty123:qwerty123@cluster0.zrw3uzs.mongodb.net/")

db = client.scrapy

posts = db.test_collection
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()}

post_id = posts.insert_one(post).inserted_id

print(post_id)





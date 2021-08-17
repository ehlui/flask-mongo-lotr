from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/animal_db")

# 1. Creating instance with basic DB data
client = MongoClient(host='localhost', port=27017)
# 2. Selecting database
db = client.animal_db
# 3. Querying and formating data to python-list
animals = list(db.animal_tb.find({}))

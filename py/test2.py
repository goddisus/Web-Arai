import pymongo

myc = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myc["testttt"]
mycol = mydb["test"]

mylist = [{"username": "6111234567","password": "123456789"},{"username": "6111234567","password": "123456789"},{"username": "6111234567","password": "123456789"},{"username": "6111234567","password": "123456789"}]

x = mycol.insert_many(mylist)

x = []
y = {"eiei":"eiei"}
x.append(y)
print(x)

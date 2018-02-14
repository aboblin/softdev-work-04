import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.test
rest = db.restaurants

x = rest.find({"borough": "Queens"})
for b in x:
    print b

y = rest.find({"address.zipcode": "11354"})
for a in y:
    print a
    
z = rest.find({"address.zipcode": "11354", "grades.grade": "A" })
for c in z:
    print c
    
omega = rest.find({"address.zipcode": "11354", "grades.score": {"$lt": 3} })
for p in omega:
    print p


local_american = rest.find({"address.zipcode": "10282", "cuisine": "American"})
for suh in local_american:
    print suh

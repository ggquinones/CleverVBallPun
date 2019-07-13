import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["FanVolley"]

mycol = mydb["teams"]
print(mydb.list_collection_names())


		
		

def MakeTeamsTable():
	mylist = [
  { "_id": 1, "teamName": "Denver", "players": []},
  { "_id": 2, "teamName": "South Dakota", "players": []},
  { "_id": 3, "teamName": "Omaha", "players": []},
  { "_id": 4, "teamName": "Purdue Fort Wayne", "players": []},
  { "_id": 5, "teamName": "North Dakota", "players": []},
  { "_id": 6, "teamName": "Oral Roberts", "players": []},
  { "_id": 7, "teamName": "North Dakota State", "players": []},
  { "_id": 8, "teamName": "South Dakota State", "players": []},
  { "_id": 9, "teamName": "Western Illinois", "players": []}
	]
	x = mycol.insert_many(mylist)

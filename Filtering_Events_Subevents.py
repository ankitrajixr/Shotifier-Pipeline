
#Importing libraries
import pymongo 
import pprint
import pandas as pd

#connecting mongodb and python
mongo_uri = "mongodb://localhost:27017/"  
client = pymongo.MongoClient(mongo_uri)
client.list_database_names()
db = client.Wyscout
db.list_collection_names()


#Filtering events and sub events with respect to goal
table=db.matches_events_v02.find({"Tag_1":"101"},{"_id":0, "eventName":1, "subEventName":1,  "playerId":1, "teamId":1, "matchId":1 })
table_df=pd.DataFrame(table2)
table_df.head(100)


#Filtering tags with respect to shots
table1= db.matches_events_v02.aggregate([
{'$project':{"_id":0, "eventName":1, "subEventName":1, "playerId":1, "teamId":1, "matchId":1}
},
{'$match':{'$or':[{"eventName":"Shot"},{"subEventName":"Shot"}]}}
])
table1_df =pd.DataFrame(table)
table1_df.head(1000)
len(table1_df)


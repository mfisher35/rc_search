import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017')
rc_msg = client['parties']["rocketchat_room"]
#result = rc_msg.find({ "$text" : {"$search" : "EIN" } })
result = rc_msg.find()
cmap  = {}

for item in result:
    if "name" in item:
       cmap[item['_id']] = item[u'name']

print( cmap)
    #print "(" + str(item['ts'])+")  "+ item[u'u']['username']+": "+ item['msg']
#print dir(parties)

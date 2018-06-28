from flask_restful import Resource, Api
from flask import Flask,jsonify,json,request,Response
from flask_cors import CORS
import pymongo

db_name = 'parties'
client = pymongo.MongoClient('mongodb://localhost:27017')

app = Flask(__name__)
CORS(app)
api = Api(app)


rc_msg = client[db_name]["rocketchat_message"]
rc_rm = client[db_name]["rocketchat_room"]


class search(Resource):
    def get(self,text):
        rooms_res = rc_rm.find()
        cmap  = {}
        cur_r = ""
        body = ""
        for item in rooms_res:
            if "name" in item:
               cmap[item['_id']] = item[u'name']

        result = rc_msg.find({ "$text" : {"$search" : text } })
        count = 0
        
        for item in result:
            try:
               cur_r = "<h3> (" + str(item['ts'])+ " in Room #%s)  " % cmap[item['rid']] + item[u'u']['username']+": "+ item['msg'] + "</h3><hr>"
               if not cur_r in body:
                   body = body + cur_r
                   count = count + 1
            except:
               a = 1
            
        html = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">' + "<h1>%i Result(s): </h1><br><hr>" % count + body
        response = Response(response=html,status=200,mimetype='text/html')
        return response


api.add_resource(search, '/search/<text>') 


if __name__ == '__main__':
     app.run(host= '0.0.0.0', port='5006')

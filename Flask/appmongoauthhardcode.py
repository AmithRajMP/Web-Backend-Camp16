from flask import Flask, request
from pymongo import MongoClient
from flask_restful import Resource , Api
from bson.objectid import ObjectId
from bson.errors import InvalidId

client = MongoClient('localhost',27017)
db = client.camp2016
notes = db.notes
app = Flask(__name__)
api = Api(app)

class authentication(Resource):
	def post(self):
		name = request.values.get('username',None)
		pword = request.values.get('password',None)
		if(name=="Amith" and pword=="veyron"):
			return "Authenticated and Welcome",200
		else:
			return "Bad Credentials",201


api.add_resource(authentication, "/auth")

class application(Resource):
	def get(self):
		data=[]
		print notes.find()
		for note in notes.find():
			print note
			note['_id'] = str(note['_id'])
			data.append(note)
		return data
 
	def post(self):
		name_id=request.values.get('taskname', None) 
		status_id=request.values.get('status', None)
		notes.insert({"taskname":name_id,"status":status_id})
		return "Inserted to Database",201

	def delete(self):
		name_id=request.values.get('taskname',None)
		status_id=request.values.get('status',None)
		notes.remove({"taskname":name_id})
		notes.remove({"status":status_id})
		return "Deleted from Database",200

	def put(self):
		object_id=ObjectId(request.values.get('_id',None))
		name_id=request.values.get('taskname',None)
		status_id=request.values.get('status',None)
		notes.update({'_id':object_id},{'$set':{'taskname':name_id,'status':status_id}})
		return "Edited from Database",200

		
api.add_resource(application, "/")



if __name__ == "__main__" :
    app.run(debug=True)

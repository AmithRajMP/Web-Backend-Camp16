from flask import Flask, request , session, render_template, redirect
from pymongo import MongoClient
from flask_restful import Resource , Api
from bson.objectid import ObjectId
from bson.errors import InvalidId

client = MongoClient('localhost',27017)
db = client.foss
db1 = client.camp2016
users = db1.users
webapps = db.web
users = db.users
mediaeditingapps = db.mediaediting
hardwareapps = db.hardware
texteditorsapps = db.texteditors
designapps = db.design
app = Flask(__name__)
api = Api(app)

class server(Resource):
	def post(self): 
		name = request.values.get('username',None)
		pword = request.values.get('password',None)
		result=db.users.find({"username":name,"password":pword}).count()
		if(result==0):	
			return "Bad Credentials",201
		else:
			session["username"]=name
			return "Authenticated and Welcome"+name,200

api.add_resource(server, "/server")
if __name__ == "__main__" :
	app.secret key="veyron"
    app.run(debug=True)

class web(Resource):
	def get(self):
		data=[]
		print webapps.find()
		for name in webapps.find():
			print name
			name['_id'] = str(name['_id'])
			data.append(name)
		return data

api.add_resource(web, "/web")

class design(Resource):
	def get(self):
		data=[]
		print designapps.find()
		for name in designapps.find():
			print name
			name['_id'] = str(name['_id'])
			data.append(name)
		return data

api.add_resource(design, "/design")

class hardware(Resource):
	def get(self):
		data=[]
		print hardwareapps.find()
		for name in hardwareapps.find():
			print name
			name['_id'] = str(name['_id'])
			data.append(name)
		return data

api.add_resource(hardware, "/hardware")

class mediaediting(Resource):
	def get(self):
		data=[]
		print mediaeditingapps.find()
		for name in mediaeditingapps.find():
			print name
			name['_id'] = str(name['_id'])
			data.append(name)
		return data

api.add_resource(mediaediting, "/media")

class texteditors(Resource):
	def get(self):
		data=[]
		print texteditorsapps.find()
		for name in texteditorsapps.find():
			print name
			name['_id'] = str(name['_id'])
			data.append(name)
		return data

api.add_resource(texteditors, "/text")



if __name__ == "__main__" :
    app.run(debug=True)

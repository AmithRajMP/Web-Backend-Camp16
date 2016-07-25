from flask import Flask, request , session, render_template, redirect
from pymongo import MongoClient
from flask_restful import Resource , Api
from bson.objectid import ObjectId
from bson.errors import InvalidId

client = MongoClient('localhost',27017)
db = client.camp2016
users = db.users
app = Flask(__name__)
api = Api(app)

class Authenticate(Resource):
	def post(self): 
		name = request.values.get('username',None)
		pword = request.values.get('password',None)
		result=db.users.find({"username":name,"password":pword}).count()
		if(result==0):	
			return "Bad Credentials",201
		else:
			session["username"]=name
			return "Authenticated and Welcome "+name,200

@app.route("/")
def server():
	name = session.get("username",None)
	if name:
		return redirect("/getuser/")
	else:
		return render_template('login.html')

@app.route("/getuser/")
def check():
	name = session.get("username",None)
	if name:
		return name
	else:
		return "User not Logged In"

@app.route("/logout/")
def logout():
		session.pop("username",None)
		return "User Logged Out"

api.add_resource(Authenticate, "/auth")
if __name__ == "__main__" :
	app.secret_key="veyron"
	app.run(debug=True) 
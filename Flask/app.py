from flask import Flask,render_template
from flask import request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/todo'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    taskname = db.Column(db.Text)
    status = db.Column(db.Boolean,default=False)
    taskdes = db.Column(db.Text)
    taskpriority = db.Column(db.Text)
    taskdate = db.Column(db.Text)
    projectname = db.Column(db.Text)

    def __init__(self,taskname,taskdes,taskpriority,taskdate,projectname):
        self.taskname = taskname
        self.taskdes = taskdes
        self.status = False
        self.taskpriority = taskpriority
        self.taskdate = taskdate
        self.projectname = projectname
db.create_all()

@app.route("/")
def task_query():
    tasks = Task.query.all()
    return render_template('list.html',todos=tasks)

@app.route("/add/", methods=["POST"])
def add_task():
    taskname = request.form["taskname"]
    taskdes = request.form["taskdescription"]
    taskpriority = request.form["taskpriority"]
    taskdate = request.form["taskdate"]
    projectname = request.form["projectname"]
    task = Task(taskname,taskdes,taskpriority,taskdate,projectname)
    db.session.add(task)
    db.session.commit()
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    print task_id
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

@app.route("/changestatus/<int:task_id>")
def change_status(task_id):
    print task_id
    task = Task.query.get(task_id)
    if task.status==True:
        task.status=False
    else:
        task.status=True
    db.session.add(task)
    db.session.commit()
    return redirect("/")

@app.route("/edit/<int:task_id>")
def edit_task_view(task_id):
    print task_id
    task = Task.query.get(task_id)
    return render_template('edit.html',task=task)
    
@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):
    task = Task.query.get(task_id)
    task.taskname = request.form["newtaskname"]
    task.taskdes = request.form["newtaskdescription"]
    task.taskpriority = request.form["newtaskpriority"]
    task.taskdate = request.form["newtaskdate"]
    task.projectname = request.form["newprojectname"]
    db.session.commit()
    return redirect("/")

if __name__ == "__main__" :
    app.run(debug=True)

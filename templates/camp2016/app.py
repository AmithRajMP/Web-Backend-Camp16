from flask import Flask, request, redirect, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/get")
def getTodo():
    with open("f", "r") as file:
        tasks = []
        todos = file.read().split("\n")[0:-1]
        for todo in todos:
            tasks.append(todo.split(";"))
        return render_template("index.html", todos=tasks)


@app.route("/add", methods=["POST"])
def createTodo():
    with open("f", "a") as file:
        print request.values.get("name") + ";" + request.values.get("status") + ";" + request.values.get(
            "project") + ";"+ request.values.get("description") + ";" + request.values.get("duedate") + "\n"
        file.write(request.values.get("name") + ";" + request.values.get("status") + ";" + request.values.get(
            "project") + ";" + request.values.get("description") + ";" + request.values.get("duedate") + "\n")
    return redirect("/get")


@app.route("/delete")
def deleteTodo():
    receivedName = request.values.get("name", None)
    todos = []
    if receivedName:
        with open("f", "r") as file:
            todos = file.read().split("\n")[0:-1]
        with open("f", "w") as file:
            for todo in todos:
                name = todo.split(";")[0]
                status = todo.split(";")[1]
                project = todo.split(";")[2]
                description = todo.split(";")[3]
                duedate = todo.split(";")[4]
                if receivedName != name:
                    file.write(name + ";" + status + ";" + project + ";" + description +";" + duedate + "\n")
            return redirect("/get")
    else:
        return "Data not received"


@app.route("/todo")
def editTodoView():
    receivedName = request.values.get("name", None)
    if receivedName:
        with open("f", "r") as file:
            todos = file.read().split("\n")[0:-1]
            for todo in todos:
                name = todo.split(";")[0]
                if receivedName == name:
                    return render_template("edit.html", todo=todo.split(";"))
    else:
        return "Data not received"


@app.route("/edit", methods=["POST"])
def editTodo():
    receivedName = request.values.get("name", None)
    receivedStatus = request.values.get("status", None)
    receivedProject = request.values.get("project", None)
    receivedDescription = request.values.get("description",None)
    receivedDuedate = request.values.get("duedate",None)
    todos = []
    if receivedName and receivedProject and receivedStatus:
        with open("f", "r") as file:
            todos = file.read().split("\n")[0:-1]
        with open("f", "w") as file:
            for todo in todos:
                name = todo.split(";")[0]
                status = todo.split(";")[0]
                project = todo.split(";")[0]
                description = todo.split(";")[0]
                duedate = todo.split(";")[0]
                if receivedName == name:
                    file.write(receivedName + ";" + receivedStatus + ";" + receivedProject + ";" + 
                    	receivedDescription + ";" + receivedDuedate + "\n")
                else:
                    file.write(name + ";" + status + ";" + project + ";" + description + ";" + duedate + "\n")
            return redirect("/get")
    else:
        return "Data not received"


if __name__ == '__main__':
    app.run(debug=True)

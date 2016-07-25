from pymongo import MongoClient #Database connector

client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.camp2016    #Select the database
todos = db.todo #Select the table


def list():
    for todo in todos.find():
        print todo


def add():
    name = raw_input("Enter name ")
    status = raw_input("Enter status ")
    project = raw_input("Enter project ")
    todos.insert({ "name":name, "status":status, "project":project })
    print "Inserted Successfully"


def edit():
    name = raw_input("Enter name ")
    for todo in todos.find({"name":name}):
        print todo
    status = raw_input("Enter new status ")
    project = raw_input("Enter new project ")
    todos.update({"name":name}, {'$set':{"status":status, "project":project}})
    print "Updated Successfully"


def delete():
    name = raw_input("Enter name ")
    for todo in todos.find({"name":name}):
        print todo
    todos.remove({"name":name})
    print "Deleted Successfully"


if __name__ == '__main__':
    print "1. List\n2. Add\n3. Edit\n4. Delete"
    choice = raw_input("Enter your choice\n")
    if choice == "1":
        list()
    elif choice == "2":
        add()
    elif choice == "3":
        edit()
    elif choice == "4":
        delete()
    else:
        "Don't act smart. :-P"

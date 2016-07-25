num=input("1.write\n2.read")
class ToDo:
   tname=raw_input("Enter the task name")
   description=raw_input("Enter the task description")
   priority=raw_input("Enter the priority")
   date=raw_input("Enter the date")
   pname=raw_input("Enter the project name")
   tstatus=raw_input("Enter the task status")
if(num==1):
    def write():
      fd = open(task.txt,'a')
      fd.write(ToDo.tname)
      fd.write(ToDo.description)
      fd.write(ToDo.priority)
      fd.write(ToDo.date)
      fd.write(ToDo.pname)
      fd.write(ToDo.tstatus)
      fd.write("\n")
      fd.close()
elif(num==2):
    def read():
      fd = open(task.txt,'r')
      fd.read(ToDo.tname)
      fd.read(ToDo.description)
      fd.read(ToDo.priority)
      fd.read(ToDo.date)
      fd.read(ToDo.pname)
      fd.read(ToDo.tstatus)
      fd.close()

class todo:
  def __init__(self, task, status):
    self.task = task
    self.status = status

  def __str__(self):
    return f"{self.task}({self.status})"

def addtask():
    Usertask = input("Add task:")
    t4 = todo(Usertask,False)
    todolist.append(t4)
    for tsk in todolist:
        print(tsk)

def updatetask():
    taskid = int(input("Enter taskid of the task that is completed "))
    todolist[taskid-1].status = True
    for tsk in todolist:
        print(tsk)

t1 = todo("pickup groceries", False)
t2 = todo("Repair car", False)
t3 = todo("Go to college", False)

todolist=[t1,t2,t3]
for tsk in todolist:
  print(tsk)

y=True
while y == True:
    opt = int(input("What would you like to do\n1. Additem\n2. Updatetask\nEnter a number:"))

    match opt:
        case 1:
            addtask()
        case 2:
            updatetask()
        






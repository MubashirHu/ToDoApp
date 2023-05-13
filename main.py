from tkinter import *
from tkinter import simpledialog

root = Tk()
root.title("KanBan Board")
root.geometry('1000x800')

currentTaskRow = 0
currentIPTaskRow = 0
listofTasks = []
var = IntVar()

#Requested tasks
reqTaskFrame = LabelFrame(root, text="Requested Tasks", padx=5, pady=10)
reqTaskFrame.grid(row=0, column=0)
label1 = Label(reqTaskFrame, text="Requested", padx=50, pady=50)
label1.grid(row=0, column=0)

def addNewTask():
    global currentTaskRow
    newTaskFrame = LabelFrame(reqTaskFrame, text="Task:", padx=5, pady=10)
    newTaskFrame.grid(row=currentTaskRow, column=0)
    newTaskString = simpledialog.askstring(title="Add new task", prompt="Add a task")
    listofTasks.append(newTaskString)

    if newTaskString and len(newTaskString) > 0:
        taskButton = Checkbutton(newTaskFrame, text=newTaskString, padx=5,pady=10, variable=var,onvalue=1, offvalue=0, command=moveRequestedTaskToInProgress)
        taskButton.pack()
        currentTaskRow+=1
    else:
        pass

addTaskButton = Button(root, text="Add Task", command=addNewTask)
addTaskButton.grid(row=100, column=0)

#In progress tasks
ipTaskFrame = LabelFrame(root, text="In-Progress Tasks", padx=5, pady=10)
ipTaskFrame.grid(row=0, column=1)
label2 = Label(ipTaskFrame, text="In-Progress", padx=50, pady=50)
label2.grid(row=0, column=0)

#completed tasks
completedTaskFrame = LabelFrame(root, text="Completed Tasks", padx=5, pady=10)
completedTaskFrame.grid(row=0, column=2)
label3 = Label(completedTaskFrame, text="Completed", padx=50, pady=50)
label3.grid(row=0, column=0)

# create a function to move a task from requested to in progress
def move_task(task):
    # remove the task from the requested frame
    for child in reqTaskFrame.winfo_children():
        if child["text"] == task:
            child.destroy()
            break

    # add the task to the in progress frame
    task_label = Label(ipTaskFrame, text=task)
    task_label.pack()

def moveRequestedTaskToInProgress():
   global currentIPTaskRow
   if var.get() == 1:
    newTaskFrame = LabelFrame(ipTaskFrame, text="Task:", padx=5, pady=10)
    newTaskFrame.grid(row=currentTaskRow, column=1)
   else:
      pass
   
root.mainloop()
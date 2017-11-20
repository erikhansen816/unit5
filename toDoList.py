#Erik Hansen
#11/20/17
#toDoList.py


toDoList = []
print("Valid commands: add, delete, print, quit")

while True:
    task = input("> ")
    if "quit" in task:
        break
    elif "print" in task:
        for w in toDoList:
            print(w)
    elif task[:4] == "add ":
        toDoList.append(task[4:])
    elif task[:7] == "delete ":
        if task[7:] in toDoList:
            toDoList.remove(task[7:])
        else:
            print(task[7:], "not in list")
    else:
        print("Invalid Command")

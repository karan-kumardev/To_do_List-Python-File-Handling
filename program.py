import json
import matplotlib.pyplot as plt


completed=0
pending=0
id=0    
Tasks={"tasks":[],"Pending Count":pending, "Completed Count":completed}

#-------------------------Data Saving----------------------------------------
def savetask(Tasks,username):
    global pending,completed,id
    try: 
        with open(username,"w") as file:
          json.dump(Tasks,file,indent=4)
          print(f"Files saved in {username} file")
    except FileNotFoundError:
         print("exception occured while saving")      

def savefiles(filename,files):#usernames, emails,passwords

    try:     
        with open(filename,"w") as file:
          json.dump(files,file,indent=4)
          

    except Exception:
         print("user data files didnt save properly")
         
def loadfiles(filename):
     
     try:
          with open(filename,'r') as file:
            return json.load(file)
            
     except FileNotFoundError:
          return []   


def loadtasks(name):
     global Tasks,completed,pending,id

     try:
          with open(name,'r') as file:
            Tasks=json.load(file)
            print("Previous Files loaded")

            pending=Tasks["Pending Count"]
            completed=Tasks["Completed Count"]
            id=Tasks["tasks"][-1]["task_id"] #takes the last id from task_id


     except FileNotFoundError:
          
          Tasks={"tasks":[],"Pending Count":0, "Completed Count":0}
          id=pending=completed=0
          print("No Old Records Exist,starting new")     

#--------------------------------------------------------------------------------------

def get_right_input(prompt):
    while True:
        try:
          return int(input(prompt))
        except ValueError:
          print("Please Enter a valid number ")  

def addTasks(tasks,username):

    global Tasks,completed,pending,id
    pending+=1
    id+=1
    Tasks["tasks"].append({"task_id":id,"Task":tasks})
    Tasks["Pending Count"]=pending
    Tasks["Completed Count"]=completed      
    savetask(Tasks,username)
    print("✅ Task Added!\n") 

def updateTasks(task_number,username):
    global Tasks

    if not any(task["task_id"] == task_number for task in Tasks["tasks"]):
        
            print("The Task ID Doesn't Exist")         
            return

    for target in Tasks["tasks"]:
           if target["task_id"]==task_number:  
            target["Task"]=input("Enter the updated task.. ")
            print("Task ", target["task_id"], " Updated!")
            break

     
           
    savetask(Tasks,username)

def deleteTasks(task_id,username):

    global Tasks,pending

    if not any(task["task_id"] == task_id for task in Tasks["tasks"]):
        
               print("The Task ID Doesn't Exist")         
               return

    for target in Tasks["tasks"]:
         if target["task_id"]==task_id:
              Tasks["tasks"].remove(target)
              set_order(task_id)
              pending-=1
              Tasks["Pending Count"]=pending
              print("Task Deleted!")     
              break

   
           
    savetask(Tasks,username)

def markTasks(task_number,username):

    global Tasks,pending,completed

    for target in Tasks["tasks"]:
         if target["task_id"]==task_number:
              Tasks["tasks"].remove(target)
              set_order(task_number)
              pending-=1
              completed+=1
              Tasks["Pending Count"]=pending
              Tasks["Completed Count"]=completed
              print("Task marked as Complete!! ")
             
              break
         
    savetask(Tasks,username)           

def set_order(task_number):
     global Tasks,id
     
     for target in Tasks["tasks"]:
          if(target["task_id"]>task_number):
          
               target["task_id"]=target["task_id"]-1
          

def viewTasks():
    global Tasks
    if Tasks is {}:
        print("Nothing loaded from memory")
        
    else:
        print("Viewing Tasks...")
        print("Task ID"," "*8, "Task")
        for task in Tasks["tasks"]:
             print(" ",task["task_id"]," "*12,task["Task"])

def program(name):
    global completed,pending,id
    global Tasks 
    while True:
                print(f"{'='*50}")
                print(f"{'='*20}","Menu", f"{'='*24}")
                print(name)
                print(f"{'='*50}")
                print("Press 1 To View All Tasks")
                print("Press 2 To Add Tasks")
                print("Press 3 to Show Statistic Chart")
                print("Press 4 To Update Tasks by Number") 
                print("Press 5 To Delete Tasks by Number")
                print("Print 6 to Mark task as Complete")
                print("Press 7 To Quit the App\n")

                print(f"{'*'*80}")
                print(f"{' '*15}","⛔ Tasks Pending: ",Tasks["Pending Count"],f"{' '*15}","✅ Tasks Completed: " ,Tasks['Completed Count'])
                print(f"{'*'*80}\n")

                option=get_right_input("Enter your Choice ")
                    

                if option==1:
                        viewTasks() 

                elif option==2:
                    print("Type 0 to return ")
                    print("You Choose to Add Tasks!\n")
                    times=get_right_input("Enter How many Tasks you want to Add ")

                    if times==0:
                        print("Back to Main Menu!")
                        continue       

                    for i in range(times) :
                            tasks=input(f"Enter the task {i+1} in words.. ")
                            addTasks(tasks,name)

                elif option==3:
                        print("Showing Chart")
                        plt.pie([Tasks["Completed Count"],Tasks["Pending Count"]],
                                labels=["Completed Tasks","Pending Tasks"],colors=["green","blue"])
                        plt.legend()
                        plt.show()
                        print("Chart Shown!!")


                elif option==4:
                    print("Type 0 to return ")
                    print("You Choose to Update Tasks!\n")
                    print("Task ID"," "*8, "Task")
                    for task in Tasks["tasks"]:
                        print(" ",task["task_id"]," "*12,task["Task"])

                    task_no=get_right_input("Enter Task number to Update it ")
                    if task_no==0:
                        print("Back to Main Menu!")
                        continue    
                    updateTasks(task_no,name)

                elif option==5:
                    print("Type 0 to return ")
                    print("You Choose to Remove Tasks!\n")
                    print("Task ID"," "*8, "Task")
                    for task in Tasks["tasks"]:
                        print(" ",task["task_id"]," "*12,task["Task"])

                    number=get_right_input("Enter the Task Number to Remove ")
                    if number==0:
                        print("Back to Main Menu!")
                        continue  
                    deleteTasks(number,name)

                elif option==6:
                    print("Type 0 to return ")
                    print("You Choose to Mark Tasks Complete!\n")
                    print("Task ID"," "*8, "Task")
                    for task in Tasks["tasks"]:
                        print(" ",task["task_id"]," "*12,task["Task"])
                    number=get_right_input("Enter Task Number to mark them Complete ")
                    if number==0:
                        print("Back to Main Menu!")
                        continue

                    markTasks(number,name)

                elif option==7:
                        print("You Choose to End the Program!\n")
                        break     

                else:
                        print("Invalid Input Try Again!\n")

                    
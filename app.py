#APPLICATION
from login_Page import *   #my own python file
from program import *      #my own python file

usernames=[] #only usernames
emails=[]  #only emails
database=[] #overall data of users collectively

#---------Loading Files-----------------------------
usernames=loadfiles("username.json")
emails=loadfiles("emails.json")
database=loadfiles("database.json")
#---------------------------------------------------
while True:
    
    print('='*50)
    print("Already Have an Account? LogIn")
    print("Didn't Have an Account?  Signup")
    print("="*50,"\n")

    print("Press 1 to Login")
    print("Press 2 to Signup")
    print("Press 3 to Close")

    choice=get_right_input("Enter your Choice ")

    if choice==1:
        print('='*50)
        print(" "*17,"Login Page"," "*20)
        print('='*50,"\n")
        account=False
        
        gmail=input("Enter your Gmail ")
        password=input("Enter your Password ")
        name=''
    
        for record in database:
            if record["email"]==gmail and record["password"]==password:
             name=record["username"]
             name+=".json"
             account=True
             break
        else:
             print("Account Doesnt Exist.\n Sign-Up!!") 

        if account:
             loadtasks(name)
             program(name)

    if choice==2:    
#-------------------------------username section-----------------------------------------------    
        while True:
            print('='*50)
            print(" "*17,"Signup Page"," "*20)
            print('='*50,"\n")

            username=input("Enter your Username ")
            
            if username not in usernames:
                print("Username Added✅")
                break
            else:
                  print("This Username is Already Taken. Try making it Unique")
#-------------------------------------------------------------------------------            
            
#---------------------------------Email Section-------------------------------------------            
        while True:
                email=input("Enter your E-mail ")

                if validate_email(email):
                   
                    if email not in emails:#not already existing
                            print("Email Entered✅")
                            break    
                    else:
                        print("Email Already Exists.Two Emails cant be same ")   
#-------------------------------------------------------------------------------            

#------------------------------------Password Section----------------------------------------            
        while True:
                    print('='*60)
                    print("\nPassword must be of length 8, contain a Capital,a Small letter","\na Number and a Special Character")
                    print('='*60,"\n")
                    password=input("Enter your Password ")

                    if validate_password(password):
                        confirmed=input("Confirm your Password ")

                        if password==confirmed: 
#-------------------------------------------------------------------------------------------            
#----------------------------saving the accurate,exact data, no leftoves--------------------------
                            emails.append(email)
                            usernames.append(username)

                            database.append({"username":username,"email":email,"password":password})

                            savefiles('usernames.json',usernames)
                            savefiles("emails.json",emails) 
                            savefiles("database.json",database)
#----------------------------------------------------------------------------------
                            print("Sign-Up Successful✅","\n","Log-In Now!!")
                            break
                        else:
                            print("Password Doesnt Match❌\n Try Again")
                    else:
                         print("Invalid Password❌")        
    
    if choice==3:
         print("Exited!")
         break


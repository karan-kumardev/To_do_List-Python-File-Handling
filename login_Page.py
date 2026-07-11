import re

# Login Page
def validate_email(email):
   pattern=r"[a-zA-Z0-9._]+\@(gmail|yahoo)\.(com|net|edu|pk|in)$"

   if re.match(pattern,email):
      return True
   else:
      return False
   

def validate_password(password):
   status=False
   if password.__len__()>8:
    upper=[chr(i) for i in range(65,91)]
    lower=[chr(i) for i in range(97,123)]
    nums=[chr(i) for i in range(48,58)]
    special=['!','@','#','$','%','^','&','*','(',')','+','-','_','.',]

    if any(i in upper for i in password):
            status=True
    else: 
        status=False
        return status

    if any(i in lower for i in password):
           status=True
    else:
       status=False
       return status
            
    if any(i in nums for i in password):
           status=True
    else:
            status=False
            return status

    if any(i in special for i in password):
           status=True
    else:
         status=False
         return status

   else:
    status=False
    

   return status        

if __name__== "__main__":
    
   email=input("Enter the email ")

   if validate_email(email):
      print("You entered a valid Email\n")
      password=input("Enter your Password ")

      if validate_password(password):
         print("Password added Successfully")
      else:
         print("Password must contain Capital and Small Aplhabets along with Special " \
         "Characters and Numbers")

   else:
      print("You entered an Invalid Email")



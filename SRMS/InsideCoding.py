from tkinter import messagebox
# Password
pass1 =input("Enter Password: ")
l,u,p,d=0,0,0,0
if len(pass1)>=8:
    for i in pass1:
        if(i.islower()):
            l+=1   
        elif(i.isupper()):
            u+=1 
        elif(i.isdigit()):
            d+=1 
        elif(i=='@'or i=='&'or i=='#' or i=='!' or i=='_'):
            p+=1 
    if(l>=1 and u>=1 and d>=1 and p>=1):
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    messagebox.showerror("Error","Password should have 8 characters ,atleast one upper case letter,atleast one lower case letter, atleast one numeric value and atleast one special character")

# First Name and Last Name
FirstName = "Rahul Babu"
LastName = "M P"
fn = 0
ln = 0
for i in FirstName:
    if i.isupper() or i.islower():
        fn+=1 
for i in LastName:
    if i.isupper() or i.islower():
        ln+=1 
if fn == len(FirstName) and ln == len(LastName):
    print("OK")
else:
    print("Error")

contact="1234567288"
s = 0
for i in contact:
    if i.isdigit():
        s+=1
if s==10:
    print("Continue")
else:
    print("error")

# Right Email address Verification
pass1 ="rahulbabu@rajalakshmi.edu.in"
k=pass1[-10:-1]
j=k+"m"
print(j)

if(j!="@rajalakshmi.edu.in"):
    print("error")
else:
    print("Ok")
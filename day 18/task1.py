# Take two numbers as input and add those numbers. Handle the possible exceptions.
try:
    a= int (input ("enter the  number : "))
    b= int (input ("enter the  second number : "))
except (ValueError,TypeError,SyntaxError):
    print("there has been some error")
else:
    print(a+b)



# Take two numbers input and divide a number by another number. Handle the possible exceptions.
try:
    a= int (input ("enter the  number : "))
    b= int    (input ("enter the  second number : "))
    c=(a/b)
except (ValueError,TypeError,SyntaxError,ZeroDivisionError):
    print("there has been some error")
else:
    print(c)
finally:
    print("the code is completed")





# Create a dictionary student with keys id, name, age, department. Take a input from the user, which info (id, name, age or department) he wants to access and print the result.
#  Handle the possible exceptions.
    


student= {"id":"5674","name":"rabi","department":"science"}
try:
    c= input ("enter the key you want to access : ")
    d=student[c]
    
except KeyError:
    print("the key is not available")
else:
    print(f"the {c} of the student is {d}")

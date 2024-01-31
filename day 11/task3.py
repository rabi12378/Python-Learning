# WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number.


hour=float(input("enter the hour of work : "))
rate =  float (input("enter the hourly rate : "))
if hour <=40 :
    print(f"the salary of the worker is {rate * hour}")
else:
   print(f"the salary of the worker is {(rate * 40)+(hour-40)*(rate *1.5)} ")
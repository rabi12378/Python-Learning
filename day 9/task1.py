# WAP to take a number input. If the number is divisible by 3 print "fizz", if divisible by
# 5 print "buzz", if divisible by both 3 and 5 print "fizzbuzz". If not divisible by both 3 and 5
# then print the number as it is.
a=int(input("enter the number"))
if a%3==0 and a%5==0:
    print("fizzbuzz")
elif a%5==0 and a%3!=0:
    print("buzz")
else:
    print("fizz")
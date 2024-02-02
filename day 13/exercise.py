# WAP to calculate the factorial of 7 using python reduce( ) function using lambda
from functools import reduce
result= reduce (lambda a,b:a*b,range(1,8))
print(result)
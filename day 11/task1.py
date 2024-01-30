# WAP to delete all the occurrences of a specified character in a given string 
# S = “All the occurrences of a specified character in a given string”
# Input = “a”
# Output = “ll occurrences of  specified chrcter in  given string”
s="all the occurences of a specified chaarcter in a given string"
a=input('enter the alphabet to remove')
result=""
for i in s:
    if i==a:
     continue
    result+=i
print(result)    




# Create a new list of repeated items from a provided list:
# nums = [3, 4, 2, 2, 1, 3, 3, 3]
# Output = [3, 2]

# nums = [3, 4, 2, 2, 1, 3, 3, 3]

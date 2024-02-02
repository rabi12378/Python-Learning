data = [2,3,4,5,6]
def square (element):
    return element **2

result= map(square, data)
print(list(result))
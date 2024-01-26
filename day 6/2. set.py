# Set is also an iterable (sequence of elements) in python like list and string
# Set elements are enclosed in curly braces {}
# Set is a mutable datatype but the elements of the set must be immutable

# Creating set in python
a = set() # empty set

b = {1, 2, 3}
vowels = {"a", "e", "i", "o", "u"}

data = {"a", 1, 2.1}  # set can have mixed datatypes.

# c = {1, 2.1, ["a", "b"]}  # Invalid set. It raises error


# Unlike list, set doesn't support indexing and slicing because set is unordered
d = {1, 2}
e = {2, 1}
print(d == e)  # True

# adding and removing set elemeentss
s1={1,2,3}
s1.add(4)
print(s1)
s1.update([3,4,5,6,7])
print(s1)

# to remove

b={1,2,3,4,5}
b.remove(3)
print (b)

b.discard(2) #is the same job like remove but doesnot show error 
b.pop() #removes the last element)
b.clear()#removes all the elements)

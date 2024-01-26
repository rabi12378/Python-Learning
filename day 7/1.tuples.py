# jan 24
# tuples are also iteerables in python (like list,string and set
# tuples are also immutable data types
# tuple elemests are enclosed inside small brackts

# crearting tuples

a=()# empty tuple
b= tuple() # empty tuple
list(), set(), tuple(), dict(), int(), float(), bool(), str()  # these are the built-in functions for datatypes

c = (1, 2, 3)  # Non-empty tuple

# Elements can be of mixed dataype
d = (1, 2.1, "hello", [1, 2])


# Accessing tuple elements
# Tuple elements can also be accessed using Indexing and Slicing similar to list
vowels = ("a", "e", "i", "o", "u")
print(vowels[0])  # a
print(vowels[-1])  # u

print(vowels[:2])  # ("a", "e")
print(vowels[3:])  # ("o", "u")
print(vowels[4:2])  # ()
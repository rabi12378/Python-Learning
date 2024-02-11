# For reading binary 

import pickle 
with open ("day20/result.dat","rb") as fp:
    students = pickle.load(fp)

print(students)
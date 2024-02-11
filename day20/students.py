# For reading binary 

import pickle 
with open ("day20/result.dat","wb") as fp:
    students = pickle.dump(fp)

print(students)
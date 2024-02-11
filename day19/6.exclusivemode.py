# if a file is already created and we try to open the file in exclusive mode then it raises error

with open ("day19/messg.txt","x") as fp :
    fp.write=("hello")
    content=fp.write
print(content)
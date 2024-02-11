# read() ad write()
filename="day20/info.txt"
with open (filename,"w") as fp:
    fp.write("heloo world \n i am rabi uhu")

with open (filename,"r") as fp:
    print(fp.readline())
    fp.seek(0)
    print(fp.readlines())
    print(fp.tell())


data = ['heloo world \n', ' i am rabi and high level language']
with open (filename,"w") as fp :
    fp.writelines(data)
a=open("day19/message.txt","r")
content= a.read()
a.close()
print(content)
a=open("day19/message.txt","r")
try:
    content=a.read()
except:
    print("something wenrt wrong")
else:
    print(content)
finally:
    a.close()





with open("day19/message.txt","w+") as fp:
    fp.write("hello world")
    fp.seek(0)
    content=fp.read()
print(content)
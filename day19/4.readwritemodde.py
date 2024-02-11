with open ("day19/message.txt","r+") as fp:
    content=fp.read()
    new_content=content[1:8]
    fp.seek(0)
    fp.write(new_content)

print("succesfull")
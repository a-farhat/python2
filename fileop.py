filetxt = open("C:/Users/AhmadFarhat/Documents/python/file.txt",'r')
fileoutxt = open("C:/Users/AhmadFarhat/Documents/python/fileupper.txt",'w')
fileoutread = open("C:/Users/AhmadFarhat/Documents/python/fileupper.txt",'r')

print(filetxt.readable())
print(fileoutread.readable())
#print (filetxt.readlines())
#print (filetxt.readlines())

for lines in filetxt.readlines():
    print(lines)
    fileoutxt.write(lines.upper())

fileoutxt.close()

for lines2 in fileoutread.readlines():
    print(lines2)


filetxt.close()

fileoutread.close()



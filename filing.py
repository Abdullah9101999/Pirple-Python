countrynames=[]
for i in range(4):
    countryside=str(input("Enter name of countries:\n"))
    countrynames.append(countryside)
fileopen=open("info","w")
for countryside in countrynames:
    fileopen.write(countryside + " ")
fileopen.close()
fileopen=open("info","r")
fullfile=fileopen.readline()
print(fileopen)
import os
if (fileopen==True):
  os.remove("info")
else:
    fileopen=open("newfile","w")
    for countryside in countrynames:
        fileopen.write(countryside + " ")
print(fileopen)
fileopen.close()
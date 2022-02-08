f=open("question3.txt","r")
f1=open("delhi.txt","w")
f2=open("shimla.txt","w")
f3=open("other.txt","w")
file=f.read()
file_data=file.split("\n")
print(file_data)
i=0
while i<len(file_data):
    if "delhi" in file_data[i]:
        f1.write(file_data[i])
        f1.write("\n")
        print(f1)
    elif "shimla" in file_data[i]:
        f2.write(file_data[i])
        f2.write("\n")
        print(f2)
    else:
        f3.write(file_data[i])
        f3.write("\n")
        print(f3)
    i=i+1
f1.close()
f2.close()
f3.close()


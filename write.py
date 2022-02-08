# f=open("student.txt",mode="w")
# f.write("hello/n")
# f. write("chsndni/n")
# f. write("how are you")
# f.close()



fo=open("mssg.txt","w")
fo.write("my name is chandni\n i am in navgurukul banglore campus\n namste ")
fo.close()

fo=open('mssg.txt','r')
fi=open('writemssg.txt','w')
l=fo.readlines()
for i in l:
    if 'a' in i:
        i=i.replace('a','')
        fi.write(i)
fi.close()
fo.close()




# f=open("sharma.txt",'r')
# file=f.read()
# data=file.split()
# count=0
# i=0
# while i<len(data):
#     if 'ing' in data[i]:
#         count=count+1
#     i=i+1
# print(count)



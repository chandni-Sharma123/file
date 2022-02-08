
fo=open("mssg.txt","w")
fo.write(" chandni sharma\n")
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




# file = open("sharma.txt", "rt")
# data = file.read()
# words = data.split()

# print('Number of words in text file :', len(words))
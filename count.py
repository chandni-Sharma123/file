def count ():
    f=open("mssg.txt",'r')
    data=f.read()
    word=data. split()
    for i in word:
        if i=='chandni' or i =='to':
            print(i)

        f.close()
count()

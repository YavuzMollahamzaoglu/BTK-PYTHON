with open('deneme.txt') as f:
    icerik = f.read(15)
    print(icerik)




'''with open('deneme.txt') as f:
    satir = f.readline()
    print(satir)
    satir = f.readline()
    print(satir)
    satir = f.readline()
    print(satir,end='')
    f.seek(0)
    satir = f.readline()
    print(satir,end='')'''

'''with open('deneme.txt') as f:
    icerik = f.readlines()
    print(icerik)
    for satir in icerik:
        print(satir,end='-')'''


'''f = open('deneme.txt','r')
icerik = f.read()
print(icerik)
f.close()'''
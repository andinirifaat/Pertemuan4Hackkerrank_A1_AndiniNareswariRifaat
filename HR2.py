angka=list(map(int, input().split()))


if angka[0]>angka[1] and angka[0]>angka[2] : 
        if angka[1]>angka[2]:
                print(angka[2],angka[1],angka[0])
        else:
                print(angka[1],angka[2],angka[0])
elif angka[1]>angka[0] and angka[1]>angka[2]  :
        if angka[0]>angka[2]:
                print(angka[2],angka[0],angka[1])
        else:
                print(angka[0],angka[2],angka[1])
else :
        if angka[1]>angka[0]:
                print(angka[0],angka[1],angka[2])
        else:
                print(angka[1],angka[0],angka[2])

bil = int(input())

if bil > 1:
    for i in range(2, bil//2):
        if (bil % i) == 0:
            print("Bukan bilangan prima")
            break
    else:
        print("Bilangan prima")
else:
    print( "Bukan bilangan prima")
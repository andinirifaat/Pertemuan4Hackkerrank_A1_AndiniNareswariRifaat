usia=int(input())

if usia >= 18:
    print("Anda dewasa")
elif 13 <= usia < 18:
    print("Anda remaja")
elif usia < 13:
    print("Anda anak-anak")
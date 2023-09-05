s = input()
s = s.replace(" ", "").lower()

a=''.join(reversed(s))
if s == a:
    print("Palindrom")
else:
    print("Bukan palindrom")
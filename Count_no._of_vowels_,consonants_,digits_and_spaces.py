s = input()
s = s.lower()
l = len(s)
vcount = 0
dcount = 0
scount = 0
for ch in s:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        vcount = vcount+1
    elif ch.isnumeric():
        dcount = dcount+1
    elif ch.isspace():
        scount = scount+1
ccount = l - vcount - dcount - scount
print("Vowels: "+str(vcount))
print("Consonants: "+str(ccount))
print("Digits: "+str(dcount))
print("White spaces: "+str(scount))
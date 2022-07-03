s = input()
s = s.lower()
count = 0
for i in s:
    if i.isdigit():
        count = count+1
if count>0:
    print("Contains " + str(count) + " digit") 
else:
    print("Doesn't contain digit")
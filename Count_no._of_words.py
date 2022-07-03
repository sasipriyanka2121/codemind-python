string = input()
total = 1
for i in range(len(string)):
    if(string[i] == ' ' or string ==' ' or string == '	'):
        total = total+1
print(total)
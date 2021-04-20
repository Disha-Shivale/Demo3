#While loop
i = 1
while(i <= 10):
    print("Number ", i)
    i += 1

#BREAK
i = 1
print()
while(i <= 10):
    print("Number ", i)
    if(i == 5):
        break
    i += 1

#Continue
i = 1
print()
while(i <=10):
    print("Number ", i)
    i += 1
    if (i == 5):
        continue
    print("Number ", i)


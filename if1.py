#IF Statement
i = 50
j = 20
if i > j:
    print("I is greater")
    print()

#ELIF Statement
i = 10
j = 20
if i > j:
    print("I is greater")
elif i < j:
    print("J is greater")
    print()


#IF ELSE
i = 10
j = 10
if i > j:
    print("I is greater")
elif i < j:
    print("J is greater")
else:
    print("No Value match")

#Same link execute
i = 20
j = 10
print()
if i > j: print("I is greater")

#One line IF ELSE Statement
i = 20
j = 30
print()
print("I is greater") if i > j else print("J is greater")

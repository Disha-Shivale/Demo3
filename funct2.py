#Default parameter value
def showMessage(name='Default name', age=30):
    print("Your name is " + name + " Age is ", age)
print("Call function by its name")
showMessage()
print()

#Pass one parameter
def showMessage(name='Default name'):
    print("Your name is " + name)
print("Call function by its name")
showMessage()
print()

#Passing a list as an argument
def showList(lang):
    for x in lang:
        print(x)
lang = ["HTML", "CSS", "Bootstrap", "Java"]
showList(lang)
print()

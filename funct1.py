#Function
def showMessage():
    print("This is function")
    print("Hello from Python")
print("Call function by its name")
showMessage()
print()

#Function Parameter
def showMessage(name):
    print("Your name is " + name)
print("Call function by its name")
showMessage('John')
print()

#2 Parameter in Function
def showMessage(name, age):
    print("Your name is " + name + " Age is ", age)
print("Call function by its name")
showMessage('John', 30)
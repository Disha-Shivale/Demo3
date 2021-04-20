#Create class object
class FirstClass:
    i = 20
    j = 10
demo1 = FirstClass()
print("Value from Class", demo1.i)
print("Value from Class" ,demo1.j)
print()

#Method in class
class User:
    def method1(self):
        print("This is method one")

    def method2(self):
        print("This is method two")
user = User()
user.method1()
user.method2()
print()




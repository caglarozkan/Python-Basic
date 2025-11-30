x=20
def multiply(num):
    x=5     #inner scpoe
    print("x is",x,"in function")
    return num*x
print("x is",x,"in global")
print(multiply(100))

print("--------")
#GLOBAL
my_name="Caglar"

def func1():
    #ENCLOSING
    my_name="Caglar 2"
    print(my_name)
    def func2():
        #LOCAL
        my_name="Caglar 3"
        print(my_name)
    func2()

print(my_name)
func1()
print("-------")

y = 10
def changeY():
    global y
    y=5
    print("in func",y)
print("before func",y)
changeY()
print("after func",y)
#FUNCTIONS

my_name="caglar"
my_name.upper() #bu satırlık degiştirir ilerisi için etilenmez
print(my_name)
print(my_name.upper())

my_name=my_name.upper()
print(my_name)

def welcome(name, surname="Ozkan"):  #bu şekilde de default atama yapabiliriz
    print("Welcome",name,surname)

welcome(my_name)

print("-------")
def square(num):
    area=num*num
    return area #it returns a return value

edge=int(input("Enter the edge value:"))
x=square(edge)
print("Area of x is",x)

print("-----------")

def args_sum(*args):
    return sum(args)

x=args_sum(10,20,30)
print(x)

def kwargs_exp(**kwargs):
    print(kwargs)
    if "apple" in kwargs:
        print("appleeeee")
    else:
        print("no apple")
kwargs_exp(apple=100,banana=15)  #dictionary oluşturur bu şekilde de


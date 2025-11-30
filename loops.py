my_list=[10,20,43,67,3,87,23,765,12312]

for i in my_list:
    if i%6==0:
        print(i)
print("loop ended")

my_string="Caglar Ozkan"
for c in my_string:
    print(c) 
print("--------")

my_new_list=[("a","b"),("c","d"),("e","f"),("g","h"),]
for element in my_new_list:
    print(element)
print("len is",len(my_new_list))

#tuple unpacking
for (x,y) in my_new_list:
    print(y)
print("--------------")
my_dict={"k1":100,"k2":200,"k3":300}
for element in my_dict:
    print(element)

print("-------")

for i in range(0,100,3):
    if i>50 and i<60:
        continue
    print(i)
    if i==93:
        break

last_list=[10,20,30,40,50]

while 20 in last_list:
    if last_list[-1]!=20:
        print("20 is in last list")
    last_list.pop()

my_list=[10,20,30]
print(f"my list is: {my_list}") # formatlı yazma
print("-------------")
enumerate_list=[123,435,635,214,76,23,7,54,327,641]
for i in enumerate(enumerate_list): #ilk girilen indexi ikinci girilen sey de value su
    print(i)

for (ix,value) in enumerate(enumerate_list):
    if value>=100:
        print(ix,value)

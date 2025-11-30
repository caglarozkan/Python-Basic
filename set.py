#set elements  are uniqe and unordered

mylist=[10,20,30,10,40,40,50,20,30]
print(len(mylist))

myset=set(mylist)
print(myset)
print(len(myset))

myset.add(10)
print(myset)

myset2={30,40,50,60,70}
print(myset.union(myset2))
print(myset)

print(myset.intersection(myset2))

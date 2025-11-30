#immutable elements

mytuple=("10",20,30,"40")

print(mytuple[0])

#mytuple[0]= 100 X the elements arre immutable so need create a new tuple
mytuple=(100,mytuple[1],mytuple[2],mytuple[3])

print(mytuple.index(100))
print(mytuple.count("40"))

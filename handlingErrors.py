
while True:
    try:
        myAge=int(input("Enter age:"))
        print(myAge*2)
        break
    except:
        print("Enter the AGEEEE!!!")
    finally: # her türlü çalışır
        print("finally...\n")
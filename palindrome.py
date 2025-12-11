def palindrome(num):
    reversed_num=0
    original_num=num
    while(num>0):
        digit=num%10
        reversed_num=reversed_num*10+digit
        num=num//10
    return reversed_num ==original_num

print(palindrome(8))
print(palindrome(999))
print(palindrome(101))
print(palindrome(1043232421))
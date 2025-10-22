a = input("Enter the string : ")
b = ""

for i in range(len(a)-1,-1,-1):
    b = b + a[i]

if(b == a):
    print(f'{a} is a palindrome')
else:
    print("Not a palindrome!")
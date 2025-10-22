# # def greet(name):
# #     print(f"Hello {name}, This is a greet functions!")

# # greet("Shubham")




# def sum(num1, num2):
#     print(f"Sum of {num1} and {num2} = {num1+num2}")

# sum(5,6)





# def checkPalin(num):
#     rev = 0
#     copy = num
#     while num > 0:
#         rev = rev*10 + num%10
#         num = num//10
    
#     if(rev == copy):
#         print("Palindrome")
#     else:
#         print("Not a palindrome")

# checkPalin(122)






def checkPalind(st):
    rev = ""
    for i in range(len(st)-1, -1, -1):
        rev = rev + st[i]

    if rev == st:
        print("Palindrome")
    else:
        print("Not a palindrome")

checkPalind("NAMAN")
checkPalind("NAM")
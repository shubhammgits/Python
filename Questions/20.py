str = input("Enter any string : ")
b = ""
for i in range(len(str)-1,-1,-1):
    b = b + str[i]

print(b )
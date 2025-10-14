gender = input("Enter your gender (M or F): ")

print(type(gender))

if(gender == 'M' or gender=='m'):
    print('Good Morning Sir!')
elif(gender == 'F' or gender =='f'):
    print('Good Morning Mam!')
else:
    print('Unindentified Gender!')

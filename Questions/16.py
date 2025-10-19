n = int(input("Enter any number :"))
evenSum = 0
oddSum = 0
for i in range(n+1):
    if(i%2==0):
        evenSum += i
        
    else:
        oddSum += i
        

print(f'Sum of even numbers in between 1 to {n} = {evenSum}')
print(f'Sum of odd numbers in between 1 to {n} = {oddSum}')
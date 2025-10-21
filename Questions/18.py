n = int(input("Enter the number :"))
factSum = 0
for i in range(1,n):
    if(n%i == 0):
        factSum = factSum + i
    
if(factSum == n):
    print(f'{n} is a perfect number!')
else:
    print(f'{n} is not a perfect number!')
n = int(input("Enter a number : "))


for i in range(n+1):
    if(n%i == 0):
        print(f'Factor of {n} = {i}')
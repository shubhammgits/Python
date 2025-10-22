str = "shui78@nkj(7KJB)jkasd^#"
dig = 0
char = 0
spchr = 0

for i in str:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        spchr += 1

print(f'Total Digits = {dig}')
print(f'Total Characters = {char}')
print(f'Total Special Symbols = {spchr}')
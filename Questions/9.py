temp = int(input("Enter the temprature in degree Celcius: "))

if(temp<0):
    print("Freezing Cold!")

elif(0<temp and temp<10):
    print("Very Cold!")

elif(10<temp and temp<20):
    print("Cold!")

elif(20<temp and temp<30):
    print("Pleasant!")

elif(30<temp and temp<40):
    print("Hot!")

elif(temp>40):
    print("Very Hot!")
x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))

if(x > 0 and y > 0):
    print("first quadrant");
elif(x < 0 and y > 0):
    print("second quadrant");
elif(x < 0 and y < 0):
    print("third quadrant");
elif(x > 0 and y < 0):
    print("fourth quadrant");
elif(x == 0 and y == 0):
    print("origin");
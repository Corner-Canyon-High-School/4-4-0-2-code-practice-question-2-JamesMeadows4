r = int(input("Enter the red: "))
g = int(input("Enter the green: "))
b = int(input("Enter the blue: "))
if r > 255 or g > 255 or b > 255 or r < 0 or g < 0 or b < 0:
    if r > 255 or r < 0:
        print("Red number is not correct")
    if g > 255 or g < 0:
        print("Green number is not correct")
    if b > 255 or b < 0:
        print("Blue number is not correct")
else:
    print("No problems found!")

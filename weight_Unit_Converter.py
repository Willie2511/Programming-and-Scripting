# This is a program which will ask a user to input their weight
# It will then ask if the unit is lbs or kg
# It will then convert the weight into another unit


w = int(input("Please Enter Weight: "))
k = input(str("L(bs) or K(g): "))
if k.upper() == "L":
    converted = w * 0.45
    print (f"You are {converted} Kilos")
else:
    converted = w / 0.45
    print (f"You are {converted} Pounds")


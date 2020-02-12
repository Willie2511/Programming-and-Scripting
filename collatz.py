n = int(input("Please enter a positive integer: "))

while n != 1: 
    
    if int (n) % 2 != 0:
        n = int(n*3)+1
    else:
        n = int(n)/2
    print(n)
print("Finished")
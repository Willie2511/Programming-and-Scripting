#check if a number is prime
#the primes are 2, 3, 5, 7, 11, 13, ...

p = 13 * 17
m = 2

while m < p:
    if p % m == 0:
        print(m, "divides", p, "and therefore", p, "is not prime.")
     m = m + 1

print("Thank you for running my program.")
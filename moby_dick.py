letters = 'e'
k = 0

with open('/Users/Willie/Desktop/moby_dick.txt', 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter == letters):
                    k= k+1
print(k) 


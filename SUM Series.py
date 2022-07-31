# Phol Siphai
# Write a Python python program to calculate the sequence of 2/9 - 5/13 + 8/17....
n = 2 
d = 9
p = 1
N = int(input("Enter the number that you want to find the sum of them :"))
sum = 0
for i in range(N) : # i in range (3) because of this series have only tree term
    x = n/d
    sum += x*p
    n += 3
    d += 4
    p *= -1
print("The Sum of this sequence is =", sum)

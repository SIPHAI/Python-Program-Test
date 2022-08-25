# Phol Siphai
# Write a Python python program to calculate the sequence of 2/9 - 5/13 + 8/17....
Top = 2 #this is the top of the sequence
Bottom = 9 # The Bottom of the sequence
power = 1 #The power
N = int(input("How many number you want to calculate :"))
sum = 0
for i in range(N) : # i in range (N) because of this series have 
    x = Top/Bottom #the first sequnce 2/9
    sum += x*power
    Top += 3 # always plus 3 for the next top
    Bottom += 4 #always plus 4 for the next bottom
    power *= -1 #to change from minus to plus and plus to minus again again
print("The Sum of this sequence is =", sum)

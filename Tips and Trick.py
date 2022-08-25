lower = 1
upper = 100
numbers = int(input("Enter any numbers:"))
for number in range (lower,upper):
    even_numbers = [number for number in numbers if number % 2 == 0]
    Odd_numbers = [number for number in numbers if number % 2 != 0]
print(even_numbers)  # [2, 4, 6, 8]
print(Odd_numbers) # [1,3,5,7]
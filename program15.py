# Date: 18/11/2025
# Program Number: 15
# Program: Convert odd numbers in a list to even by adding 1.
numbers = [3, 7, 8, 12, 15, 21, 26]
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] += 1
print("List after converting odd numbers to even:", numbers)
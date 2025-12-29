# Date: 28/10/2025
# Program Number: 03
# Program: To calculate Sum and Average of N numbers.
N = int(input("Enter the number: "))
totalNo = N
sum = 0
while N >= 0:
    sum += N
    N -= 1
average = sum / totalNo
print("Sum =", sum)
print("Average =", average)
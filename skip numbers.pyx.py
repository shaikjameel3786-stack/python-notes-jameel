#numbers

numbers = [-10, -3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    # Skip negative numbers
    if num < 0:
        continue
    # Skip multiples of 3
    if num % 3 == 0:
        continue
    print(num)
    
#1

with open("students.txt", "w") as file:
    for i in range(5):
        name = input(f"Enter name of student {i+1}: ")
        file.write(name + "\n") 

print("Names have been written to students.txt successfully!")

#2
import os
file_name = input("Enter the file name: ")
if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        print("File exists! Contents are:\n")
        print(file.read())
else:
    print("File does not exist!")


#3
with open("student.txt", "w") as file:
    file.write("Your Name") 
print("Name written to student.txt successfully!")

#4
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
my_list = [10, 20, 30, 40]
print("Sum of list elements:", sum_of_list(my_list))

#5
arr = [10, 20, 30, 40, 50]
total_sum = sum(arr)
average = total_sum / len(arr)
print("Array elements:", arr)
print("Sum of elements:", total_sum)
print("Average of elements:", average)

#6
marks = float(input("Enter the student's marks (out of 100): "))
if marks >= 40:
    print("Result: PASS *")
elif marks < 40:
    print("Result: FAIL $")
else:
    print("Invalid input! Please enter marks between 0 and 100.")


#7
my_list = [10, 20, 30, 40, 50]
element = int(input("Enter the element to search: "))
if element in my_list:
    print(f"{element} is present in the list.")
elif element not in my_list:
    print(f"{element} is not present in the list.")
 












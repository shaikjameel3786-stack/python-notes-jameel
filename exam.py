#1
a=int(input("enter your num a:" ))
b=int(input("enter your num b:"))
print(a+b)
print(a-b)
print









#3
# Program to check if two numbers are equal

# Taking input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Using comparison operator ==
if num1 == num2:
    print("# The numbers are equal.")
else:
    print("* The numbers are not equal.")


#4
def reverse_array(arr):
    # Two-pointer approach
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements at left and right
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

# Example usage
array = [1, 2, 3, 4, 5]
print("Original array:", array)
reversed_array = reverse_array(array)
print("Reversed array:", reversed_array) 



#5
# Program to find sum and average of array elements

# Example array
arr = [10, 20, 30, 40, 50]

# Calculate sum
total_sum = sum(arr)

# Calculate average
average = total_sum / len(arr) if len(arr) > 0 else 0

print("Array elements:", arr)
print("Sum of elements:", total_sum)
print("Average of elements:", average)

#6
import numpy as np

# Create a 1D numpy array
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array into 2D 
reshaped_arr = arr.reshape(2, 3)

print("Original 1D array:")
print(arr)

print("\nReshaped 2D array:")
print(reshaped_arr)

#7
import numpy as np
# Define two matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Multiply the matrices
result = np.dot(A, B) # or A @ B

# Display the result
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nProduct of A and B:")
print(result)

  




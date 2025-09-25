#1
n1=int(input("enter first number"))
n2=int(input("enter second number"))
def mul_numbers(a,b):
   result=mul_numbers(n1,n2)
   print(result)



   #2
number=int(input("enter number"))
def is_even(num):
   if num%2==0:
      print("even")
   else:
      print("odd")
      is_even(num)


#3
n1=int(input("enter number"))
def factorial(n):
   result=1
   for i in range(1,n+1):
      result*=i
      return result
      print(factorial(n1))

#4
n1=int(input("enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
def largest_of_three(a,b,c):
   if a>=b and a>=c:
      return a
   elif b>=a and b>=c:
      return b
   else:
      return c
print(largest_of_three(n1,n2,n3))


#5
str=input("enter string")
def reverse_string(s):
   return s[::-1]
print(reverse_string(str))

#6
def count_vowels(word):
   vowels="aeiouAEIOU"
   count=0
   for char in word:
      if char in vowels:
         count+=1
   return count
print(count_vowels("programing"))

# 7
import array as arr
a=arr.arr('i',[1,2,4])
b=arr.arr('i',[2,3,5])
result=arr.arr('i',[a.b])
print(result)
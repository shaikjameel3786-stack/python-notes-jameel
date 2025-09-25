#beak
from tkinter import TRUE


for number in range(1,10):
 if number==5:
  print("breaking the loop at number 5")
  break
 print("number:",number)



# for numbers 
numbers=[1,3,5,10,7,9,8]
for num in numbers:
    if num%2==0:
          print("first even number found:",num)
          break
else:
   print("no even number found")

#user input simulation

while True:
   user_input=input("enter'jameel' to stop: ")
   if user_input =='jameel':
      print("logined")
      break
   else:
      print("try again")




      #continue
   for number in range(1,2,3,4,5,6,7,4,6,7,8):
           for i in list:
               if i%3==0:
                   print("skippimg num:3")
                   continue
               print(i)



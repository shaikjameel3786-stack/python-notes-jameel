#functions

def greet():
    print("welcome to python function!")
    greet()

     
# passing parameters and arguments
def greet_user (name):
    print("hello,",name)
#calling function with argument
greet_user("ram")

#function argument types:
#a:-positional arguments
def add(a,b):
    print("sum is;",a+b)
    add(5,10)

 #key word arguments
def introduce(name,age):
    print(f"my name is {name} and iam{age}years old")
introduce(age=20,name="jammu")

    #default arguments
def greet(name="guest"):
    print("hello,",name)
greet("ram")


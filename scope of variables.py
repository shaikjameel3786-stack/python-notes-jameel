#global
x=100
def func():
    # local variable
    y=50
    print("inside function,x=",x) 
    print("inside function,y=",y) 
    print("outside function,x=",x)
    print(y)
func()




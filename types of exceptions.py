# handling  zero division error
try:
	result = 10 / 0
except ZeroDivisionError:
	print("Cannot divide by zero.")
finally:
	print("program ended")
	 


#2 multiple execeptions
try:
	num = int("abc")
	result = 10 / 0
except ValueError:
	print("invalid number")
except ZeroDivisionError:
	print(" Cannot divide by zero")
finally:
	print("done")
	
# catch my exceptions
try:
	f=open ("data.txt")
except Exception as e:
	print("error:",e)
finally:
	print(" file handling attempted")
	









    
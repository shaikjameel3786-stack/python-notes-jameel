#writing a data to a file
f=open("data.txt","w")
f.write("hello,python!/n")
f.close()

#write line():-
f=open("data.txt","w")
f.writelines(["line 1/n","line 2/n","line 3/n"])
f.close()

#reading data from a file
# read()
f=open("data.txt","r")
print(f.readline())
print(f.read(5))
f.close()

#readline():-
f=open("data.txt","r")
print(f.readline())
print(f.readline())
f.close()

#read lines():-
f=open("data.txt","r")
lines=f.readlines()
print (lines)
f.close()


#random access file operations
# tell(seek)():-
f=open("data.txt","r")
print(f.read(5))
print("pointer at:",f.tell())
f.seek(0)
print(f.read(5))
f.close()











  
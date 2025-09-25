#type conversions

#list-tuple
my_list=[1,2,3,4]
my_tuple=tuple(my_list)
print (my_tuple)
print (type(my_tuple))

#tuple_list
my_list=[5,6,7]
my_set=set(my_list)
print(my_set)
print(type(my_set))

#list-set(remove duplicates)
my_list=[1,2,2,3,3,4]
my_set=set(my_list)
print(my_set)
print(type(my_set))


#set-list
my_set={10,20,30}
my_list=list(my_set)
print(my_list)
print(type(my_list))


#dictionary-list of keys
student={'name':'jammu','age':'19','grade':'A'}
keys_list=list(student.keys())
print(keys_list)


#dictionary-list of values
student={'name':'jammu','age':'19','grade':'A'}
values_list=list(student.values())
print(values_list)

#dictionary-list ofitems(tuples of key value pairs)
student={'name':'jammu','age':'19'}
items_list=list(student.items())
print(items_list)
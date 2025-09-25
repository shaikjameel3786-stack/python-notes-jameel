# with looping
import array
a=array.array('i',[1,2,3])
b=array.array('i',[4,5,6])
result =array.array('i',[a[i] + b[i] for i in range(len(a))])
print(result)


# vectorized
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
result=a+b
print(result)



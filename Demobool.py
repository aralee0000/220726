#Demobool.py
#얕은복사
a=[1,2,3]
b = a
a[0] =38
print(a)
print(b)
print(id(a), id(b))

print("---깊은복사---")
a=[1,2,3]
b=a[:]
a[0]=38
print(a)
print(b)
print(id(a), id(b))

#다른형식이라면
import copy
a=[100,200,300]
b=copy.deepcopy(a)
a[0]=101
print(a)
print(b)
print(id(a),id(b))


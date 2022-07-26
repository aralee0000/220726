Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=100
>>> y=3.14
>>> starA="python"
>>> strB="파이썬"
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'starA', 'strB', 'x', 'y']
>>> type(x)
<class 'int'>
>>> typc(y)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    typc(y)
NameError: name 'typc' is not defined
>>> type(y)
<class 'float'>
>>> type(strA)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type(strA)
NameError: name 'strA' is not defined
>>> type(strA)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    type(strA)
NameError: name 'strA' is not defined
>>> len(starA)
6
>>> len(strB)
3
>>> strC=""""이문자열은
다중라인을
저장합니다."""
>>> strC
'"이문자열은\n다중라인을\n저장합니다.'
>>> printstrC)
SyntaxError: unmatched ')'
>>> print(strC)
"이문자열은
다중라인을
저장합니다.
>>> strA[1]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    strA[1]
NameError: name 'strA' is not defined
>>> strA[0]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    strA[0]
NameError: name 'strA' is not defined
>>> starA[0]
'p'
>>> strB[1]
'이'
>>> 
>>> starA[1]
'y'
>>> starA[0:3]
'pyt'
>>> starA[:3]
'pyt'
>>> starB[0:3]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    starB[0:3]
NameError: name 'starB' is not defined
>>> strb[:5]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    strb[:5]
NameError: name 'strb' is not defined
>>> 
>>> strB[:5]
'파이썬'
>>> strD="pthon is very powerful"
>>> len(strD)
22
>>> strD[0:6]
'pthon '
>>> strD[-1]
'l'
>>> str[-3:]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    str[-3:]
TypeError: 'type' object is not subscriptable
>>> strD[-3"]
     
SyntaxError: EOL while scanning string literal
>>> strD[-3:]
'ful'
>>> colors=["red","blue","green"]
>>> type(colors)
<class 'list'>
>>> len(colors)
3
>>> colors[0]
'red'
>>> colors.append("white")
>>> colors
['red', 'blue', 'green', 'white']
>>> colors.append("pink")
>>> colors
['red', 'blue', 'green', 'white', 'pink']
>>> colors.insert(1, "black")
>>> colors
['red', 'black', 'blue', 'green', 'white', 'pink']
>>> colors.index("black")
1
>>> colors.index("black")
1
>>> 
>>> colors.index("black")
1
>>> colors +=["red"]
>>> colors
['red', 'black', 'blue', 'green', 'white', 'pink', 'red']
>>> colors.pop()
'red'
>>> colors
['red', 'black', 'blue', 'green', 'white', 'pink']
>>> colos.remove("black"09
	     
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 
>>> colos.remove("black")
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    colos.remove("black")
NameError: name 'colos' is not defined
>>> colos.remove("red")
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    colos.remove("red")
NameError: name 'colos' is not defined
>>> colors
['red', 'black', 'blue', 'green', 'white', 'pink']
>>> colors.count
<built-in method count of list object at 0x000002698752BD80>
>>> colors.count("red")
1
>>> colors.count(red)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    colors.count(red)
NameError: name 'red' is not defined
>>> colors.count("red")
1
>>> a={1,2,3,4}
>>> b={3,4,4,5}
>>> a
{1, 2, 3, 4}
>>> a={1,2,3,3}
>>> a
{1, 2, 3}
>>> b
{3, 4, 5}
>>> type{a
     
SyntaxError: invalid syntax
>>> }
SyntaxError: unmatched '}'
>>> type{a}
SyntaxError: invalid syntax
>>> type(a)
<class 'set'>
>>> a,union(b)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a,union(b)
NameError: name 'union' is not defined
>>> a.untion(b)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.untion(b)
AttributeError: 'set' object has no attribute 'untion'
>>> a | b
{1, 2, 3, 4, 5}
>>> a-b
{1, 2}
>>> tp=(1,2,3)
>>> tp
(1, 2, 3)
>>> len(tp)
3
>>> tp.index
<built-in method index of tuple object at 0x000002698754E400>
>>> tp[1]
2
>>> def times(a,b):
	return a*b, ab+b

>>> 
>>> 
>>> result =timse(2,3)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    result =timse(2,3)
NameError: name 'timse' is not defined
>>> result = timse(2,3)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    result = timse(2,3)
NameError: name 'timse' is not defined
>>> result
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    result
NameError: name 'result' is not defined
>>> def times(a,b):
	return a*b, a+b

>>> 
>>> 
>>> 
>>> result = times(2,3)
>>> result
(6, 5)
>>> resulr[0]
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    resulr[0]
NameError: name 'resulr' is not defined
>>> result[0]
6
>>> print("id:%s, name:%s" % ("kim", "김유신"))
id:kim, name:김유신
>>> printt
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    printt
NameError: name 'printt' is not defined
>>> print
<built-in function print>
>>> print("id:%s, name:%s" % ("kim", "김유신"))
id:kim, name:김유신
>>> a=set((1,2,3))
>>> a
{1, 2, 3}
>>> b=[list(a)
   b
   
SyntaxError: invalid syntax
>>> type(b)
<class 'set'>
>>> b = list(a)
>>> b
[1, 2, 3]
>>> type(b)
<class 'list'>
>>> b.append(4)
>>> b
[1, 2, 3, 4]
>>> 
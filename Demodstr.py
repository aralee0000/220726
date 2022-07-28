#Demodstr.py
#print(dir())

strA= "Python is very powerful"
strB= "파이썬은 강력해"
print(len(strA))
print(len(strB))

print(strA.upper())

#고객명단
names = ["전우치", "이순신", "김유식"]
for name in names:
    print("안녕하세요 {0}님 더운 여름입니다.".format(name))
    print("="*40)


u="<<< spam and ham >>>"
result = u.strip("<>")
print(u)
print(result)
result =result.replace("spam", "spam egg")
print(result)
lst=result.split()
print(lst)
print(":)".join(lst))

print("mbc2580".isalnum())
print("mbc:2580".isalnum())
print("mbc2580".isdecimal())
print("2580".isdecimal())





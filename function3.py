#function3.py
#기본값이 있는 경우
from tkinter.messagebox import RETRY


def times(a=10, b=20):
    return a*b
#호출
print(times())
print(times(5))
print(times(5,6))

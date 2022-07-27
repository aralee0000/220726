# 메모리관리.py 

class MyClass:
    #가장먼저 실행되는 초기화 루틴
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    #인스턴스를 파괴할때 가장 마지막에 실행 (소멸자)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성
d = MyClass(5)
#인스턴스 메모리 삭제
del d 

print("전체코드 실행종료")


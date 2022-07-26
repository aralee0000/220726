#class1.py
#1) 클래스 형식을 정의
class Person:
    #클래스 멤버 변수(클래스 자체에 추가-주로데이터공유)
    num_person =0
    #초기화 메서드
    def __init__(self):
        #소속이 인스턴스멤버 변수
        self.name = "default name"
        #소속이 클래스 멤버 변수
        Person.num_person += 1
    #인스턴스 메서드
    def print(self):
        print("my name is {0}".format(self.name))

#2) 인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person()
print("인스턴스개수:{0}".format(Person.num_person))







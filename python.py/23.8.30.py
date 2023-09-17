# class Test:
#     def __init__(self, name):
#         self.name = name
#         print("{} - 생성되었습니다".format(self.name))
#     def __del__(self):
#         print("{} - 파괴되었습니다".format(self.name))

# a = Test("A")
# b = Test("B")
# c = Test("C")



# import math

# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius

#     def get_curcumference(self):
#         return 2 ** math.pi * self.__radius
    
#     def get_area(self):
#         return math.pi * (self.__radius ** 2)
    
#     @property
#     def radius(self):
#         return self.__radius
    
#     @radius.setter
#     def set_radius(self, value):
#         if value <= 0:
#             raise TypeError("길이는 양의 숫자여야 합니다.")
#         self.__radius = value

# # print(circle.__radius) # 프라이빗 변수는 직접 호출이 안된다
# circle = Circle(10)
# # @데코레이터를 활용하여 직접 호출하는 것처럼 활용가능
# print("원래 원의 반지름", circle.radius)
# circle.radius = 2
# print("변경된 원의 반지름", circle.radius)
# print("원위 둘레: ", circle.get_curcumference())
# print("원위 넓이: ", circle.get_area())
# print(circle.get_radius())
# print(circle.set_radius(20))
# print("원의 둘레: ",circle.get_curcumference())
# print("원위 넓이: ",circle.get_area())



# class Parent:
#     def __init__(self):
#         self.value = "테스트"
#         print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")

#     def test(self):
#         print("Parent 클래스의 test() 메소드입니다.")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")

# child = Child()
# child.test()
# print(child.value)



# class CustomException(Exception):
#     def __init__(self, message, value):
#         Exception.__init__(self)
#         self.message = message
#         self.value = value
#     def __str__(self) -> str:
#         return self.message
    
#     def print(self):
#         print("##### 오류정보 #####")
#         print("메시지: ", self.message)
#         print("값: ", self.value)

# try:
#     raise CustomException("그냥", 273)
# except CustomException as e:
#     e.print()



# result1 = 0
# result2 = 2

# def adder1(num):
#     global result1
#     result1 += num
#     return result1

# def adder2(num):
#     global result2
#     result2 += num
#     return result2

# adder1(1)
# print(result1)
# adder2(3)
# print(result2)
# adder1(5)
# print(result1)
# adder2(9)
# print(result2)

# class Calculator:
#     def __init__(self):
#         self.result = 0
    
#     def adder(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# cal1.adder(3)
# cal2.adder(3)
# cal1.adder(5)
# cal2.adder(7)

# print(cal1.result)
# print(cal2.result)
    


# class Service:
#     def setname(self,name):
#         self.name = name

#     def sum(self,a,b):
#         result = a + b
#         print(f"{self.name}님 {a} + {b}는 {a+b}입니다.")

# pey = Service()
# pey.setname("홍길동")
# pey.sum(1,1)

# pal = Service()
# pal.setname("김홍균")
# pal.sum(3,5)



# class FourCal:
#     def setdata(self,first,second):
#         self.first = first
#         self.second = second

#     def sum(self):
#         result = self.first + self.second
#         return result
    
#     def mul(self):
#         result = self.first * self.second
#         return result
    
#     def sub(self):
#         result = self.first - self.second
#         return result

#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# b = FourCal()
# a.setdata(4,2)
# b.setdata(3,7)

# print(a.sum())
# print(a.mul())
# print(a.sub())
# print(a.div())
# print(b.sum())
# print(b.mul())
# print(b.sub())
# print(b.div())



# class HousePark:
#     lastname = "박"
#     def __init__(self,name):
#         self.fullname = self.lastname + name

#     def travel(self, where):
#         print(f"{self.fullname},{where}여행을 가다")
    
#     def love(self, other):
#         print(f"{self.fullname},{other.fullname} 사랑에 빠졌네")
    
#     def fight(self, other):
#         print(f"{self.fullname},{other.fullname} 싸우네")

#     def __add__(self, other):
#         print(f"{self.fullname},{other.fullname} 결혼했네")

#     def __sub__(self, other):
#         print(f"{self.fullname},{other.fullname} 이혼했네") 

# class Housekim(HousePark):
#     lastname = "김"
#     def traver(self, where, day):
#         print(f"{self.fullname},{where}여행 {day}가다")

# pey = HousePark("응용")
# juliet = Housekim("줄리엣")
# pey.travel("부산")
# juliet.travel("부산,3")
# pey.love(juliet)
# pey + juliet
# pey.fight(juliet)
# pey - juliet



# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)



# print(abs(-4))
# print(all([1,2,3]))
# print(all([1,2,3,0]))
# print(any([1,2,3,0]))
# print(any([0,""]))
# print(chr(97))
# print(chr(65))
# print(chr(48))



# for i, name in enumerate(['boy','foo','bar']):
#     print(i,name)



# print(eval("1+2"))
# print(eval('"hi"+"a"'))
# print(eval('divmod(4,3)'))



# def positive(x):
#     return x>0

# print(list(filter(positive,[1,-2,2,0,-5,6])))



# print(list(filter(lambda x:x>0,[1,-2,2,0,-5,6])))

# print(hex(234))
# print(hex(3))
# a = 3
# print(id(3))
# print(id(a))
# b = a
# print(id(b))



# class Person:
#     pass

# b = 3
# a = Person()
# print(isinstance(a,Person))

# sum = lambda a,b: a+b
# print(sum(3,4))

# myList = [lambda a,b:a+b,lambda a,b:a*b]

# print(myList[0](3,4))
# print(myList[1](3,4))

# def two_times(x):return x ** 2

# print(list(map(lambda a: a**2,[1,2,3,4])))

# def plus_one(x):
#     return x + 1

# print(list(map(plus_one,[1,2,3,4,5])))
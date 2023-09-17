# s = input("학점을 입력하세요> ")
# s = float(s)

# if s >=4.5:
#     print("신")
# elif s >= 4.2:
#     print("교수님의 사랑")
# elif s >= 3.5:
#     print("현 제체의 수호자")
# elif s >= 2.8:
#     print("일반인")
# elif s >= 2.3:
#     print("일탈을 꿈꾸는 소시민")
# elif s >= 1.75:
#     print("오락문화의 선구자")
# elif s >= 1.0:
#     print("불가촉천민")
# elif s >=0.5:
#     print("자벌레")
# elif s > 0:
#     print("플랑크톤")
# elif s == 0:
#     print("시대를 앞서가는 혁명의 씨앗")
# else:
#     print("Error")




# a = input("첫 번째 수를 입력하세요> ")
# b = input("두 번째 수를 입력하세요> ")
# c = input("세 번째 수를 입력하세요> ")
# a = int(a)
# b = int(b)
# c = int(c)

# if a > b:
#     if a > c:
#         print("가장 큰 수는 {}입니다.".format(a))
#     else:
#         print("가장 큰 수는 {}입니다.".format(c))
# else :
#     if b > c:
#         print("가장 큰 수는 {}입니다.".format(b))
#     else:
#         print("가장 큰 수는 {}입니다.".format(c))




# money = input("돈을 입력해 주세요> ")
# money = int(money)

# if money >=1000:
#     print("1번 코카콜라 1000원\n")
#     print("2번 환타 800원\n")
#     print("3번 사이다 900원\n")
#     print("4번 밀키스 700원\n")
#     print("5번 솔의눈 600원\n")
#     print("6번 삼다수 500원\n")


#     menu = input("음료를 선택해 주세요> ")
#     menu = int(menu)
#     if menu == 1:
#         if money >= 1000:
#             print("코카콜라를 선택하셨습니다.")
#             print("잔돈 {}원".format(money-1000))

#     elif menu ==2:
#         if money >= 800:
#             print("환타를 선택하셨습니다.")
#             print("잔돈 {}원".format(money-800))

#         if money >= 900:
#             print("사이다를 선택하셨습니다.")
#             print("잔돈 {}원".format(money-900))

#     elif menu ==4:
#         if money >= 700:
#             print("밀키스를 선택하셨습니다.")
#             print("잔돈 {}원".format(money-700))

#     elif menu ==5:
#         if money >= 600:
#             print("솔의눈를 선택하셨습니다.")
#             print("잔돈 {}원".format(money-600))

#     elif menu ==6:
#         if money >= 500:
#             print("삼다수를 선택하셨습니다.")
#             print("잔돈 {}원".format(money-500))
# else:
#     print("잔액이 부족합니다")




# number = input("정수 입력> ")
# number = int(number)

# if number > 0:
#     pass
# else:
#     pass




# str_input = input("태어난 해를 입력해 주세요> ")
# birth_year = int(str_input) % 12

# if birth_year == 0:
#     print("원숭이 띠 입니다.")
# elif birth_year == 1:
#     print("닭 띠 입니다.")
# elif birth_year == 2:
#     print("개 띠 입니다.")
# elif birth_year == 3:
#     print("돼지 띠 입니다.")
# elif birth_year == 4:
#     print("쥐 띠 입니다.")
# elif birth_year == 5:
#     print("소 띠 입니다.")
# elif birth_year == 6:
#     print("범 띠 입니다.")
# elif birth_year == 7:
#     print("토끼 띠 입니다.")
# elif birth_year == 8:
#     print("용 띠 입니다.")
# elif birth_year == 9:
#     print("뱀 띠 입니다.")
# elif birth_year == 10:
#     print("말 띠 입니다.")
# elif birth_year == 11:
#     print("양 띠 입니다.")




# list_a = [273, 32, 103, "문자열", True, False]

# print(list_a)
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])
# print(list_a[1:3])

# list_a[0] = 300
# print(list_a)
# print(list_a[0])

# print(list_a[3][1])



# list_a = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
# print(list_a[1])
# print(list_a[1][2])
# print(list_a[0][2])
# print(list_a[2][1])



# list_a = [1,2,3]
# list_b = [4,5,6]

# print("# 리스트")
# print("list_a =", list_a)
# print("list_b =", list_b)
# print()

# print("# 리스트 기본 연산자")
# print("list_a + list_b = ", list_a + list_b)
# print("list_a * 3", list_a * 3)
# print()

# print("# 길이 구하기")
# print("len(list_a)", len(list_a))



# list_a = [1,2,3]

# print("리스트 뒤에 요소 추가하기")
# list_a.append(4)
# list_a.append(5)

# print(list_a)
# print()
# print("리스트 중간에 요소 추가하기")
# list_a.insert(0,10)
# print(list_a)



# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print(f"나무를 {treeHit}번 찍었습니다.")
#     if treeHit == 10:
#         print("나무 넘어갑니다.")



# prompt = """
# ...1.Add
# ...2.Del
# ...3.List
# ...4.Quit
# ...
# ...Enter number:"""

# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())



# coffee = 10
# money = 300
# while money:
#     print("돈은 받았으니 커피를 줍니다.")
#     coffee = coffee -1
#     print(f"남은 커피의 양은 {coffee}개 입니다.")
#     if not coffee:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break



# coffee = 10
# while True:  
#     money = int(input("돈을 넣어 주세요:"))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee -1
        
#     elif money > 300:
#         print(f"거스름돈 {money-300}를 주고 커피를 줍니다.")
#         coffee = coffee -1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    
#         print(f"남은 커피의 양은 {coffee}개 입니다.") 

#     if not coffee:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break



# i = 1
# while i < 10:
#     print("2 * {} = {}".format(i, int(2) * int(i)))
#     i += 1


# 구구단 출력하기
# i = int(input("몇 단을 출력할까요?"))
# a = 1
# while a < 10:
#     print("{} * {} = {}".format(i, a, int(a) * int(i)))
#     a += 1



# import time 

# number = 0

# terget_tick = time.time() + 5
# while time.time() < terget_tick:
#     number += 1

# print("5초동안 {}번 반복했습니다.".format(terget_tick, number))



# i = 0

# while True:
#     print("{}번째 반복문입니다.".format(i))
#     i = i + 1
#     input_text = input("> 종료하시겠습니까(y):")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다.")
#         break



# i = 0
# while i < 10:
#     print("*"*i, end='')
#     print()
#     i += 1

# i = 10
# while i > 0:
#     print("*"*i, end='')
#     print()
#     i -=1
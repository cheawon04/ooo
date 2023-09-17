# print("우리집 강아지의 이름은 앙꼬에요")
# print("앙꼬는 2살이며, 장난감을 아주 좋아해요 ")
# print("앙꼬는 어른 일까요? True")

#19분 
# animal = "강아지"
# name = "앙꼬"
# age = 4
# hobby ="산책"
# is_adult = age>=2
# print("우리집"+animal+"의 이름은"+ name +"에요")
# print(name+"는"+str(age)+"살이며," +hobby+"을 아주 좋아해요")
# print(name+ "는 어른일까요?"+str(is_adult)) 


#우리집강아지의 이름은앙꼬에요
#앙꼬는4살이며,산책을 아주 좋아해요
#앙꼬는 어른일까요?True


# station="사당"
# print(station+"행 열차 입니다.")
# station="신도림"
# print(station+"행 열차 입니다.")

#29분 연산자
# print(1+1)
# print(3-2)
# print(2**3)
# print(5*2)
# print(6/3)
# print(5%3)# 나머지 
# print(10%3)# 1
# print(5//3)#몫
# print(10//3)#3

# print(10>3)#t
# print(4>=7)#f
# print(10<3)#f
# print(5<=5)#t
# print(3==3)#t
# print(3!=4)#t 3과4는 같지 않다
# print(not(3!=4)) #f
# print((3>0)and(3<5)) #t and는 둘중 하나라도 틀리면 false
# and=&임
 
#print((3>0)or(3>5)) #true or은 둘중 하나만 맞아도 true
#print ((3>0)|(3>5)) #true |도 둘중 하나만 만족 할시 true
#print(3<5<7) #true
#print(3>5>2) # false

#33분 간단한 식 곱,나누기 더하기 빼기등 순서로 진행
#print(3+2*2) #7
#print((3+2)*2) #10

# number=3+2*2 #7
# print(number) 
# number=number+7
# print(number) #14

# number +=2 #16 -= /= %= //= //는 1.5에서 1인정수만 씀
# number*=2 도 가능 
# print(number)

#35분 
# number=number+2 & number+=2 는 같은 식

#36분30초
#절대값 0의 기준 -2까지 갔으면 2간거니까 절댓값이 2인거 +2도 똑같음

# # abs=절댓값
# print(abs(-5)) #5

# #pow 제곱
# print(pow(4,2))  #pow는 4^2 4의 2승 (제곱) #16

# #max 입력받은 것에 제일큰것
# print(max(5,12)) #12

# # min 입력에서 가장 작은것 
# print(min(5,12)) #5

# #round 반올림 1~4 5~9
# print(round(3.14)) #3
# print(round(4.99))#5


#floor= 내림 ceil=올림 sqrt=제곱근 16이면 4
#from math import를 써야 쓸수 있음 #** 
# math 안에 있는 라이브러리를 모두 이용하겠다 라는 뜻
#random #randint이 쉬움 33분 정도


#from math import *
# print(floor(4.99)) #올림 .4
# print(ceil(3.14)) #내림 .4
#print(sqrt(16)) #제곱근 4

#random 랜덤 무작위로 뽑아주는
# from random import *
# print(random()) #0.0 ~ 1.0 까지 랜덤으로 임의의 값을 출력
# print(random() * 10 ) #0.0 ~ 10.0 까지 랜덤으로 임의의 값을 출력  # 위에 10을 곱 한것 
#소숫점 보기 싫을땐 int(정수)
# print(int(random()*10)) #0 ~ 10 미만의 임의의 값 생성

#0이 보기 싫을때

#from random import *
# print(int(random()*10)+1) #1~10이하의 임의의 값 생성
# print (int(random()* 45 )+1) # 1 ~ 45의 이하의  임의의 값 생성 *6문장을 쓰면 랜덤으로 6개 볼수 있음

# print( randrange (1,46)) # 1 ~ 45 미만 랜덤 생성 (-1하고)
#print(randint (1,45)) #1~45 랜덤
#print(randint (1,45)) #1~45 랜덤
#print(randint (1,45)) #1~45 랜덤
#print(randint (1,45)) #1~45 랜덤
#print(randint (1,45)) #1~45 랜덤

#45분 퀴즈

# from random import *
# date_1 = randint (4 , 28)

# print("오프라인 스터디 모임 날짜는 매월" +str(date_1)+"일로 선정 되었습나다.")
# print("온라인 스터디 머임 날짜는 매월" +str(date_1)+"일로 선정 되었습니다.") # 숫자 이기 때문에 str붙힘

#47분 문자열

# 앙꼬="귀여워"
# print(앙꼬)

#슬라이싱  #48분

#채원 = "040319 4777777"
# print("성별 :"+ 채원[7]) #0부터 세고 가지고 옥 싶은 숫자쓰기
# print("연도:"+채원[0:2]) #0~1까지 하고 싶으면 0:2로 +1
#print("생일:"+채원[:6]) # [:6]음 0~5까지 #ex [7:] 7부타 끝까지
#앞에서 세면  0 1 2 3 4 5 6 7 8 9
#뒤에서면 -1 -2 -3 -4 -5 -6 -7

#문자열 55분

# # lower
#python="PYTHON IS AMAZING"
# print(python.lower()) #lower 소문자
# print(python.upper()) #upper 대문자 
# print(python[0].isupper()) #0번째가 대문자인가? #true
#print(len(python)) #17 len문자 길이 "PYTHON IS AMAZING"
#print(python.replace("PYTHON", "Java")) # replace= PYTHON에서 Java로바꿈


# #58분 index
# python="PYTHON IS AMAZING"
# index=python.index("N")
# print(index) #index "N"이 몇번 째에 있는지
# index=python.index("N", index+1) #첫번째 "N"말고 두번째 "N" 볓번쨰인지  #15
# print(index) 
# print(python.find("N")) #index와 같이 "N"이 어디에 있는지
# #find는 "PYTHON IS AMAZING"에서 "java"인 다른것을 찾으면 -1이 나옴
# #index는 오류가 뜨고 귀에 print("hi")가 있더라도 출력이 안됨
# #find는 뒤어 print("hi")있으면 -1 ,hi 라고 출력됨

# print(python.count("N")) #count "N"이 몇개 있는지  #2


# 1:00 문자열 포멧 

# 방법1
# print("나는 %s살 입니다"%20) #나는 20살 입니다
# print("나는 %s색과 %s색을 좋아 한다." %("파란","빨간")) #나는 파란색과 빨간색을 좋아한다.
# print("Apple은 %c로 시작해요." % "A") #한글자 #Apple은 A로 시작해요

#방법2
#print("나는 {}살입니다.".format(20))
#print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간")) #나는 파란색과 빨간색을 좋아해요.
#print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간")) #나는 빨간색과 파란색을 좋아해요.

#방법3
#print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))  
#나는 20살이며, 빨간색을 좋아해요.

#방법4
# age=20
# color="빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.") #나는 20살이며, 빨간색을 좋아해요.


# 1:13
#  \\ 는 \
#print("c\\users") #c\users\

# #\n 줄바꿈
# print("바보 \n멍청이")

# # \", \' 는 문장에서 " , '
# print("저는\"인형\"이 좋습니다")  #저는 "인형"이 좋습니다

# # \r 뒤에있는것을 맨앞으로
# print("Red Apple \r pine")  #pineApple

# #\b 백스페이스 (한 글자 삭제)
#print("Redd\bApple") #RedApple

# #\t 탭
# print("Red\tApple") #Red     Apple

# # 퀴즈 1:16 ????/?
# url="http://naver.com"
# my_str =url.replace("http://","") 
# print(my_str) #naver.com
# my_str=my_str[:my_str.index(".")] 
# prirnt(my_str)

#리스트 []
# subway1 = 10
# subway2 = 20
# subway3 = 30
# subway = [10, 20, 30]
# print(subway)

# subway =["유재석", "조세호", "박명수"]
# print(subway)
# #조세호씨가 몇번째 칸에 타고 있는가?
# print(subway.index("조세호")) #1
#0,1,2 중 조세호 는 1번 에 타있음

#하하씨가 다음 정류장 에서 다음칸에 탐
# subway.append("하하") #append 뒤에 더하다
# print(subway)

# 정형돈 유재석 /조세호 사이에 태우기
# subway.insert(1, "정형돈") #1자리에 정형돈
# print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서꺼냄 #pop
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

#같은 이름의 사람이 몇명 있는지 확인
# subway.append("유재석") 
# print(subway)
# print(subway.count("유재석")) #count 똑같은게 몇개


#1:29
#정렬도 가능 #sort 정렬 한다는 뜻
# num_list =[5,2,4,3,1]
# num_list.sort()
# print(num_list) #[1,2,3,4,5]

# 순서 뒤집기 가능 #reverse
# num_list.reverse()
# print(num_list) #[5,4,3,2,1]

# 모두 지우기 #clear
#  num_list.clear()
#  print(num_list) #[]

# # 다양한 자료형 함께 사용 1:30
# mix_list =["세호" , 20 , True]
# print(mix_list) #['세호', 20, True]

#  리스트 확장 #extend
# num_list = [5,4,3,2,1]
# num_list.extend(mix_list)
# print(num_list) #[5, 4, 3, 2, 1, '세호', 20, True]

#1:33 key
# cabinet ={3:"유재석" , 100:"김태호"}
# print(cabinet[3]) #유재석 #3이 키
# print(cabinet[100]) #김태호 #100이 키

# print(cabinet.get(3)) # 유재석
# print(cabinet[5])
# print("hi") #5가 없기 때문에 "hi"가 안적히고 에러뜸

# print(cabinet.get(5)) # get을 사용했을때 none
# print("hi") #"hi"

# print(cabinet.get(5,"사용가능")) #사용 가능시 5오고 없으면 "사용가능"나옴
# print("hi") 

# print(3 in cabinet) # 안에 있는지 in #True
# print(5 in cabinet) #False

# #새손님 

# cabinet[3]="김종국" #유재석괴 깉아서 바뀜
# cabinet["77"]="조세호" #조세호 77로 추가
# print(cabinet)

# #간 손님 #del 삭제
# del cabinet[3]
# print(cabinet)

# # 사용하고 있는 키들만 출력
# print(cabinet.keys()) #([100,77])

# # value들 만 출력 3이 키 김종국이 value
# print(cabinet.values())

# #key와 value를 함꼐 출력 #items
# print(cabinet.items()) #dict_items([(100, '김태호'), ('77', '조세호')])

# # 목욕탕이 문을 닫았을때 #clear
# cabinet.clear ()
# print(cabinet) #{}

#1:40 튜플  #8,28 418
# 메뉴=("돈까스","치즈까스")
# print(메뉴[0])
# print(메뉴[1]) #돈까스 #치즈까스

#메뉴.add("생선까스") 
# #튜플은 내용을 바꿀 수 없add(추가) 안됨 x

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)  #김종국 20 코딩

#위에의 튜플을 사용하면 한번에 할수 있음
# (name,age,hobby) = ("김종국",20,"코딩")
# print(name,age,hobby) #김종국 20 코딩

# #집합(set) 1:43
# #중복이 안됨, 순서기 없음
# my_set ={1,2,3,3,3}
# print(my_set) #{1,2,3}

# java ={"재석","태호","세형"}
# python =set(["재석","명수"])

# 교집합 (java와 python을 모두 할수 있는 사람)
# print(java & python) #{'재석'}

# # 합집합 (java 할수 있거나 python 할 수 있는 개발자) 둘중 하나만
# print(java|python) # |는 (or)
# print(java.untion(python))  #{'태호', '재석', '명수', '세형'} # 순서 없이

# 차집합(java는 할수 있지만 python은 할줄 모르는 사람)
# print(java-python)
# # print(java.difference(python)) #{'태호', '세형'} # 재석은 둘다 할수 있기 떄문에

# #python 할수있는 사람이 늘어남
# python.add("태호")
# print(python)#{'태호', '명수', '재석'}

# #java를 까먹음
# java.remove("태호")
# print(java) #{'세형', '재석'}

#자료구조의 변경 1:46
#커피숍
# menu={"커피","우유","주스"}
# print(menu,type(menu)) #class set {}

# menu = list(menu)
# print(menu, type(menu)) #class list[]

# menu = tuple(menu)
# print(menu,type(menu)) # <class 'tuple'>()

# menu = set (menu)
# print(menu, type(menu)) # <class 'set'>


#퀴즈 1:53 ???
# from random import *
# users =range(1,21) # 1부터 20까지 숫자를 생성
# #print(type(users)) #<class 'range'>
# users = list(users)
# #print(type(users)) # <class 'list'>

# print(users)
# shuffle(users)
# print(users) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# #[8, 3, 6, 14, 9, 18, 15, 11, 7, 20, 17, 10, 16, 12, 5, 1, 19, 4, 2, 13]

# winner = sample(users,4) #4명 중에서 1명은 치킨, 3명은 커피 ?

# print(" -- 당첨자 발표 -- ")
# print("치킨 당첨자 :{0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 -- ")

#if 2:03 ?
# weather ="맑아요"
# if weather=="비":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비믈 필요 없음")

# temp = int(input("기온은 어떄요?"))
# if 30 <= temp:
#     print("너무 더워요 나가지 마세요")
# elif 10<=temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙겨주세요")
# else:
#     print("너무 추워요, 나가지 나세요

# number = int(input ("가격은 얼마에요?"))
# if 3000>=number:
#     print("싸다")
# elif 5000>=number:
#     print("보통이다")
# else:
#     print("다 팔림")

# for waiting_num in range(101): #대기번호 100번 까지 출력
#     print("대기번호 :{0}".format(waiting_num)) #0번 부터
#print("나는 동물중 {}와 {}를 좋아해요.".format("강아지", "고양이"))

# a, b = map(int, input().strip().split(' '))
# print("a =", a, b)
# print("aㅓㄹ히ㅏㅓㅀㅇ", a, 'hello')


# b = input("b를입력: ")
# b = int(b)
# a = input("a를입력: ")
# a = int(a)

# a = input()
# b = int(input())
# print(a* b)
# a, b = input().strip().split(' ')
# print(a,b)

# def 인사하기():
#     print("안녕하세요")
#     print("안녕하세요")
# print(인사하기())   # 안녕하세요 안녕하세요 #  긴 코드를 짧게 인사하기():로 바꿔줌

# def 앙꼬(c) :
#     print(c+1) 
# 앙꼬(3) #4
# 앙꼬(5)#6

# def 함수():
#     return 10
# print(함수()) #10


# a="aBcDeFg"
# print(a.upper())

# station = "사당"
# print(station,"행 열차가 들어오고 있습니다.")

# station = "신도림"
# print(station,"행 열차 도착")

# from random  import *
# date = randint (4,28)
# print('오프라인 스터디 모임 닐짜는 매월'+str(date)+'일로 선정')

# from random import *
# date = randint(4,28)
# print("오프라인 수업은"+str(date)+"입니다.")

# a = "aBcDeFg"
# print("aBcDeFg"[0:3])
# print("aBcDeFg"[:6])
# print("aBcDeFg"[-4:])

# python = "aBcDeFg"
# print(len(python))#7
# print(python.replace("a","A"))
# print(python.replace("B","b"))

#index = python.index("n") #에러

# index = python.index("a") 
# print(index) #0
# print(python.find("a")) # 0
# print(python.find("q")) #-1 뒤에 print("hi")면 -1 다음 hi 출력
# print(python.count("a")) #a가몇개 #1

# print("나는 {}색과 {}색을 좋아해요".format("파란","빨간")) #나는 파란색과 빨간색을 좋아해요
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간")) #나는 빨간색과 파란색을 좋아해요


# print("나는 {c}색과 {c1}색을 좋아해요".format(c="파란",c1="빨간"))  #나는 파란색과 빨간색을 좋아해요

# age=20
# color="빨간"
# print(f"{color}색이 좋은{age}살") #빨간색이 좋은20살

# print("나는 \"이채원\" 입니다") #나는 "이채원" 입니다
# print("나는 이채원\n 입니다") #\n 줄바꿈

#print("red apple\rpine") #pineapple

# a ="http://naver.com"
# vv=a.replace("http://","")
# vv="naver.com"
# vv=vv[:vv.index(".")]
# print(vv)
# passworld = vv[0:3]+str(len(vv))+str(vv.count('e'))+"!"
# print("{0}의 비밀번호는 {1}입니다.".format(a,passworld))


# a = "http://naver.com"
# b = a.replace("http://","")
# print(b) #naver.com
# b = b[:b.index(".")]
# print(b)  #naver
# c = b[0:3]+str(len(b))+str(b.count('e'))+"!"  #nav51!
# print("{0}의 비밀번호는 {1}입니다.".format(a,c)) #http://naver.com의 비밀번호는 nav51!입니다.

# java = {"유재석","김태호","양세형"}
# python = {"유재석","빅명수"}
# print(java & python)  #{'유재석'}

#print(r'@#$%^&*(\'"<>?:;')

#튜플 
# menu =("돈까스","치즈까스")
# print(menu[0])
# print(menu[1]) #ex menu.add("생선까스") 생선까스 추가 안됨 

# (name,age,hobby) = ("김종국",20,"코딩")
# print(name,age,hobby)

# number="4 5"
# print(number)

# print('a 와 b 대소비교')
# a = input("a를 입력: ")
# a = int(a)
# b = input("b를 입력: ")
# b = int(b)
# if a > b:
#    print("a")
# if a < b:
#    print("b")

# a = input("a를 입력: ")
# a = int(a)
# b = input("b를 입력: ")
# b = int(b)

# a=4
# b=5
# print('{} + {} == {}'.format(a,b,a+b))
# ("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))

# a, b = map(int, input().strip().split(' '))
# a=str(4)
# b=str(5)
# print(str("a\t b")
# print('{},{}'.format("a=4","b=5"))


# print('{}  {}'.format(int("4"),int("5")))
# print('{}+{}=={}'.format(int(4),int(5),int(4+5)))

# scores = {"수학":0, "영어": 50, "코딩":100 }
# for subject, scores in scores.items():
#     print(subject,ljust(8), str(score).rjudt(4),sep":")    

# absent = [2,5] # 결석
# no_book = [7]
# for student in range (1,11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와". format (student))
#         break
#         print("{0}, 책을 읽어봐". format(student))

#print( "Python" , "Java" , "Java Script", sep= " vs ") # Python vs Java vs Java Script

# print("Python" , "Java", sep= "," , end="?")
# print("무엇이 더 재밌을까요?") # Python,Java?무엇이 더 재밌을까요?


# 시험 성적 305:31
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject , score)


# 수학 0
# 영어 50
# 코딩 100


# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8),str(score).rjust(4),sep=":")

# 수학      :   0
# 영어      :  50
# 코딩      : 100

#은행 대기 순번표 #001, 002, 003, 004, 005, 006, 007 ....
# for num in range (1,21): #1~20 까지
#     print("대기번호 :" + str(num).zfill(3)) # zfill 0넣기

# 대기번호 :001
# 대기번호 :002
# 대기번호 :003
# 대기번호 :004
# 대기번호 :005
# 대기번호 :006
# 대기번호 :007 ...

# answer = input("아무 값이나  입력하세요")
# print("입력하신 값은" + answer +"입니다.") 
# 아무 값이나  입력하세요7
# 입력하신 값은7입니다.
# input 은 항상 문자열 
# print(type(answer)) <class str>

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0:>10}".format(500))
# #양수 + 음수- 로 표시
# print("{0:>+10}".format(500))
# print("{0:>+10}".format(-500))

# 왼쪽으로 정렬하고 빈칸으로 _을 채움
# print("{0:_<10}".format(500))

# 3자리 마다 , 붙히기
# print("{0:,}".format(100000000000000000))
# 10,000,000,000,000,000

#3자리 마다 , 붙히기에 +-부호 붙히기
#print("{0:+,}".format(100000000000000000))
#+100,000,000,000,000,000

#print("{0:+,}".format(-100000000000000000))
#-100,000,000,000,000,000

#소수점 출력
# print("{0:f}".format(5/3))
#1.666667

# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
#print("{0:.2f}".format(5/3))
#1.67

#encoding="utf8" 안쓰면 한글쓸떄 이상한 글자로 나옴

#score_file.close() 파일 닫아주기

# score_file = open("score.txt","w", encoding="utf8")
# print("수학 : 0", file= score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
# score.txt에 
# 수학 : 0
# 영어 : 50

# 뒤에 이어 쓰고 싶을떄 "a" = append
# score_file = open("score.txt","a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
#score_file.close() 
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

#파일에 쓴 내용을 읽고 싶을때 (불러오기) "r" 한번에 다 읽는거
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close() 
# 수학 : 0
# 영어 : 50
# 코딩 : 100
# 과학 : 80 (터미널에)

# 한줄 한줄씩 만 들어오게 하는것 ???
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close() 

# 파일에 몇줄이있는디 모르고 읽어야 할때


# 딕셔너리
# dictionary = {
#     "name" : "7D 건조망고",
#     "type" : "당절임",
#     "ingredient" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
#     "origin" :"필리핀"
# }
# print("name:",dictionary["name"])
# print("type:",dictionary["type"])
# print("ingredient:",dictionary["ingredient"])
# print("origin:",dictionary["origin"])
# print()

# dictionary["name"]="8D건조망고"
# print("name:",dictionary["name"])


# name: 7D 건조망고
# type: 당절임
# ingredient: ['망고', '설탕', '메타중아황산나트륨', '치자황색소']
# origin: 필리핀

# name: 8D건조망고

# 반복분 반복하기
# for i in reversed(range(8)):
#     print("현재 반복 변수:{}".format(i))
 
# 현재 반복 변수:7
# 현재 반복 변수:6
# 현재 반복 변수:5
# 현재 반복 변수:4
# 현재 반복 변수:3
# 현재 반복 변수:2
# 현재 반복 변수:1
# 현재 반복 변수:0

# output=""

# for i in range(1,10):
#     for j in range(0,i):
#         output +="*"
#     output+="\n"
# print(output)


# break 
# i=0
# while True:
#     print("{}번째 반복문 입니다.".format(i))
#     i=i+1
#     input_text = input(">종료하시겠습니까?(y/n):")
#     if input_text in["y","Y"]:
#         print("반복을 종료합니다.")
#         break

# 0번째 반복문 입니다.
#>종료 하시겠습니까?(y/n): n
#1번째 반복문 입니다.
#>종료 하시겠습니까?(y/n): y

# print("백문이 불여일타\n 백견이 불여일타")
# print("저는 '이채원' 입니다")


# from random import *
# cnt = 0 #총 탑승 승객 수
# for i in range(1,51): # 1~50 이라는 수 (승객)
#      time =randrange(5,51) # 5~50분 소요시간 
#      if 5<= time <=15: # 5~15분 이내의 손님, 탑승 승객수 증가 처리 
#          print("[0]{0}번쨰 손님 (소요시간 : {1}분)".format(i,time))
#          cnt+=1
#      else:
#          print ("[ ] {0}번째 손님 (소요 시간 :{1}분)".format(i,time))
# print ("총 탑승 승객 : {0} 분".format(cnt))

# def open_account():
#     print("새로운 계좌가 생성 되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료 되었습니다. 잔액은 {0}원입니다.".format(balance+money))
#     return balance + money

# def withdraw(balance,money):
#     if balance >= money:
#         print()
# balance = 0
# balance = deposit(balance, 1000)
# print(balance)

# def profile(name,age=17,main_lang="파이썬"):
#     print("이름 : {0}t나이 : {1}\t주 사용언어: {2}"\
#           .format (name,age,main_lang))

# profile("유재석")
# profile("김태호")

#이름 : 유재석t나이 : 17 주 사용언어: 파이썬
#이름 : 김태호t나이 : 17 주 사용언어: 파이썬


# def profile (name, age, main_lang):
#     print(name,age,main_lang)

# profile(name="유재석",main_lang="파이썬",age=20)
# profile(main_lang="자바",age=25, name="김태호")

# # 유재석 20 파이썬
# # 김태호 25 자바

# def checkpoint(soldiers): # 경계근무
#     global gun  # 전역 공간에 있는 gun 사용
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun,soldiers):
#     gun=gun -soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
    

# print("전체 총 :{0}".format(gun))
# checkpoint(2) #2명이 경계근무 나감
# print("남은총 : {0}".format(gun))

# def std_weight(height,gender):
#     if gender == "남자":
#         return height * height *22
#     else:
#         return height * height* 21
# height =175
# gender = "남자"
# weight = std_weight(height / 100,gender)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))

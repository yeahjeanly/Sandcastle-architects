# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.

# 점수 학점

# 81~100 A

# 61~80 B

# 41~60 C

# 21~40 D

# 0~20 E








# 답
a = int(input("score: "))

if 100 >= a > 80:
    print("grade is A")
elif a > 60:
    print("grade is B")
elif a > 40:
    print("grade is C")
elif a > 20:
    print("grade is D")
elif a >= 0:
    print("grade is E")
else:
    print("잘못된 점수입니다")



# 함수 암기용 추가문제 : 
# 
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.

# 현재시간:02:00
# 정각 입니다.

# 현재시간:03:10
# 정각이 아닙니다

# 답 : 
# a = input("현재시간:")

# if a.endswith("00"):
# print("정각 입니다")

# else:
# print("정각이 아닙니다")

##참고

# upper() : 대문자로 변경
# lower() : 소문자로 변경

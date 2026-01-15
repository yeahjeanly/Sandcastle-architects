# 문자열 띄어쓰기
greeting = "환영합니다."
name = "이연주님"
sep = "="
print(sep * 18 + "\n" + greeting + " " + name + "\n" + sep * 18)

# 문자열
a = "JR 코딩 마법 학교"
print(a[0])
print(a[-0])
print(a[-1])
print(a[-5])

# 문자열 슬라이싱
name = "윌리엄 헨리 게이츠 3세"
word = name[0:3]
print(word)

# 문자열 슬라이싱 2
a = "2019-01-01"
year = a[:4]
month = a[5:7]
day = a[8:]
print(year, month, day)

# T -> t
a = "PyThon"
a = a[:2] + 't' + a[3:]
print(a)

# "이연주" 만 출력
name = "내 이름은 이연주"
print(name[6:])

# - 지우고 502260 으로 만들기
post_num = "502-206"
print(post_num[:3] + post_num[4:])

# 예시와 같이 출력
data = "2019-06-29"
print(data[:4] + " 년")
print(data[6] + " 월")
print(data[-2:] + " 일")
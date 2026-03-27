### TL;DR : 대소문자 스왑


# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 
# 코드를 작성해 보세요.





# str = input()





# ->





# 1. 내장함수 이용
str = input()
print(str.swapcase())





# 2. if-else 조건부 표현 
print(''.join(x.upper() if x == x.lower() else x.lower() for x in str))

### if-else 조건부 표현 문법[ 참일_때_값 if 조건 else 거짓일_때_값 for 항목 in 이터러블 ]
#   에서는 리스트 컴프리헨션 시 if가 제일 뒤로 오지않음
### 대괄호가 없는 이유: 제너레이터 표현식
# 파이썬에서 list()나 tuple() 등의 함수나, join()과 같은 메서드의 인자로 컴프리헨션을 바로 넣을 경우,
# 대괄호([])를 생략하고 소괄호(())만 사용해도    
# 생략전 원래 코드 : print("".join([x.upper() if x == x.lower() else x.lower() for x in str_input]))
# 변환된 문자열들을 합치는 코드 : ''.join(...) (합치기)join() 함수는 앞 단계에서 연속적으로 생성된 모든 문자열 조각들을 하나의 큰 문자열로 합칩니다.'' 
# (빈 문자열)을 구분자로 사용했기 때문에, 문자들 사이에 아무것도 넣지 않고 그대로 붙여서 최종 문자열을 만듭니다.
# 예시: 'h', 'E', 'l', 'l', 'O' $\rightarrow$ "hEllO"




# 3. for + if (내가 썼던 정답. 1회 시도 틀림. 2회 시도 맞음.)
# 길수록 오히려 전략을 짜야함 for 반복으로 대문자는 소문자로, 소문자는 대문자로. 그렇다면 만약 대문자면 소문자로,
# 그렇지않다면 대문자로 바꿔주라 하면 되겠고, 주의할점은 else : 붙이기가 되겠다.
str = input()
for i in str:
    if i.islower():
        print(i.upper())
    else : print(i.lower())

#dsanofuiASDFI
# D
# S
# A
# N
# O
# F
# U
# I
# a
# s
# d
# f
# i

#... 코딩마법학교에서 배웠던 줄바꿈 방지 end=''를 깜박했다. print 함수는 기본적으로 줄바꿈이 되어있으므로 주의하자.

str = input()
for i in str:
    if i.islower():
        print(i.upper(),end='')
    else: print(i.lower(),end='')

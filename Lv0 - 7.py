### TL;DR : 몫과 나머지에 통용되는 함수


# 파이썬을 이용해서 가장 빠르게 100과 7의 몫과 나머지를 구하세요





# -> 

q, r = divmod(100, 7)
print (q,r)

#  q=몫, r=나머지



# 프로그래머스 문제
# 위 함수로 하나만 구할때
# 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 
# solution 함수를 완성해주세요.

def solution(num1, num2):
    return divmod(num1, num2)[1]

# 몫이면 뒤에가 [0]
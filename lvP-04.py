# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
# 실행 예시:
# print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}






# 나의 오답 :
# a=dict(keys)
# b=dict(vals)
# print(result={x:for k, v in {a,b}}) ...이게 안되네??
      
# 틀린이유 : 키와 값을 합치는 방법을 몰랐음.

result = dict(zip(keys, vals))
print(result)


# zip()함수 : 동일한 개수로 이루어진 자료형을 묶어주는 역할
# 관련 추가 문제

# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

# 실행 예시:
# print(close_table)
# {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}







close_table = dict(zip(date, close_price))
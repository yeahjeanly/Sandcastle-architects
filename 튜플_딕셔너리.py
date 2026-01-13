# 튜플에서는 리스트의 대괄호[] 대신 소괄호() 사용
# 튜플에서는 리스트와 달리 요소의 수정과 추가가 불가능하다!

# 튜플 예시/ 소괄호가 덮혀서 출력됨. 
fruits = ("banana","apple","melon","orange")

print(fruits)

# 튜플을 생성하는 다른 방법
# 1. 소괄호() 작성 
# 2. tuple()함수 이용
numbers = tuple(range(10))
print(numbers)

# 주의할점: 아래 코드처럼 실행하면 오류남.
#  튜플에서는 요소의 항목을 수정할 수 없다. 수정하려면 리스트 사용해야함. 
# fruits = ("banana","apple","melon","orange")
# fruits[2] = "remon"

# 조건에 맞는 튜플만들어서 출력해보기 
animal = ("호랑이","사자","독수리","곰")
number = tuple(range(5))

print(animal)
print(number)

# ('호랑이', '사자', '독수리', '곰')
# (0, 1, 2, 3, 4)

# 튜플도 리스트와 같이 인덱스를 이용하여 추출이 가능하다.
n = tuple(range(0,10))
print(n)
print("n[0]=", n[0])
print("n[2:5]=", n[2:5])
print("n[::-1]=", n[::-1])

# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# n[0]= 0
# n[2:5]= (2, 3, 4)
# n[::-1]= (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

#  심화문제 
tuple = ("!","야","이","법","마","는","호","암","의","선","주","우")
n = tuple
print(n[::-1])

# 튜플도 리스트와 마찬가지로 len()함수를 이용해 길이를 구할 수 있다.
#  아래는 튜플의 길이만큼 반복시켜 튜플의 요소들을 화면에 출력한 것.
tuple_len = (1,2,3,4,5)

for i in range(len(tuple_len)):
    print(tuple_len[i])


# 딕셔너리: 자료를 찾는 인덱스를 의미하는 키와 자료의 내용인 값을 이용해서 데이터 관리
# 요소들을 중괄호{}를 이용해 표현한다. 

# 딕셔너리 생성법 : 1. {} 사용 2. dict()함수 이용
rank = {"gold":90, "silver":80, "bronze":70}
print(rank)
name = dict([("name","이우연"), ('age',15)])
print(name)

# 딕셔너리에서 원하는 요소 출력하는 방법
rank = {'silver': 80, 'gold':90, 'bronze': 70}

print(rank)
print(rank['silver'])
print(rank['bronze'])
# {'silver': 80, 'gold': 90, 'bronze': 70}
# 80
# 70

# 딕셔너리 요소 변환 & 활용

# 매개변수 여러개로 만든 함수 예제
def favorate_color(name, color, amount) :
    if (amount == 1) :
        print('%s 님은 %s을 좋아하지 않습니다.' % (name, color))
    elif (amount ==2) :
        print('%s 님은 %s을 조금 좋아합니다.' % (name, color))
    else :
        print('%s 님은 %s을 매우 좋아합니다.' % (name, color))
		
favorate_color('이미나', '빨강', 1)
favorate_color('조충범', '노랑', 2)
favorate_color('이예영', '파랑', 3)

# 매개변수가 2개인 함수
# version 1
def introduce(name, gender):
    print(f"{name}님은 {gender}입니다.")
	
introduce("이빛나","여자")
introduce("김코딩","남자")

# version 2
def introduce(name, gender):
    if gender == "여자":
        print("%s 님은 %s 입니다." % (name, gender))
    else:
        print("%s 님은 %s 입니다." % (name, gender))
introduce("이빛나","여자")
introduce("김코딩","남자")

# 매개변수가 3개인 함수
def storage(name, price, amount):
    if amount == True:
        print("%s은 %d원이고 재고가 있습니다." %(name, price))
    else: 
        print("%s은 %d원이고 재고가 없습니다." %(name, price))
		
storage("피자빵",1500,True)
storage("야채빵",1000,False)
storage("크림빵",800,True)
# amount자체가 불리언 값(True/False)이므로 비교 연산자 없이 바로 사용 가능. if amount: 로도 가능.

# 개선된 버전
def storage(name, price, amount):
    if amount:
        status = "있습니다"
    else:
        status = "없습니다"

    print(f"{name}은 {price}원이고 재고가 {status}.")

# 더 간단한 버전
def storage(name, price, amount):
    status = "있습니다" if amount else "없습니다"
    print(f"{name}은 {price}원이고 재고가 {status}.")

#함수에서 선언한 변수의 효력 범위 
# 매개변수 값이 1이 더해졌는데 2가 출력되지 않은 이유
var = 1
def test(var):
    var = var +1
test(var)
print(var)  # 출력값 1 
# 함수 내부에서 var 값을 변경해도 함수 외부의 var 값에는 영향을 미치지 않음.
# 즉, 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 수 있고 함수 밖에서는 사용되지 않는다. 

# 함수 안에서 함수 밖의 변수를 변경할 수는 없을까? 
# return 키워드를 사용하면 가능 
a = 1
def test(a):
    a = a+1
    return a
a = test(a)
print(a)  # 출력값 2
# return 키워드를 사용하여 함수 내부에서 변경된 값을 함수 외부로 반환하고
# 그 값을 다시 함수 외부의 변수에 할당함으로써 변수 값을 변경할 수 있음.

# lambda 함수란: 함수를 한 줄로 간결하게 만들 때 사용하는 함수 
# def 함수는 어렵고 복잡한 함수 표현할때 사용, lambda 함수는 간단한 함수를 만들때 사용
# def 함수이름(매개변수): + return 결과
# lambda 매개변수: 결과
result = lambda a,b,c : a*b-c
print(result(5,2,4))  # 출력값 6
# 위의 코드는 아래의 def 함수와 동일한 기능을 함
def result(a,b,c):
    return a*b-c

#list를 이용해 함수 선언하는 방법 
def printList(lst):
    for element in lst:
        print(element)
printList([1,2,3])
# 리스트는 내가 입력하는 대로 바뀌는 가변적인 객체(object)이다.
# 함수안에 리스트를 넣을때는 함수를 호출하며 원하는 리스트 값을 넣어주면 된다. 

# 문자열 뒤집기 함수 만들기
def print_reverse(text):
    print(text[::-1])
print_reverse("olleh") # 출력값 "hello"

# 성적 리스트 입력 받아 평균 출력하는 함수 만들기 
def print_point(scores):
    result = sum(scores) / len(scores)
    print(f"결과 :{result:.1f}")
    return result
print_point([70,80,90])
# sum() 함수는 리스트의 모든 요소를 더해주는 함수
# len() 함수는 리스트의 요소 개수를 세주는 함수
# :.1f는 소수점 첫째 자리까지 출력하라는 의미


# 심화문제: 리스트를 입력받아 짝수만 화면에 출력할 수 있는 함수를 정의하고 호출해보기 
def print_even(nums):
    for num in nums:
	    if num % 2 == 0:
		    print(num)

print_even([5,7,9,10,12,14,15])




# Q1
def print_magician():
    print("마법사")
    print_magician()

# Q2
print("A")
def message1():
    print("C")
print("B")
def message2():
    print("D")
message1()
print("E")
message2()

#Q3 
def message1():
    print("가")
def message2():
    print("나")
def message3():
    for i in range(4):
        message2()
        print("다")
    message1()

message3()

# Q4
# 함수를 호출할 때는 해당 함수의 정의에 맞는 파라미터를 입력하여 사용한다! 

# Q5
def print_star():
    print("문자열 뒤에 별 문자열을 붙여봅시다%s" % "✯")

print_star()

# Q6
def print_minus(a,b ):
    print(a-b)

minus = print_minus

minus(5, 3)
minus(6,2)

# Q7
def order():
    print("주문하실 음료")
    drink = input()
    print(f"{drink}를 주문하셨습니다.")

order()

# Q8
def print_Calculator(a, b):
	print(a+b)
	print(a-b)
	print(a*b)
	print(a/b)
print_Calculator(7, 5)

# Q9
def print_oddnumber(my_list):
    for x in my_list:
        if x % 2 == 1:
            print(x)

my_list = [1, 4, 5, 6, 9, 11, 15]
print_oddnumber(my_list)

# Q10
def print_maxnumber(a, b, c):
    print(max(a, b, c))

print_maxnumber(3, 5, 2)

# 오답노트 8번 문제
def print_Calculator(a, b):
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")

print_Calculator(7, 5)
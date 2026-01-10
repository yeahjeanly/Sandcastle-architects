#2
def func():
    x =200 
    print(x)
x= 100 
func()
print(x)
#다음 프로그램 실행 결과는?
#200
#100


#3 함수를 정의해서 킬로미터를 마일로 환산하는 프로그램 작성하기 
def km_to_mile(km):
    return km * 0.621371
	
km = int(input("킬로미터를 입력하세요 : "))
mile = km_to_mile(km)
print(f"{km} 킬로미터는 {mile:.2f} 마일로 환산됩니다.")

# 킬로미터를 입력하세요 :30
# 킬로미터는 18.64 마일로 환산됩니다.

# 풀이: 함수 km_to_mile을 정의하여 매개변수 km를 받아 마일로 환산한 값을 반환합니다.

#5
def triangle_area(width, height):
    return width * height * 0.5
print("너비를 입력하세요")
width = int(input())
print("높이를 입력하세요")
height = int(input())
area = triangle_area(width,height)

print(f"=>삼각형의 너비{width}")
print(f"=>삼각형의 높이{height}")
print(f"=>삼각형의 면적{area}")

# 너비를 입력하세요
# 높이를 입력하세요
# =>삼각형의 너비10
# =>삼각형의 높이15
# =>삼각형의 면적75.0

# 풀이: 함수 triangle_area를 정의하여 매개변수 width와 height를 받아 삼각형의 면적을 계산하여 반환합니다.
# 입력값 10과 15를 각각 너비와 높이로 받아 면적 75.0을 출력합니다.

#6
def favorate_color(name, color,favor):
    if favor:
        print(f"{name}는 {color}을 좋아한다.")
    else: 
        print(f"{name}는 {color}을 싫어한다.")
		
favorate_color("민주","빨강색",True)
favorate_color("진서","노란색",True)
favorate_color("지은","파란색",False)

#8
for _ in range(2):
    print("수를 입력하세요")
    num = int(input())

    if num % 2 == 0:
        print(f"{num}은 짝수입니다.")
    else:
        print(f"{num}은 홀수입니다.")

# 수를 입력하세요
# 10은 짝수입니다.
# 수를 입력하세요
# 27은 홀수입니다.
# 풀이: for 루프를 사용하여 두 번 반복하면서 사용자로부터 수를 입력받고, 짝수인지 홀수인지 판별하여 출력합니다.
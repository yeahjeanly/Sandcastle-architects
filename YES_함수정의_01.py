def auto_print():
	print("안녕하세요. 제 이름은 ?입니다.")
	
auto_print()

#심화문제 매개변수가 1개인 경우 짝수인지, 홀수인지 판단하는 함수
def odd_number(num):
	if num % 2 == 0:
		print("%d는 짝수입니다." % num)
	else:
		print('%d는 홀수입니다.' % num)
	
odd_number(7)
odd_number(16)

#심화문제
def favorate_bread(name, bread, amount):
    if amount == 0:
        print(f"{name}이는 {bread}을 좋아하지 않습니다.")
    elif amount == 1:
        print(f"{name}는 {bread}을 조금 좋아합니다.")
    else:
        print(f"{name}는 {bread}을 매우 좋아합니다.")

favorate_bread("재경", "소보로빵", 0)
favorate_bread("진서", "피자빵", 1)
favorate_bread("민주", "옥수수 식빵", 2)

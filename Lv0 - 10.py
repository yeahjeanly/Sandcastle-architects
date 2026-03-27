### TL;DR :map, if조건, split, strip 등 상기


# 정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

# 입출력 예

# 입력 #1

# 4 5

# 출력 #1

# a = 4
# b = 5

# 제한사항
# -100,000 ≤ a, b ≤ 100,000




# 내가푼방식(map은 for문 리스트컴프리헨션과 비슷한 느낌)
a, b = map(int, input().strip().split(' '))
print(f'a = {a}') 
print(f'b = {b}')





# 남이푼방식(앞에 문자열, 뒤에 변수그대로. 조건은 if문)
a, b = map (int, input().split())

if -100000 <= a <= 100000 and -100000 <= b <= 100000:
    print("a =", a)
    print("b =", b)
else:
    print("잘못된 입력입니다.")
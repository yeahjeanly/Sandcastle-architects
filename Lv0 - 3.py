### TL;DR : %의 예시에 각도기 추가 - 390도 % 360 = 30도.


# 문제 설명
# 일반적으로 두 선분이 이루는 각도는 한 바퀴를 360도로 하여 표현합니다. 따라서 각도에 360의 배수를 더하거나 빼더라도 같은 각을 의미합니다. 
# 예를 들면, 30도와 390도는 같은 각도입니다.

# 주어진 코드는 각도를 나타내는 두 정수 angle1과 angle2가 주어질 때, 이 두 각의 합을 0도 이상 360도 미만으로 출력하는 코드입니다. 
# 코드가 올바르게 작동하도록 한 줄(디버깅 문제)을 수정해 주세요.

# angle1 = int(input())
# angle2 = int(input())

# sum_angle = angle1 + angle2
# print(sum_angle)





# ->





angle1 = int(input())
angle2 = int(input())

sum_angle = (angle1 + angle2)%360
print(sum_angle)

# 답이 숫자열로 반환되기에 마지막 줄에서 % 360해줘도 된다 - print(sum_angle % 360)
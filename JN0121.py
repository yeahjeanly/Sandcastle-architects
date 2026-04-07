# 문제2
apple = 3
sentence = "사과는 %d개 있습니다." %apple
print(sentence)

# 문제4
name = "이연주"
age = 15
sentence = "제 이름은 %s이고 나이는 %d입니다." %(name, age)
print(sentence)

# 문제6
product = "카메라"
discount = 5
sentence = "%s %d%% 할인 이벤트 진행 중입니다." %(product, discount)
print(sentence)

# 문제8
math = 75
english = 72
korean = 87
sentence = "이번 기말고사의 평균 점수는 %f 점이다." %((math+english+korean)/3)
print(sentence)

# 문제9
weapon = "도끼"
damage = 200
monster_name = "가고일"
monster_hp = 850
percent = int((monster_hp - damage) / monster_hp * 100)
sentence = "%s로 %d의 피해를 입혔습니다.\n현재 %s의 체력은 %d%% 남았습니다." %(weapon, damage, monster_name, percent)
print(sentence)

# 문제10
date = "2019-07-15"
year = date[0:4]
month = date[5:7]
day = date[8:10]
sentence = "%s년 %d월 %d일" %(year, int(month), int(day))
print(sentence)
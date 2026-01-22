# 문자열 포멧 코드 
apple = 3
sentence = "I eat %d apples." %apple
print(sentence)
# 출력 : I eat 3 apples.

age = 20
sentence = "He is %d years old." %age
print(sentence)
# 출력 : He is 20 years old.

name = "HongGilDong"
sentence = "He is %s." %name
print(sentence)
# 출력 : He is HongGilDong.

food = "Curry"
sentence = "He likes %s." %food
print(sentence)
# 출력 : He likes Curry.

name = "HongGilDong"
age = 20
sentence = "He is %s and he is %d years old." %(name, age)
print(sentence)
# 출력 : He is HongGilDong and he is 20 years old.

name = "홍길동"
age = 20
food = "카레"
sentence = "그의 이름은 %s입니다.\n나이는 %d입니다.\n좋아하는 음식은 %s입니다." %(name, age, food)
print(sentence)
# 출력 : 그의 이름은 홍길동입니다. 
# 나이는 20입니다. 
# 좋아하는 음식은 카레입니다.

rank = 40
total = 250
sentence = "그의 점수는 상위 %f%%입니다." %(rank/total*100)
print(sentence)
# 출력 : 그의 점수는 상위 16.000000%입니다.

name = "김철수"
age = 16
food = "라면"
sentence = "%s 학생은 나이가 %d입니다.\n%s 학생이 좋아하는 음식은 %s입니다." %(name, age, name, food)
print(sentence)
# 출력 : 김철수 학생은 나이가 16입니다.
# 김철수 학생이 좋아하는 음식은 라면입니다.

name = "김석원"
rank = 16
total = 200
grade = "우"
sentence = "%s 학생은 전체 %d명 중 %d등을 했습니다.\n그는 상위 %f%%였지만, 성적은 %s를 받았습니다." %(name, total, rank, rank/total*100, grade)
print(sentence)
# 출력 : 김석원 학생은 전체 200명 중 16등을 했습니다.
# 그는 상위 8.000000%였지만, 성적은 우를 받았습니다.

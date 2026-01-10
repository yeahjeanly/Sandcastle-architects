# 학생 점수 리스트
scores = [85, 92, 78, 90, 88]

# 평균 계산
average = sum(scores) / len(scores)

# 결과 출력
print("점수 목록:", scores)
print("평균 점수:", average)

# 합격 / 불합격 판별
if average >= 80:
    print("결과: 합격 ")
else:
    print("결과: 불합격 ")

### TL;DR : ?????


# 다음 카드는 연주가 지금 가지고 있는 알파벳 카드를 모아둔 리스트
alphabet = ['a','b','d','b','a','c','a','b','a','d']

a : 1
b : 2
c : 3
d : 4
# 로 출력





# ->






# 전략 중복빼고 리스트 다시 만들고 정렬한 변수 설정
# 딕셔너리 변수 하나 만들어주고
# enumerate 함수로 인덱스 넣되 0부터니까 +1하고 
# f스트링 써서 변수 만들되 키:값 모양으로 순환하며 반환되게
# join매소드(변수) 앞에 \n 넣어서 문자열 합치되 줄띄게
alphabet = ['a', 'b', 'd', 'b', 'a', 'c', 'a', 'a', 'b', 'a', 'd', 'c', 'c', 'b']
alphabet_change = sorted(list(set(alphabet)))
counts = {}
for i, card in enumerate(alphabet_change):
    counts[card] = i + 1
output_lines = [f"{key}: {value}" for key, value in counts.items()]
x = '\n'.join(output_lines)
print(x)

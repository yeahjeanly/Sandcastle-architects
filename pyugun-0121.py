#1.화면에 Hello World 문자열을 출력하세요.
print("Hello World")

#2.화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("Mary's cosmetics")

#3.화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
#-> "신씨가 소리질렀다. "도둑이야".
print("""
"신씨가 소리질렀다. "도둑이야".
""")

#4.화면에 C:\Windows를 출력하세요.
print("C:\Windows")

#5.다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
#-> print("안녕하세요.\n만나서\t\t반갑습니다.")
# \t는 탭 , \n 은 줄 바꿈 

#6.print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
#-> print ("오늘은", "일요일")
# 오늘은 일요일 

#7.print() 함수를 사용하여 다음과 같이 출력하세요.
#-> naver;kakao;sk;samsung
print("naver;kakao;sk;samsung")

#8.print() 함수를 사용하여 다음과 같이 출력하세요.
#-> naver/kakao/sk/samsung
print("naver/kakao/sk/samsung")

#9.다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 
# 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
#-> print("first");print("second")
print("first",end=" ");print("second")

# 추가문제 # 여러 정보를 슬래시(/)로 구분하고, 마지막엔 엔터 대신 화살표를 넣고 싶다면?
print("Epoch 1", "Loss: 0.02", "Acc: 0.98", sep=" / ", end=" ▶ Done!\n")
print("010","1234","5678",sep="-",end="Done")

#10.연산 결과 출력 -> 5/3의 결과를 화면에 출력하세요.
print(5/3)

#11.삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
samsung=50000
x=10
print("평가금액:",samsung*x)

#12.다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
시가총액=298000000000
현재가=50000
per=15.79

#13.변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.(14-18 type()문제 생략)
s = "hello"
t = "python" #를 이용해서 -> hello! python 만들기

print(s,"!",t)
print(s+"!"+t)
print(f"{s}! {t}")

#19.year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
x=int(year)
print(x*3)



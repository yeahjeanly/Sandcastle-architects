menu = {
    "라면": 1000,
    "김밥": 800,
    "떡볶이": 2000
}

order = {
    "라면": 2,
    "김밥": 3,
    "떡볶이": 1
}

total = 0

for item in order:
    total += menu[item] * order[item]

print("주문 내역:", order)
print("총 금액:", total, "원")

from random import *

count = 0
for customer in range(1, 51):
    time = randint(5, 50)

    if 5 <= time <= 15:
        print("[O] {}번째 손님 (소요시간 : {}분)".format(customer, time))
        count += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(customer, time))

print("총 탑승 승객: {} 분".format(count))

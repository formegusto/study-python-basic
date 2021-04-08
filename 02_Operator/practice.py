# -*- coding: utf-8 -*-

from math import *
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)  # 8
print(5 % 3)  # 2
print(10 % 3)  # 1
print(5//3)  # 몫 구하기 인데 위랑 무슨차이지? 1

print(10 > 3)  # True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 <= 5)  # True
print(3 == 3)  # True
print(4 == 2)  # False
print(3 + 4 == 7)  # True
print(1 != 3)  # True
print(not 1)  # False
print(not 0)  # True

# 와씨 이게 되네
print(True and False)  # False
print(True and 1)  # 1
print(False and 1)  # False
print(True & 1)  # 1

print((3 > 0) or (3 > 5))  # True
print((3 > 0) | (3 > 5))  # True

print(5 > 4 > 3)  # True
print(5 > 4 > 7)  # False

print(2 + 3 * 4)
print((2+3) * 4)
number = 2 + 3 * 4
print(number)  # 14
number = number + 2
print(number)  # 16
number += 2
print(number)  # 18
number *= 2
print(number)  # 36
number -= 2
print(number)  # 34

number %= 2
print(number)  # 0

# 숫자 처리 함수
print(abs(-5))  # 5
print(pow(4, 2))  # 16
print(max(5, 12))  # 12
print(min(5, 12))  # 5
print(round(3.14))  # 3
print(round(4.99))  # 5

# 라이브러리
print(floor(4.19))  # 내림, 4.0
print(ceil(4.19))  # 올림, 5.0
print(sqrt(16))  # 제곱근, 4.0

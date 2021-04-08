from math import *


def std_weight(height, gender):
    operate = 22 if gender == "남자" else 21
    return round(((height / 100) ** 2) * operate, 2)


print(std_weight(179, "남자"))

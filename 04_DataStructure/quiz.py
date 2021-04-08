from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))

# -----
lst = range(1, 21)
lst = list(lst)
print(lst)
shuffle(lst)

chicken = sample(lst, 1)
coffee = sample(lst, 3)

print("치킨 당첨자 : ", chicken)
print("커피 당첨자 : ", coffee)

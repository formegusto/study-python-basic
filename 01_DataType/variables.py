# -*- coding: utf-8 -*-

animal = '강아지'
name = '호랑이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '에요~')
hobby = '공놀이'
print(name + '는 ' + str(age) + '살이며, ' + hobby + '를 아주 좋아해요')
# 문자열 외의 자료형은 str 로 감싸주어야 한다.
print(name + '는 어른일까요? ' + str(is_adult))

# 다음과 같은 형식은 str로 안 감싸도 된다.
print(name, age, is_adult)

# 한줄 주석
'''
 여러줄 주석
'''

sentence = '나는 소년입니다.'
print(sentence)

sentence2 = '파이썬은 쉬워요.'
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)

jumin = "990120-1234567"
print("성별 : " + jumin[7])  # 성별 : 1
print('연 : ' + jumin[0:2])  # 연 : 99
print('월 : ' + jumin[2:4])
print('일 : ' + jumin[4:6])

print('생년월일 : ' + jumin[:6])  # 처음부터 6직전까지
print('뒤 7자리 : ' + jumin[7:])  # 7자리부터 끝까지
print('뒤 7자리 (뒤에부터) : ' + jumin[-7:])

python = 'Python is Amazing'
print(python.lower())  # python is amazing
print(python.upper())  # PYTHON IS AMAZING
print(python[0].isupper())  # True
print(len(python))  # 17
print(python.replace("Python", "Java"))  # Java is Amazing

index = python.index("n")
print(index)  # 5
index = python.index("n", index + 1)
print(index)  # 15 - 다음 위치부터 찾음
print(python.find("Java"))  # -1 - 포함되어 있지 않음
# print(python.index("Java"))  # Error
print(python.count("n"))  # 2

print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아애요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아애요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아애요.".format("파란", "빨간"))
# 나는 빨간색과 파란색을 좋아애요.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 방법 4 (v3.6 이상 ~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")  # 실제 변수에서 쓰이는 값을 가지고옴

print("백문이 불여일견 \n백견이 불여일타")  # 줄 바꿈 \n
print("저는 \"나도코딩\"입니다.")

print("줄바꿈 문자는 \\n 입니다.")

print("Red Apple\rPine")  # Pine Apple - 커서 위치 변경

print("ABCDEF\bG")  # ABCDEG - 백스페이스

print("\tprint()")  # Tab

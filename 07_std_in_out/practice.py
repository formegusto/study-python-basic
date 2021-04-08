import sys
print("Python", "Java", sep=", ")  # Python, Java
print("Python", "Java", sep=" vs ")  # Python vs Java

# end : 문장의 끝 부분 수정 ( 기본값 : \n )
print("Python", "Java", sep=", ", end="? ")
print("무엇이 더 재미있을까요?")  # Python, Java? 무엇이 더 재미있을까요?

# # 표준 출력으로 찍힘
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 디스트럭처링 할당
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # ljust - 왼쪽 정렬
    # rjust - 오른쪽 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")
'''
수학      :   0
영어      :  50
코딩      : 100
'''

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    # zfill 값이 없는 부분에는 0
    # 인수는 자릿수
    print("대기번호 : " + str(num).zfill(3))
'''
대기번호 : 001
대기번호 : 002
(...)
대기번호 : 020
'''

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))  # 무조건 str로 박힘
print("입력하신 값은 " + answer + "입니다.")

# 빈 자리를 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# 첫 포맷 빈 공간
# > 는 정렬
# 10은 자릿수
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))  # +500
print("{0: >+10}".format(-500))  # -500

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(5000))
print("{0:_<10}".format(50000000))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(10000000000))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기, 자릿수 확보
# 돈이 많으면 행복하니까 빈 자리는 ^표시
print("{0:^<+30,}".format(10000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자릿수
print("{0:.2f}".format(5/3))  # 올림

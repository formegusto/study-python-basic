# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()
'''
수학 : 0
영어 : 50
과학 : 80
영어 : 90
'''

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()
# '''
# 수학 : 0
# '''

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:  # 라인이 없으면
#         print()
#         break
#     print(line, end="")

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
print()

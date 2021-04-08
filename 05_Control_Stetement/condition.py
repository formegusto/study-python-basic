weather = input("오늘 날씨는 어때요? ")

'''
    if 조건 :
        명령문
'''
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("좋은 하루 되세요.")

    print("엘스 걸림")

print("그냥 실행")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("더워용")

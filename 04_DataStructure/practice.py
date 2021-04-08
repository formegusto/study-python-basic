# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)  # [10, 20, 30]

subway = ['유재석', '조세호', '박명수']
print(subway)  # ['유재석', '조세호', '박명수']

# 조세호씨가 몇 번째 칸에 타 있으신가?
print(subway.index('조세호'), "번째 칸")

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append('하하')
print(subway)  # ['유재석', '조세호', '박명수', '하하']

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)  # ['유재석', '정형돈', '조세호', '박명수', '하하']

print(subway.pop())  # 하하
print(subway)  # ['유재석', '정형돈', '조세호', '박명수']

# 같은 이름의 사람이 몇 명 있는지 확인
print(subway.append('유재석'))
print(subway)
print(subway.count("유재석"))  # 2

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)  # [1, 2, 3, 4, 5]

# 뒤집기
num_list.reverse()
print(num_list)  # [5, 4, 3, 2, 1]

# 모두 지우기
# num_list.clear()
print(num_list)  # []


# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)  # [5, 4, 3, 2, 1, '조세호', 20, True]

# 사전
cabinet = {3: '유재석', 100: '김태호'}
print(cabinet)  # {3: '유재석', 100: '김태호'}
print(cabinet[100])  # 김태호
print(cabinet.get(100))  # 김태호
print(cabinet.get(5))  # None
# print(cabinet[5]) - 이 방법으로는 없는 키 적으면 에러뜬다
print(cabinet.get(5, "사용가능"))  # 없으면 두번째 인수로 준 값이 뜬다
print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet[3] = "김종국"  # 대체됨
cabinet["C-20"] = "조세호"  # 추가됨
print(cabinet)
print("C-20" in cabinet)

del cabinet[3]  # 지워짐
print(cabinet)

# 키 들만 출력
print(cabinet.keys())  # dict_keys([100, 'C-20'])

# 값 들만 출력
print(cabinet.values())  # dict_values(['김태호', '조세호'])

# 아이템 단위
print(cabinet.items())  # dict_items([(100, '김태호'), ('C-20', '조세호')])

cabinet.clear()
print(cabinet)  # {}

# 튜플
menu = ("돈까스", "치즈돈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") Error

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 세트 (집합)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1,2,3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (자바와 파이썬을 모두 할 수 있는 자)
print(java & python)  # {'유재석'}
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)  # {'양세형', '김태호'}
print(java.difference(python))

# python을 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# 지우기
java.remove("김태호")
print(java)

# 커피숍
menu = {"커피", "우유", "주스"}  # Set
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))  # list

menu = tuple(menu)
print(menu, type(menu))  # tupple

menu = set(menu)
print(menu, type(menu))

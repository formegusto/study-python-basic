students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)  # [101, 102, 103, 104, 105]

# 학생이름을 길이로 반환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)  # [8, 4, 10]

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)  # ['IRON MAN', 'THOR', 'I AM GROOT']

import pickle

# 열어서 profile_file에 넣고,
# 알아서 클로즈 해줌
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 공부하고 있습니다.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance < money:
        print("출금이 불가능합니다.")
        return balance
    else:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money


def withdraw_night(balance, money):
    commission = 100  # 수수료 100원
    return commission, balance - money - commission


balance = deposit(0, 10000)
balance = deposit(balance, 2000000)

balance = withdraw(balance, 20000000)
balance = withdraw(balance, 10000)

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원 입니다.".format(commission, balance))


def profile(name="안적음", age="안적음", main_lang="할줄아는 언어가 없나봄"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"
          .format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile()


def profile_2(name, age, main_lang):
    print(name, age, main_lang)


profile_2(name="유재석", main_lang="파이썬", age=10)
profile_2(age=10, name="유재석", main_lang="파이썬")


def profile_3(name, age, *lang):
    print("이름: {0}\t나이: {1}\t,"
          .format(name, age), end=" ")
    # end 옵션은 줄바꿈을 없앤다.
    for l in lang:
        print(l, end=" ")
    print()


profile_3("유재석", 20, "Python", "Java", "C", "JS", "C++")
profile_3("조세호", 25, "Kotlin", "Swift")

gun = 10


def checkpoint(soldiers):
    # 파이썬은 전역변수 키워드를 따로 지정해주지 않으면 함수내에서 사용할 수 없다.
    # gun = 20
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


print("전체 종 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

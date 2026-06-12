# 파일이름 :
# 작 성 자 : 안효민

users = []


def show_menu():
    print("\n===== 다이어트 BMI 관리 시스템 V4.0 =====")
    print("1. 사용자 정보 입력하기")
    print("2. 현재 BMI 정보 다시 보기")
    print("3. 목표 체중과 현재 체중 차이 확인해보기")
    print("4. 저장된 정보 불러오기")
    print("5. 종료하기")


def calculate_bmi(weight, height):
    height_meter = height / 100
    bmi = weight / (height_meter ** 2)
    return bmi


def get_bmi_status(bmi):
    if bmi >= 25:
        return "비만"
    elif bmi >= 23:
        return "과체중"
    elif bmi >= 18.5:
        return "정상"
    else:
        return "저체중"


def input_user():
    name = input("이름을 입력해주세요 : ")
    weight = float(input("몸무게를 입력해주세요 : "))
    height = float(input("키를 입력해주세요 : "))
    goal_weight = float(input("목표 체중을 입력해주세요 : "))

    user = [name, weight, height, goal_weight]
    users.append(user)

    print("\n사용자 정보가 입력되었습니다.")
    print(f"이름 : {name}님")
    print(f"키 : {height}cm")
    print(f"몸무게 : {weight}kg")
    print(f"목표 체중 : {goal_weight}kg")


def show_bmi_info():
    if len(users) == 0:
        print("먼저 사용자 정보를 입력해주세요.")
        return

    print("\n-------- BMI 정보 --------")

    for user in users:
        name = user[0]
        weight = user[1]
        height = user[2]

        bmi = calculate_bmi(weight, height)
        status = get_bmi_status(bmi)

        print(f"{name}님")
        print(f"BMI 지수 : {bmi:.2f}")
        print(f"판정 : {status}")
        print("--------------------")


def check_goal_weight():
    if len(users) == 0:
        print("먼저 사용자 정보를 입력해주세요.")
        return

    print("\n-------- 목표 체중 차이 --------")

    for user in users:
        name = user[0]
        weight = user[1]
        goal_weight = user[3]

        dif = weight - goal_weight

        print(f"{name}님")

        if dif > 0:
            print(f"목표 체중까지 {dif:.1f}kg 감량이 필요합니다.")
        elif dif < 0:
            print(f"목표 체중보다 {abs(dif):.1f}kg 적습니다.")
        else:
            print("현재 목표 체중과 동일합니다.")

        print("--------------------")


def show_saved_information():
    if len(users) == 0:
        print("먼저 사용자 정보를 입력해주세요.")
        return

    print("\n-------- 저장된 정보 --------")

    for user in users:
        name = user[0]
        weight = user[1]
        height = user[2]
        goal_weight = user[3]

        bmi = calculate_bmi(weight, height)
        status = get_bmi_status(bmi)

        print(f"이름 : {name}님")
        print(f"키 : {height}cm")
        print(f"몸무게 : {weight}kg")
        print(f"목표 체중 : {goal_weight}kg")
        print(f"BMI 지수 : {bmi:.2f}")
        print(f"BMI 판정 : {status}")
        print("--------------------")


def main():
    while True:
        show_menu()
        menu = input("메뉴를 선택해주세요 : ")

        if menu == "1":
            input_user()

        elif menu == "2":
            show_bmi_info()

        elif menu == "3":
            check_goal_weight()

        elif menu == "4":
            show_saved_information()

        elif menu == "5":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 접근입니다. 다시 선택해주세요.")


main()

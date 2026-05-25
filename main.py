# 파일이름 :
# 작 성 자 :안효민
information=[]
while True:
  print("1. 사용자 정보 입력하기")
  print("2. 현재 BMI 정보 다시 보기")
  print("3. 목표 체중과 현재 체중 차이 확인해보기")
  print("4. 저장된 정보 불러오기")
  print("5. 종료하기")

  menu = input("메뉴를 선택해주세요")
  
  if menu =="1":
    name=input("이름을 입력해주세요 : ")
    weight=float(input("몸무게를 입력해주세요 : "))
    height=float(input("키를 입력해주세요 : "))
    height_meter=height/100
    goal_weight=float(input("목표 체중을 입력해주세요 : "))
    information=[name,weight,height,goal_weight]
    print(f"이름 : {name}님")
    print(f"키 : {height}cm")
    print(f"몸무게 : {weight}kg")
    print(f"목표 체중 : {goal_weight}kg")
    print("사용자 정보가 입력되었습니다")
  elif menu =="2":
    if len(information) == 0:
      print("먼저 사용자 정보를 입력해주세요.")
      continue
    name = information[0]
    weight = information[1]
    height = information[2]
    height_meter = height / 100
    bmi = weight / (height_meter**2)
    if bmi >=25:
      print(f"bmi지수 : {bmi}. 비만입니다.")
    elif bmi>= 23:
      print(f"bmi지수 : {bmi}. 과체중입니다.")
    elif bmi>=18.5:
      print(f"bmi지수 : {bmi}. 정상입니다.")
    else:
      print(f"bmi지수 : {bmi}. 저체중입니다.")
  elif menu =="3":
    if len(information) == 0:
       print("먼저 사용자 정보를 입력해주세요.")
       continue
    weight = information[1]
    goal_weight = information[3]
    dif = weight - goal_weight
    if dif > 0:
      print(f"목표 체중까지 {dif}kg 감량이 필요합니다")
    elif dif <0:
      print(f"목표 체중보다 {dif}kg 적습니다")
    else:
      print("현재 목표 체중과 동일합니다")
  elif menu =="4":
    if len(information) == 0:
       print("먼저 사용자 정보를 입력해주세요.")
       continue
    print("--------저장된 정보--------")
    print(f"이름 : {information[0]}님")
    print(f"키 : {information[2]}cm")
    print(f"몸무게 : {information[1]}kg")
    print(f"목표 체중 : {information[3]}kg")
  elif menu =="5":
    print("프로그램을 종료합니다")
    break
  else:
    print("잘못된 접근입니다, 다시 선택해주세요")
    continue

# 파일이름 :
# 작 성 자 :안효민

while True:
  print("1. 사용자 정보 입력하기")
  print("2. 현재 BMI 정보 다시 보기")
  print("3. 목표 체중과 현재 체중 차이 확인해보기")
  print("4. 저장된 정보 불러오기")
  print("5. 종료하기")

  menu = input("메뉴를 선택해주세요")
  
if menu ==1:
  name=input("이름을 입력해주세요 : ")
  weight=float(input("몸무게를 입력해주세요 : "))
  height=float(input("키를 입력해주세요 : "))
  height_meter=height/100
  goal_weight=float(input("목표 체중을 입력해주세요 : "))
  print(f"이름 : {name}님")
  print(f"키 : {height}cm")
  print(f"몸무게 : {weight}kg")
  print(f"목표 체중 : {goal_weight}kg")
  information=[name,weight,height,goal_weight]
if menu ==2:
   bmi = weight / (height_meter**2)
  if bmi >=25:
    print(f"bmi지수 : {bmi}. 비만입니다.")
  elif bmi>= 23:
    print(f"bmi지수 : {bmi}. 과체중입니다.")
  elif bmi>=18.5:
    print(f"bmi지수 : {bmi}. 정상입니다.")
  else:
    print(f"bmi지수 : {bmi}. 저체중입니다.")
if menu ==3:
  dif = weight-goal_weight
  if dif > 0:
    print(f"목표 체중까지 {dif}kg 감량이 필요합니다")
  if dif <0:
    print(f"목표 체중보다 {dif}kg 적습니다")
  else:
    print("현재 목표 체중과 동일합니다")
if menu ==4:
  print("--------저장된 정보--------")
  print(f"이름 : {name}님")
  print(f"키 : {height}cm")
  print(f"몸무게 {weight}kg")

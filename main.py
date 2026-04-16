# 파일이름 :
# 작 성 자 :안효민
name=input("이름을 입력해주세요 : ")
weight=float(input("몸무게를 입력해주세요 : "))
height=float(input("키를 입력해주세요 : "))
height_meter=height/100
print(f"이름 : {name}님")
print(f"키 : {height}cm")
print(f"몸무게 {weight}kg")
bmi = weight / (height_meter**2)
if bmi >=25:
  print(f"bmi지수 : {bmi}. 과체중입니다.)
elif bmi>= 23:
print

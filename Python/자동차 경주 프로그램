#자동차 경주 프로그램
from turtle import * #
import random #랜덤 함수를 사용
class Car: #Car클래스 선언
    def __init__(self, speed, color, fname, locate, goal): #생성자 생성
        self.speed = speed 
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)
        self.turtle.speed(self.speed)
        self.locate = locate
        self.goal = goal
        
    def drive(self, distance): # 거리 값을 받아 전진
        self.turtle.forward(distance)

    def goto(self, x, y): # 좌표 값을 받아 위치 이동
        self.turtle.goto(x, y)

    def write(self, write): # 문자를 받아 화면에 전시
        self.turtle.write(write)

    def hide(self): # 보이지 않게 숨겨줌
        self.turtle.hideturtle()

register_shape("car2.gif") #해당 이미지파일을 새로 등록

car_list = [] #car라는 빈 리스트 생성
y=-100 #초기 생성 위치
n=0 
for i in range(3): # 자동차 생성 함수 3번 반복
    car_list.append(Car(10, "red", "car2.gif", -400, 0)) #car라는 리스트에 등록

for car in car_list: # car라는 리스트에 있는만큼 반복
    car.turtle.penup() # 이동 경로가 보이지 않게 설정
    car.goto(-400, y) # 해당 좌표로 이동
    car.turtle.pendown() # 이동 경로가 보이도록 설정
    y+=100 #y값에 +100을 해준 후 저장

for i in range(400):
    for car in car_list:
        speed = random.randint(2, 20) #속도는 2~20사이
        if car.locate < 400: # 위치가 400보다 아래일 때
            if car.locate + speed >= 400: #
                speed = 400 - car.locate
                n+=1 # 순위 1씩 증가
                car.goal = 1 
                car.hide()
            car.drive(speed)
            if car.goal == 1:
                car.write(str(n)+"등")
        car.locate += speed

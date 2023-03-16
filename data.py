from turtle import Turtle,Screen
from time import sleep
from random import *

class Scr:
    def __init__(self):
        self.s=Screen()

    def screen_settings(self):
        self.s.setup(600,600)
        self.s.bgcolor('black')
        self.s.listen()
        self.s.title('snake game'.title())
        self.s.tracer(0)

    def refresh_screen(self):
        self.s.update()
        sleep(0.1)

    def hold_screen(self):
        self.s.exitonclick()

class Snake:
    
    def __init__(self):
        self.a=[]
        self.b=0
        self.c=0
        self.d=0
        self.e=0
        self.f=0

    def make_snake(self):
        for self.c in range(3):
            self.a.append(Turtle('square'))
            self.a[self.c].color('white')
            self.a[self.c].speed(1)
            self.a[self.c].penup()
            self.a[self.c].goto(self.b,0)
            self.b-=20
        
    def make_food(self):
        self.d=Turtle("circle")
        self.d.shapesize(0.5,0.5)
        self.d.color("red")
        self.d.penup()
        self.d.speed("fastest")
        self.d.goto(randint(-280,280),randint(-280,280))

    def r(self):
        if self.a[0].heading()!=0 and self.a[0].heading()!=180:
            self.a[0].setheading(0)

    def l(self):
        if self.a[0].heading()!=0 and self.a[0].heading()!=180:
            self.a[0].setheading(180)
    
    def up(self):
        if self.a[0].heading()!=90 and self.a[0].heading()!=270:
            self.a[0].setheading(90)
        
    def down(self):
        if self.a[0].heading()!=90 and self.a[0].heading()!=270:
            self.a[0].setheading(270)

    def snake_move(self):
        for self.b in range(self.c,0,-1):
            self.a[self.b].goto(self.a[self.b-1].xcor(),self.a[self.b-1].ycor())
        self.a[0].forward(20)

    def food_eaten(self):
        if self.a[0].distance(self.d) < 20:
            self.d.goto(randint(-280,280),randint(-280,280))
            return True


    def tail_plus(self):
        self.c+=1
        self.a.append(Turtle('square'))
        self.a[self.c].color('white')
        self.a[self.c].speed(1)
        self.a[self.c].penup()
        self.a[self.c].goto(self.a[self.c-1].xcor(),self.a[self.c-1].ycor())

    def hit_wall(self):
        if self.a[0].xcor()<=-280 or self.a[0].xcor()>=280 or self.a[0].ycor()<=-280 or self.a[0].ycor()>=280:
            return True
    
    def hit_snake(self):
        for self.f in self.a[1:]:
            if self.a[0].distance(self.f)<10:
                return True

    def score(self):
        self.e=Turtle()
        self.e.color("white")
        self.e.penup()
        self.e.hideturtle()
        self.e.goto(0,270)
        self.e.write(f"Score: {self.c-2}",False,"center",("courier",15,"normal"))

    def score_plus(self):
        self.e.clear()
        self.e.write(f"Score: {self.c-2}",False,"center",("courier",15,"normal"))

    def game_over(self):
        self.e.setposition(0,0)
        self.e.write(f"GAME OVER",False,"center",("courier",25,"normal"))




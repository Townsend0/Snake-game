from data import *
from turtle import *
a, b, c = Scr(), Snake(), Screen()
a.screen_settings()
b.make_snake()
b.make_food()
c.onkey(b.l,'Left')
c.onkey(b.r,'Right')
c.onkey(b.up,'Up')
c.onkey(b.down,'Down')
b.score()
game_on=True
while game_on:
    b.snake_move()
    a.refresh_screen()
    if b.food_eaten():
        b.tail_plus()
        b.score_plus()
    if b.hit_wall() or b.hit_snake():
        game_on=False
b.game_over()
a.hold_screen()
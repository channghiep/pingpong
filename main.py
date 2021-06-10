import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

RIGHT_POS = (350, 0)
LEFT_POS = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle(RIGHT_POS)
l_paddle = Paddle(LEFT_POS)

screen.listen()
screen.onkey(r_paddle.paddle_up, "w")
screen.onkey(r_paddle.paddle_down, "s")

screen.onkey(l_paddle.paddle_up, "i")
screen.onkey(l_paddle.paddle_down, "k")

game_on = True
# ballt = Ball()
# ballt.goto(340,100)
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        # game_on =False
    #Detect collision paddle
    # if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
    #     if (r_paddle.ycor() + 20) > ball.ycor() > (r_paddle.ycor() - 20):
    #         ball.bounce_x()
    #         # print('hit')
    #     elif (l_paddle.ycor() + 20) > ball.ycor() > (l_paddle.ycor() - 20):
    #         ball.bounce_x()
    if ball.distance(r_paddle) < 50 and ball.xcor() >340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()







screen.exitonclick()
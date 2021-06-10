from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        # self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        print(self.xcor())
        print(self.ycor())

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

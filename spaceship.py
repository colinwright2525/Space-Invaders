from turtle import Turtle

UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('gold')
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.goto(0, -225)
        self.setheading(UP)

    def right(self):
        self.hideturtle()
        self.setheading(RIGHT)
        self.settiltangle(UP)
        self.showturtle()
        self.forward(30)

    def left(self):
        self.hideturtle()
        self.setheading(LEFT)
        self.settiltangle(DOWN)
        self.showturtle()
        self.forward(30)

    def player_dead(self):
        game_is_on = False
        return game_is_on
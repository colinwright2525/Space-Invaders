from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(0, 270)
        self.write(f'Current level: {self.level}', align='center', font=('courier', 20, 'bold'))

    def change_level(self):
        self.level += 1
        self.clear()
        self.write(f'Current level: {self.level}', align='center', font=('courier', 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('courier', 42, 'bold'))

    def game_won(self):
        self.clear()
        self.goto(0, 0)
        self.write('Enemy turtles\nare vanquished.\nYOU WIN!', align='center', font=('courier', 36, 'bold'))

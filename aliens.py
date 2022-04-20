from turtle import Turtle
import random

COLORS = ['green', 'grey']
DOWN = 270

class Mothership:
    def __init__(self):
        self.aliens = []
        self.ghosts = []
        # self.create_aliens(positions)
        self.stockpile = []
        self.active_lasers = []
        for step in range(10):
            new_laser = Turtle('square')
            new_laser.color('green')
            new_laser.penup()
            new_laser.shapesize(stretch_wid=0.1, stretch_len=1.25)
            new_laser.goto(0, 450)
            new_laser.setheading(DOWN)
            new_laser.speed('fastest')
            self.stockpile.append(new_laser)

    def create_aliens(self, positions):
        for position in positions:
            self.add_alien(position)
            # self.lasers = []


    def add_alien(self, position):
        new_alien = Turtle('turtle')
        color = random.choice(COLORS)
        new_alien.color(color)
        new_alien.penup()
        new_alien.goto(position)
        new_alien.setheading(DOWN)
        new_alien.speed('fastest')
        self.aliens.append(new_alien)

    def fire_laser(self, choice):
        # shooter = self.aliens[choice]
        # new_laser = Turtle('square')
        # new_laser.color('green')
        # new_laser.penup()
        # new_laser.shapesize(stretch_wid=0.1, stretch_len=1.25)
        # new_laser.goto(shooter.position())
        # new_laser.setheading(DOWN)
        # new_laser.speed('fastest')
        # self.lasers.append(new_laser)

        shooter = self.aliens[choice]
        laser = random.choice(self.stockpile)
        self.active_lasers.append(laser)
        self.stockpile.remove(laser)
        laser.goto(shooter.position())



    def kill_alien(self, alien):
        alien.hideturtle()
        self.aliens.remove(alien)
        self.ghosts.append(alien)



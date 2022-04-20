from turtle import Turtle
import time
import random

UP = 90

class Cannon:
    def __init__(self):
        self.ammo = []
        self.active_missiles = []
        for step in range(10):
            new_missile = Turtle('square')
            new_missile.color('red')
            new_missile.penup()
            new_missile.shapesize(stretch_wid=0.1, stretch_len=1.25)
            new_missile.setheading(UP)
            new_missile.speed('fastest')
            new_missile.goto(0, -400)
            self.ammo.append(new_missile)


    def fire_missile(self, ship):
        # new_missile = Turtle('square')
        # new_missile.color('red')
        # new_missile.penup()
        # new_missile.shapesize(stretch_wid=0.1, stretch_len=1.25)
        # new_missile.goto(ship.position())
        # new_missile.setheading(UP)
        # new_missile.speed('fastest')
        # self.missiles.append(new_missile)

        missile = random.choice(self.ammo)
        self.active_missiles.append(missile)
        self.ammo.remove(missile)
        missile.goto(ship.position())





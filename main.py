from turtle import Screen
import time
from spaceship import Spaceship
from cannon import Cannon
from functools import partial
from aliens import Mothership
import random
from scoreboard import Scoreboard

UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('SPACE INVADERS')
screen.tracer(0)

starting_positions = []
x_spot = -225
for alien in range(10):
    position = (x_spot, 250)
    starting_positions.append(position)
    x_spot += 50

ship = Spaceship()
cannon = Cannon()
mothership = Mothership()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(ship.right, 'd')
screen.onkey(ship.left, 'a')

argument = partial(cannon.fire_missile, ship)
screen.onkey(argument, 'space')

empties = []
counter = 1
hold = 2
alien_counter = 0.3
fire = 0
alien_speed = 0.2
alien_hold = 0.5
LEVEL = 1
y_spot = 250
interval = 200

DIRECTION = RIGHT
ORIENTATION = DOWN

game_is_on = True
start_level = False
mothership.create_aliens(starting_positions)

while game_is_on:
    screen.update()
    if start_level:
        y_spot = 250
        for level in range(LEVEL + 1):
            mothership.create_aliens(starting_positions)
            start_level = False
            starting_positions = []
            x_spot = -225
            y_spot -= 40
            for alien in range(10):
                position = (x_spot, y_spot)
                starting_positions.append(position)
                x_spot += 50




    if mothership.aliens == []:
        scoreboard.change_level()
        LEVEL += 1
        counter += 1
        alien_speed += 0.2
        interval -= 50
        mothership.ghosts =[]
        start_level = True

    if LEVEL == 4:
        scoreboard.game_won()
        game_is_on = ship.player_dead()


    fire += 1

    for alien in mothership.aliens:
        if alien.xcor() > 350:
            DIRECTION = LEFT
            ORIENTATION = UP

        if alien.xcor() < -350:
            DIRECTION = RIGHT
            ORIENTATION = DOWN

        alien.hideturtle()
        alien.setheading(DIRECTION)
        alien.settiltangle(ORIENTATION)
        alien.showturtle()
        alien.forward(alien_speed)



    if fire % interval == 0 and mothership.aliens:
        alien_pool = len(mothership.aliens)
        alien_choice = random.randint(0, (alien_pool - 1))
        mothership.fire_laser(alien_choice)


    if mothership.active_lasers:
        for laser in mothership.active_lasers:
            laser.forward(counter)
            if laser.ycor() < -325:
                # counter += 0.1
                # alien_speed += 0.02
                mothership.stockpile.append(laser)
                mothership.active_lasers.remove(laser)

        # for laser in empties:
            # laser.reset()
        # screen.update()


    # if cannon.missiles:
    if cannon.active_missiles:
        hold = counter
        for missile in cannon.active_missiles:
            missile.forward(counter)
            if missile.ycor() > 325:
                # counter += 0.1
                # alien_speed += 0.02
                cannon.ammo.append(missile)
                cannon.active_missiles.remove(missile)

        # for missile in empties:
            # missile.reset()
        # screen.update()

        for missile in cannon.active_missiles:
            for alien in mothership.aliens:
                if missile.distance(alien) < 25:
                    mothership.kill_alien(alien)

    for laser in mothership.active_lasers:
        if laser.distance(ship) < 20:
            scoreboard.game_over()
            game_is_on = ship.player_dead()






screen.exitonclick()

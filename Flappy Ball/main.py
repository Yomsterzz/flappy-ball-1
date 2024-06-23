import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Flappy Ball!"

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

color = (r,g,b)
radius = random.randint(50,200)
gravity = 2000

class Ball:
    def __init__(self, color, radius, x, y):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.xvel = 200
        self.yvel = 0

    
    def draw_ball(self):
        self.pos = (self.x, self.y)
        screen.draw.filled_circle(self.pos, self.radius, self.color)
    

ball1 = Ball(color, radius, 400, 300)

def draw():
    ball1.draw_ball()

def update():
    pass

pgzrun.go()
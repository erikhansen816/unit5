#Erik Hansen
#11/20/17
#antsDemo.py - how to use lists with graphics

from ggame import *
from random import randint

WIDTH = 800
HEIGHT = 400

def step():
    for ant in data['antlist']:
        dx = randint(-4,3)
        dy = randint(-4,3)
        if ant.x + dx > 0 and ant.x + dx < WIDTH:
            ant.x += dx
        if ant.y + dy > 0 and ant.y + dy < HEIGHT:
            ant.y += dy

if __name__ == '__main__':
    red = Color(0xFF0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    
    data = {}
    data['antlist'] = []
    
    for i in range(20):
        data['antlist'].append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run(step)


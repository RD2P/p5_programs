from p5 import *

x = 300
y = 300

def draw_spider(x, y):
  circle(mouse_x, mouse_y,20)

def setup():
  size(600, 600)

def draw():
  background(255)
  draw_spider(x,y)



run()
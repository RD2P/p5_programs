from p5 import *

x = 300
y = 300
x_scale = 1

def draw_legs():
    # RIGHT
    # leg 1
    line(x+20, y+2, x+50, y-10)
    
    # leg 2
    line(x+20, y+5, x+50, y+10)
    
    # leg 3
    line(x+18, y+10, x+50, y+30)
    
    # leg 4
    line(x+16, y+12, x+50, y+40)

    # LEFT
    # leg 1
    line(x-20, y+2, x-50, y-10)
    
    # leg 2
    line(x-20, y+5, x-50, y+10)
    
    # leg 3
    line(x-18, y+10, x-50, y+30)
    
    # leg 4
    line(x-16, y+12, x-50, y+40)

def draw_head():
  """Tie coordinates to edge of body"""

  bottom_x = x
  bottom_y = y + (40 + x_scale)/2
  width = 10 + x_scale/2
  height = 10 + x_scale/2

  rect(bottom_x - width/2, bottom_y, width, height)

def draw_spider():  
  # body
  circle(x, y, 40 + x_scale)

  draw_head()  
  draw_legs()

def setup():
  size(600, 600)

def draw():
  background(255)
  draw_spider()

def key_pressed():
  """Press 1 to increase size, 2 to decrease size"""
  global x_scale
  if key == '1':
    x_scale += 2
  if key == '2' and (x_scale - 2) > 1:
    x_scale -= 2

def mouse_pressed():
  global x,y
  x = mouse_x
  y = mouse_y

run()
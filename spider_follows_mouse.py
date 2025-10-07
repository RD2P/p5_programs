from p5 import *

x = 300
y = 300
s_size = 20

def draw_spider():
  global s_size
  circle(mouse_x, mouse_y, s_size)

def setup():
  size(600, 600)

def draw():
  background(255)
  draw_spider()


def key_pressed():
  """Press 1 to increase size, 2 to decrease size"""
  global s_size
  if key == '1':
    s_size += 5
  if key == '2':
    s_size -= 5

run()
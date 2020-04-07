from draw import *
import math

xspacing = 16
w = 0
theta = 0.0
amplitude = 75.0
period = 500.0
dx = 0.0
yvalues = []

create_window('Test')
create_canvas(400,400)
set_background(BLACK)
frame_rate(60)
w = WIDTH + 16
print (WIDTH)
print(w)
dx = ((2*(math.pi))/period) * xspacing

def calcWave():

  global theta, yvalues
  yvalues = []
  # Increment theta (try different values for 'angular velocity' here
  theta += 0.02

  # For every x value, calculate a y value with sine function
  x = theta
  for i in range(int(w/xspacing)):
      yvalues.append(math.sin(x) * amplitude)
      x += dx


def renderWave():
  stroke(NONE)
  fill(255)
  # A simple way to draw the wave with an ellipse at each location
  for i, x in enumerate(yvalues):
      ellipse(i*xspacing, HEIGHT/2+x, 16, 16)


while True:
    refresh_canvas()

    calcWave()
    renderWave()
    #rectangle(WIDTH/2 + 50, HEIGHT/2 + 50, 100, 100)
    #translate(WIDTH/2, HEIGHT/2)
    #line(10.5, 0, 100, 100)
    #translate(0, 0)
    update_canvas()

from draw import *

create_window('Test')
create_canvas(400,400)
set_background(PURPLE)

while True:
    refresh_canvas()

    stroke(WHITE)
    stroke_width(4)
    rectangle_mode("CENTER")
    translate(WIDTH/2, HEIGHT/2)
    stroke(128)
    fill(128)
    rectangle(0, 0, 100, 100)
    fill(0)
    stroke(0)
    rectangle(50, 50, 100, 100)
    #rectangle(WIDTH/2 + 50, HEIGHT/2 + 50, 100, 100)
    #translate(WIDTH/2, HEIGHT/2)
    #line(10.5, 0, 100, 100)
    #translate(0, 0)
    update_canvas()

from draw import *

create_window('Test')
create_canvas(400,400)
set_background(PURPLE)

while True:
    refresh_canvas()

    stroke(NONE)
    stroke_width(4)
    fill(RED)
    translate(WIDTH/2, HEIGHT/2)

    ellipse_mode(CENTER)
    ellipse(0, 0, 100, 100)

    update_canvas()

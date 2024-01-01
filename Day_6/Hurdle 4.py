def turnright():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    wall_height = 0
    while wall_on_right():
        wall_height += 1
        move()
    turnright()
    move()
    turnright()
    for i in range(wall_height):
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

def turnright():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turnright()
    move()
    turnright()
    move()
    turn_left()
    
for i in range(6):
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

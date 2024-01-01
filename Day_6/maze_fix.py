def turnright():
    turn_left()
    turn_left()
    turn_left()

loop_count = 0  
while not at_goal():
    if right_is_clear():
        loop_count += 1
        if loop_count > 4:
            loop_count = 0
            turn_left()
            continue
            
        turnright()
        move()

    elif front_is_clear():
        loop_count = 0
        move()
        
    else:
        loop_count = 0
        turn_left()
        
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

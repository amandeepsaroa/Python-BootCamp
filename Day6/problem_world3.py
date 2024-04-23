def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    


while not at_goal():
    # move in front if front is clear 
    if front_is_clear():
        move()
    # if front not clear check if right clear if clear then turn right and move right
    elif right_is_clear():
        turn_right()
        move()
    # last option is to turn left but dont move we will now again check if new front clear or not
    else:
        turn_left()
        
    # turning aroung not worth it
    
    
            
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

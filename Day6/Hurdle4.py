def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    # move()
    turn_left()
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
        
    turn_left()
    
    
while not at_goal():
        
    while front_is_clear():
        move()
    jump()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

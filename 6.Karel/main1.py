def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(): # duvar varsa atlarsin
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
    if wall_in_front():
        jump()
    else:
        move()
        
    
    
     
    
        

# front_is_clear()
# right_is_clear()
# wall_in_front()
# wall_on_right()
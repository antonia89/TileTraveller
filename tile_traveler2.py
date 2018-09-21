#Questions:

#1. Which implementation was easier and why?
# I think the second implementation was a lot easier because I had already programmed a solution for the first implementation
#  and just needed to add functions. 

#2. Which implementation is more readable and why?
# In my opinion the second implementation is a lot more readable and "cleaner" because of the comments for the reader.

#3. Which problems in the first implementations were you able to solve with the latter implementation?
#Tidyer code with clear information for functions. 


def move_north(x,y):
    """Moves you from your current position to north (up)"""
    y+=1
    return x,y
def move_south(x,y):
    """Moves you from your current position to south (down)"""
    y=y-1
    return x,y
def move_west(x,y):
    """Moves you from your current position to west (left)"""
    x=x-1
    return x,y
def move_east(x,y):
    """Moves you from your current position to east (right)"""
    x+=1
    return x,y

def not_won_yet(x,y):
    """Returns "True" if you have not won yet and "False if you have won"""
    if x == 3 and y == 1:
        return False
    else:
        return True

def valid_direction(x,y):
    """Checks your current position and prints out valid directions from current postition"""
    if x == 1 and y == 3:
        print("You can travel: ", end='')
        print("(E)ast","or ", end='')
        print("(S)outh.",)
    elif x == 1 and y == 2:
        print("You can travel: ", end='')
        print("(N)orth","or ",end='')
        print("(E)ast","or ", end='')
        print("(S)outh.")
    elif x == 1 and y == 1:
        print("You can travel: ", end='')
        print("(N)orth.",)
    elif x == 2 and y == 3:
        print("You can travel: ", end='')
        print("(E)ast","or ", end='')
        print("(W)est.")
    elif x == 2 and y == 2:
        print("You can travel: ", end='')
        print("(S)outh","or ",end='')
        print("(W)est.",)
    elif x == 2 and y == 1:
        print("You can travel: ", end='')
        print("(N)orth.",)
    elif x == 3 and y == 3:
        print("You can travel: ", end='')
        print("(S)outh","or ",end='')
        print("(W)est.",)
    elif x == 3 and y == 2:
        print("You can travel: ", end='')
        print("(N)orth","or ",end='')
        print("(S)outh.")

def player_move(travel_direction,x,y):
    """Player moves depending on current position and choice of direction """
    if x == 1 and y == 3:
        while travel_direction != "e" and travel_direction != "s":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            if travel_direction == "e":
                x,y = move_east(x,y)
                return x , y
            elif travel_direction == "s":
                x,y = move_south(x,y)
                return x , y

    elif x == 1 and y == 2:
        while travel_direction != "e" and travel_direction != "s" and travel_direction != "n":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            if travel_direction == "e":
                x,y = move_east(x,y)
                return x , y
            elif travel_direction == "s":
                x,y = move_south(x,y)
                return x , y
            elif travel_direction == "n":
                x,y = move_north(x,y)
                return x , y

    elif x== 1 and y == 1:
        while travel_direction != "n":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            x,y = move_north(x,y)
            return x , y

    elif x== 2 and y == 3:
        while travel_direction != "e" and travel_direction != "w":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            if travel_direction == "e":
                x,y = move_east(x,y)
                return x , y
            elif travel_direction == "w":
                x,y = move_west(x,y)
                return x , y

    elif x == 2 and y == 2:
        while travel_direction != "w" and travel_direction != "s":
            print("Not a valid direction!")
            travel_direction=input("Direction: ").lower()
        else:
            if travel_direction == "w":
                x,y = move_west(x,y)
                return x , y
            elif travel_direction == "s":
                x,y = move_south(x,y)
                return x , y

    elif x == 2 and y == 1:
        while travel_direction != "n":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            x,y = move_north(x,y)
            return x , y

    elif x == 3 and y == 3:
        while travel_direction != "w" and travel_direction!="s":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            if travel_direction == "w":
                x,y = move_west(x,y)
                return x , y
            elif travel_direction == "s":
                x,y = move_south(x,y)
                return x , y

    elif x == 3 and y == 2:
        while travel_direction !="n" and travel_direction !="s":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            if travel_direction == "n":
                x,y = move_north(x,y)
                return x , y
            elif travel_direction == "s":
                x,y = move_south(x,y)
                return x , y

    
x = 1
y = 1

while not_won_yet(x,y):
    valid_direction(x,y)
    travel_direction = input("Direction: ").lower()
    x,y = player_move(travel_direction,x,y)
else:
    print("Victory!")

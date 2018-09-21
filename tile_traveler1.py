x = 1
y = 1

while (str(x) + str(y)) != "31":
    if x == 1 and y == 3:
        print("You can travel: ", end='')
        print("(E)ast","or ", end='')
        print("(S)outh.",)
        travel_direction = 0
        travel_direction = input("Direction: ").lower()
        while travel_direction != "e" and travel_direction != "s":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            if travel_direction == "e":
                x = 2
                y = 3
            elif travel_direction == "s":
                x = 1
                y = 2
        
    elif x == 1 and y == 2:
        print("You can travel: ", end='')
        print("(N)orth","or ",end='')
        print("(E)ast","or ", end='')
        print("(S)outh.")
        travel_direction = 0
        travel_direction = input("Direction: ").lower()
        while travel_direction != "e" and travel_direction != "s" and travel_direction != "n":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            if travel_direction == "e":
                x = 2
                y = 2
            elif travel_direction == "s":
                x = 1
                y = 1
            elif travel_direction == "n":
                x = 1
                y = 3

    elif x == 1 and y == 1:
        print("You can travel: ", end='')
        print("(N)orth.",)
        travel_direction = 0
        travel_direction = input("Direction: ").lower()
        while travel_direction != "n":
            print("Not a valid direction!")
            
            travel_direction = input("Direction: ").lower()
        else:
                x = 1
                y = 2

    elif x == 2 and y == 3:
        print("You can travel: ", end='')
        print("(E)ast","or ", end='')
        print("(W)est.")
        travel_direction = 0
        travel_direction = input("Direction: ").lower()
        while travel_direction != "e" and travel_direction != "w":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            if travel_direction == "e":
                x = 3
                y = 3
            elif travel_direction == "w":
                x = 1
                y = 3
            
    elif x == 2 and y == 2:
        print("You can travel: ", end='')
        print("(S)outh","or ",end='')
        print("(W)est.",)
        travel_direction = 0
        travel_direction = input("Direction: ").lower()
        while travel_direction != "w" and travel_direction != "s":
            print("Not a valid direction!")
            travel_direction=input("Direction: ").lower()
        else:
            if travel_direction == "w":
                x = 1
                y = 2
            elif travel_direction == "s":
                x = 2
                y = 1
        
    elif x == 2 and y == 1:
        print("You can travel: ", end='')
        print("(N)orth.",)
        travel_direction = 0
        travel_direction = input("Direction: ").lower()
        while travel_direction != "n":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            x = 2
            y = 2

    elif x == 3 and y == 3:
        print("You can travel: ", end='')
        print("(S)outh","or ",end='')
        print("(W)est.",)
        travel_direction = 0
        travel_direction = input("Direction: ").lower()
        while travel_direction != "w" and travel_direction!="s":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:

            if travel_direction == "w":
                x = 2
                y = 3
            elif travel_direction == "s":
                x = 3
                y = 2
    
    elif x == 3 and y == 2:
        print("You can travel: ", end='')
        print("(N)orth","or ",end='')
        print("(S)outh.")
        travel_direction = 0
        travel_direction = input("Direction: ").lower()
        while travel_direction !="n" and travel_direction !="s":
            print("Not a valid direction!")
            travel_direction = input("Direction: ").lower()
        else:
            if travel_direction == "n":
                x = 3
                y = 3
            elif travel_direction == "s":
                print("Victory!")
                break

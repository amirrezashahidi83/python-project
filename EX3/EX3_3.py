def EX3_3(commands):
    x = 0
    y = 0
    for command in commands:
        if command == "s":
            y -= -1
        elif command == "n":
            y += 1
        elif command == "e":
            x -= 1
        elif command == "w":
            x += 1
    
    return (x == -3 && y == 2) || ( x == 4 && y = 3)

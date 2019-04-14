f = open("Data/DATA32.txt")

while True:
    info = f.readline()[:-1].split(' ')
    if len(info) == 1:
        break

    jump = int(info[0])
    game = []

    for i in range(int(info[2])):
        game.append(f.readline()[:-1])

    game.reverse()

    die = False
    jDist = 0
    x = 0
    y = 1

    for char in game[1]:
        if char == "L":
            break
        else:
            x += 1

    while True:
        # print(y, x)
        if game[y][x] == 'G':
            print("CLEAR")
            break
        if game[y][x] == '@' or die:
            print(x+2)
            break

        if game[y][x+1] == '.' or game[y][x+1] == 'G':
            x += 1
        elif game[y][x + 1] == "@":
            # print("jump")
            for i in range(jump):
                if game[y][x + 1] == '.':
                    break
                try:
                    if game[y+1][x] != "@":
                        y += 1
                    else:
                        die = True
                        break
                except:
                    die = True
                    break
            if game[y][x+1] == "@" or game[y][x+2] == "@":
                # print(y, x)
                die = True
                continue
            else:
                x += 2
            while y > 1:
                if game[y-1][x] != "@":
                    y -= 1
                else:
                    # print("DIed")
                    die = True
                    break

        # elif game[y][x+1] == "@":
        #     if y > jump:
        #         x += 1
        #         jDist += 1
        #     else:
        #         y += jump

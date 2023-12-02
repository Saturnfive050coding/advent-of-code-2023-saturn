input = open("day2.txt", "r")
games = input.readlines()

def check_cubes(cubes):
    if "red" in cubes:
        num_cubes = ''.join(filter(str.isdigit, cubes))
        num_cubes = int(num_cubes)
        if num_cubes > 12:
            return False
    elif "green" in cubes:
        num_cubes = ''.join(filter(str.isdigit, cubes))
        num_cubes = int(num_cubes)      
        if num_cubes > 13:
            return False
    elif "blue" in cubes:
        num_cubes = ''.join(filter(str.isdigit, cubes))
        num_cubes = int(num_cubes)
        if num_cubes > 14:
            return False
    return True

def main():
    sum = 0
    IS_POSSIBLE = True
    for game in games:
        game = game.split(":")
        game_num = ''.join(filter(str.isdigit, game[0]))
        game_num = int(game_num)

        game[1] = game[1].replace(";", ",")
        colours = game[1].split(",")
        for cubes in colours:
            if check_cubes(cubes) == False:
                IS_POSSIBLE = False
                break
            else:
                IS_POSSIBLE = True

        if IS_POSSIBLE == True:
            sum = sum + game_num
        else:
            IS_POSSIBLE == True
    
    print("Sum: ", sum)

if __name__ == "__main__":
    main()
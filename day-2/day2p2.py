input = open("day2.txt", "r")
games = input.readlines()

def check_cubes(cubes, min_cubes):
    if "red" in cubes:
        num_cubes = ''.join(filter(str.isdigit, cubes))
        num_cubes = int(num_cubes)
        if num_cubes > min_cubes[0]:
            min_cubes[0] = num_cubes
    elif "green" in cubes:
        num_cubes = ''.join(filter(str.isdigit, cubes))
        num_cubes = int(num_cubes)     
        if num_cubes > min_cubes[1]:
            min_cubes[1] = num_cubes
    elif "blue" in cubes:
        num_cubes = ''.join(filter(str.isdigit, cubes))
        num_cubes = int(num_cubes)
        if num_cubes > min_cubes[2]:
            min_cubes[2] = num_cubes
    
    return min_cubes

def main():
    sum = 0
    min_cubes = [0, 0, 0]
    IS_POSSIBLE = True
    for game in games:
        game = game.split(":")
        game_num = ''.join(filter(str.isdigit, game[0]))
        game_num = int(game_num)

        game[1] = game[1].replace(";", ",")
        colours = game[1].split(",")
        for cubes in colours:
            check_cubes(cubes, min_cubes)
        

        sum = sum + (min_cubes[0] * min_cubes[1] * min_cubes[2])
        min_cubes = [0, 0, 0]
    
    print("Sum: ", sum)

if __name__ == "__main__":
    main()
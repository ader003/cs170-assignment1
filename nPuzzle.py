# import heapq
# the different choices in puzzles offered/test cases
trivial = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]
veryEasy = [[1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]]
easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]
doable = [[0, 1, 2],
          [4, 5, 3],
          [7, 8, 6]]
ohBoy = [[8, 7, 1],
         [6, 0, 2],
         [5, 4, 3]]
impossible = [[1, 2, 3],
              [4, 5, 6],
              [8, 7, 0]]
userPuzzle_string = " "
goalState = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]


def main():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own."
                       + '\n')
    if puzzle_mode == "1":
        print_puzzle(default_puzzle_mode())

    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
              "Enter each row using a space or tab between each number. RET only when finished." + '\n')
        input(userPuzzle_string)
        user_puzzle = [x for x in userPuzzle_string in userPuzzle_string]
        print(user_puzzle)  # TODO: delete; temporary for for testing purposes
    return


def default_puzzle_mode():
    selected_difficulty = input(
        "You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 5." + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if selected_difficulty == "1":
        print("Difficulty of 'Very Easy' selected.")
        return veryEasy
    if selected_difficulty == "2":
        print("Difficulty of 'Easy' selected.")
        return easy
    if selected_difficulty == "3":
        print("Difficulty of 'Doable' selected.")
        return doable
    if selected_difficulty == "4":
        print("Difficulty of 'Oh Boy' selected.")
        return ohBoy
    if selected_difficulty == "5":
        print("Difficulty of 'Impossible' selected.")
        return impossible


def print_puzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])


def uniform_cost_search():  # basically BFS, keeping track of how many L's deep you've expanded
    nodes_expanded = 0  # he wants this data
    cost = 0

    return cost, nodes_expanded


def misplaced_tile_heuristic():
    nodes_expanded = 0
    cost = 0

    return cost, nodes_expanded


def manhattan_distance_heuristic():
    nodes_expanded = 0
    cost = 0

    return cost, nodes_expanded


def move_zero(direction, zero_position):  # TODO: REWRITE; CURRENTLY, MORE LINES THAN NECESSARY
    if direction == "up":
        position_holder = zero_position
        # look at the index above
        above_position = 0 # find it
        zero_position = above_position
        above_position = position_holder
        return zero_position, above_position

    if direction == "down":
        position_holder = zero_position
        # look at the index above
        below_position = 0  # find it
        zero_position = below_position
        below_position = position_holder
        return zero_position, below_position

    if direction == "right":
        position_holder = zero_position
        # look at the index above
        right_position = 0  # find it
        zero_position = right_position
        right_position = position_holder
        return zero_position, right_position

    if direction == "left":
        position_holder = zero_position
        # look at the index above
        left_position = 0  # find it
        zero_position = left_position
        left_position = position_holder
        return zero_position, left_position



if __name__ == '__main__':
    main()

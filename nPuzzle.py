# TODO: link treeCreation.py

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
eight_goal_state = [[1, 2, 3],
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
        user_puzzle_size = x
        create_goal_state(user_puzzle_size)
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


def create_goal_state(puzzle_size):  # works under the assumption there was a valid
    # size (a factor of 3, minus 1) requested
    puzzle_dimensions = sqrt(puzzle_size + 1)
    goal_tuples = [x for x in range(0, puzzle_dimensions)]
    goal_state = []
    for i in range(0, puzzle_dimensions):
        goal_state[i] = goal_tuples[i]
    print(goal_state)  # TODO: REMOVE LATER; PRESENT FOR TESTING PURPOSES
    return goal_state

if __name__ == '__main__':
    main()

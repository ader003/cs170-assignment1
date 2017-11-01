import TreeNode
import heapq as min_heap_esque_queue  # because it kinda acts like a min heap

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
oh_boy = [[8, 7, 1],
         [6, 0, 2],
         [5, 4, 3]]
impossible = [[1, 2, 3],
              [4, 5, 6],
              [8, 7, 0]]
userPuzzle_string = " "

# TODO: CHANGE TO ACCEPT N PUZZLE
eight_goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]


def main():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own."
                        + '\n')
    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())

    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
              "Enter each row using a space or tab between each number. RET only when finished." + '\n')
        input(userPuzzle_string)
        user_puzzle = [x for x in userPuzzle_string in userPuzzle_string]
        print(user_puzzle)  # TODO: delete; temporary for for testing purposes
        user_puzzle_size = x
        create_goal_state(user_puzzle_size)
    return


def init_default_puzzle_mode():
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
        return oh_boy
    if selected_difficulty == "5":
        print("Difficulty of 'Impossible' selected.")
        return impossible


def print_puzzle(puzzle):
    # TODO: ADAPT TO ACCEPT N PUZZLES
    for i in range(0, 3):
        print(puzzle[i])


def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
                      "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        uniform_cost_search(puzzle)
    if algorithm == "2":
        misplaced_tile_heuristic(puzzle)
    if algorithm == "3":
        manhattan_distance_heuristic(puzzle)


def uniform_cost_search(puzzle):  # basically BFS, keeping track of how many nodes expanded

    starting_node = TreeNode.TreeNode(None, puzzle, 0, 0)
    working_queue = []
    repeated_states = dict()
    min_heap_esque_queue.heappush(working_queue, starting_node)
    num_nodes_expanded = 0

    while len(working_queue) > 0:
        node_from_queue = min_heap_esque_queue.heappop(working_queue) # the node from the queue being considered/checked
        if node_from_queue.solved():  # check if the current state of the board is the solution
            print("yay")
            # TODO: PRINT TREE TRACE
            return node_from_queue

        # Hash in tuples
        if node_from_queue.board_to_tuple() not in repeated_states:
            repeated_states[node_from_queue.board_to_tuple()] = "This can literally be anything"
            # push non-duplicate parents onto queue
            children_from_node = node_from_queue.expand_children()
            num_children = len(children_from_node)
            for i in range(0, num_children):
                # do not hash duplicate children
                if children_from_node[i].board_to_tuple() not in repeated_states:
                    min_heap_esque_queue.heappush(working_queue, children_from_node[i])
                    num_nodes_expanded = num_nodes_expanded + 1

        if len(working_queue) == 0:
            print("Failure. No solution.")

    return num_nodes_expanded


def misplaced_tile_heuristic(puzzle):
    nodes_expanded = 0
    cost = 0

    return cost, nodes_expanded


def manhattan_distance_heuristic(puzzle):
    nodes_expanded = 0
    cost = 0

    return cost, nodes_expanded


# TODO: FOR N PUZZLE
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

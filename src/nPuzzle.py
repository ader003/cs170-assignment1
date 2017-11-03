import TreeNode
import copy
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

# FUTURE: CHANGE TO ACCEPT N PUZZLE
eight_goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]


def main():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own."
                        + '\n')
    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())

    if puzzle_mode == "2":  # TODO: IMPLEMENT
        user_puzzle_string = input("Enter your puzzle, using a zero to represent the blank. " +
                                   "Please only enter valid 8-puzzles. Enter the puzzle demilimiting " +
                                   "the numbers with a space. RET only when finished." + '\n')
        print("User puzzle string: ", user_puzzle_string, '\n')  # TODO: delete; temporary for for testing purposes
        user_puzzle = user_puzzle_string.split()
        for i in range(0, len(user_puzzle)):
            user_puzzle[i] = int(user_puzzle[i])
        # print("User puzzle (list): ", user_puzzle)
        # print("Length of user puzzle: ", len(user_puzzle))
        # create_goal_state_board(len(user_puzzle))
        select_and_init_algorithm(user_puzzle)

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
    # FUTURE: ADAPT TO ACCEPT N PUZZLES
    for i in range(0, 3):
        print(puzzle[i], '\n')


def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
                      "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        uniform_cost_search(puzzle, 0)
    if algorithm == "2":
        uniform_cost_search(puzzle, 1)
    if algorithm == "3":
        uniform_cost_search(puzzle, 2)


def uniform_cost_search(puzzle, heuristic):  # basically BFS, keeping track of how many nodes expanded

    starting_node = TreeNode.TreeNode(None, puzzle, 0, 0)
    working_queue = []
    repeated_states = dict()
    min_heap_esque_queue.heappush(working_queue, starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    repeated_states[starting_node.board_to_tuple()] = "This is the parent board"

    stack_to_print = []  # the board states are stored in a stack

    while len(working_queue) > 0:
        max_queue_size = max(len(working_queue), max_queue_size)
        # the node from the queue being considered/checked
        node_from_queue = min_heap_esque_queue.heappop(working_queue)
        repeated_states[node_from_queue.board_to_tuple()] = "hell"
        # moved to line 95 -- no difference was made
        # print(node_from_queue.board, node_from_queue.g_n)
        if node_from_queue.solved():  # check if the current state of the board is the solution
            print("This message indicates the puzzle was solved. Printing was skipped.")
            # while len(stack_to_print) > 0:
            #    node_to_print = stack_to_print.pop()
            #    print(node_to_print)
            print(node_from_queue.board)
            print("Number of nodes expanded: ")
            print(num_nodes_expanded)
            print("Max queue size:", max_queue_size)
            return node_from_queue
        # push the non-duplicate parent boards to stack
        stack_to_print.append(node_from_queue.board)
        # expand children : children_from_node is a list of expanded children's nodes
        children_from_node = node_from_queue.expand_children(heuristic)
        # push non-duplicate children to working_queue
        for expanded_child in children_from_node:
            if expanded_child.board_to_tuple() not in repeated_states:
                min_heap_esque_queue.heappush(working_queue, expanded_child)
                num_nodes_expanded += 1
            # Hash in tuples
            repeated_states[expanded_child.board_to_tuple()] = "This the newest unique board of an expanded child"

    if len(working_queue) == 0:
        print(num_nodes_expanded)
        print(max_queue_size)
        print("Failure. No solution.")

    return


# FUTURE: N PUZZLE
def create_goal_state_board(puzzle_size):

    # puzzle_dimensions = (puzzle_size + 1) / 3
    # if (puzzle_size + 1) % 3 == 0:
    #    print("Invalid puzzle size. Please ensure the size of your puzzle = 3n + 1, for any natural number n.")

    # goal_state_row = []
    # goal_state_board = []
    # puzzle_size_counter = copy.deepcopy(puzzle_size)
    # for i in range(0, puzzle_size_copy):
    #    for j in range(0, puzzle_dimensions):
    #        goal_state_row = goal_state_row.append[puzzle_size_counter]
    #        puzzle_size_counter -= 1
    #        if len(goal_state_row) != 8:
    #            goal_state_row.append[0]
    #    goal_state_board.append[goal_state_row]

    # for i in range(0, puzzle_size):
    #    for j in range(0, 3):
    #        goal_state_row = goal_state_row.append(puzzle_size_counter)
    #        puzzle_size_counter -= 1
    #    if len(goal_state_row) != 8:
    #        goal_state_row.append[0]
    #    goal_state_board.append(goal_state_row)

    # print(goal_state_board)  # TODO: REMOVE LATER; PRESENT FOR TESTING PURPOSES
    # return goal_state_board

    return

if __name__ == '__main__':
    main()

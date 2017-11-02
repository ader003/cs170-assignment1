import copy

eight_goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]

manhattan_distance_matrix = [[0, 1, 2, 1, 2, 3, 2, 3],
                             [1, 0, 1, 2, 1, 2, 3, 2],
                             [2, 1, 0, 3, 2, 1, 4, 3],
                             [1, 2, 3, 0, 1, 2, 1, 2],
                             [2, 1, 2, 1, 0, 1, 2, 1],
                             [3, 2, 1, 2, 1, 0, 1, 2],
                             [2, 3, 4, 1, 2, 1, 0, 1],
                             [3, 2, 3, 2, 1, 2, 1, 0]]


class TreeNode:

    def __init__(self, parent_node, board, h_n, g_n):

        self.board = board
        self.parent = parent_node
        self.g_n = g_n  # how far you've travelled (not the heuristic)
        self.h_n = h_n  # the heuristic
        return

    def expand_children(self, heuristic):

        if heuristic == 0:
            g_n = 0
        elif heuristic == 1:
            g_n = self.find_misplaced_distance()
        elif heuristic == 2:
            g_n = self.find_manhattan_distance_heuristic()

        # viable moves
        # TODO: CHANGE TO ACCEPT N PUZZLE
        children = []  # a list of boards
        z = self.zero_position()  # position of the zero in the parent
        # the following if statements determine the new position of the 0 in the child node
        if z[1] in range(0, 2):
            # can move right
            # c_node is the new child node
            # parameters passed in are the new z position coordinates
            c_right_node_board = self.child_node(z[0], z[1] + 1)
            c_right_node = TreeNode(self, c_right_node_board, self.h_n + 1, g_n)
            children.append(c_right_node)
        if z[1] in range(1, 3):
            # can move left
            c_left_node_board = self.child_node(z[0], z[1] - 1)
            c_left_node = TreeNode(self, c_left_node_board, self.h_n + 1, g_n)
            children.append(c_left_node)
        if z[0] in range(0, 2):
            # can move down
            c_down_node_board = self.child_node(z[0] + 1, z[1])
            c_down_node = TreeNode(self, c_down_node_board, self.h_n + 1, g_n)
            children.append(c_down_node)
        if z[0] in range(1, 3):
            # can move up
            c_up_node_board = self.child_node(z[0] - 1, z[1])
            c_up_node = TreeNode(self, c_up_node_board, self.h_n + 1, g_n)
            children.append(c_up_node)
        return children

    def zero_position(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return [i, j]

    def __lt__(self, other): # to tell the priority queue how to queue
        return (self.h_n + self.g_n) < (other.h_n + other.g_n)

    def child_node(self, y_val, x_val):
        # a copy of the board
        board_copy = copy.deepcopy(self.board)
        # on the parent board: x and y position values of the tile 0 is being swapped with
        swapped_val = board_copy[y_val][x_val]
        # child = TreeNode(self, board_copy, 0, self.g_n + 1)
        # child.board[y_val][x_val] = 0  # the board now has 2 0's
        board_copy[y_val][x_val] = 0
        # set parent 0 position to the swapped value
        # child.board[self.zero_position()[0]][self.zero_position()[1]] = swapped_val
        board_copy[self.zero_position()[0]][self.zero_position()[1]] = swapped_val

        return board_copy

    def board_to_tuple(self):  # TODO: MAKE IT HANDLES N PUZZLES
        return tuple(self.board[0]), tuple(self.board[1]), tuple(self.board[2])

    def solved(self):  # TODO: CHANGE TO ACCEPT N PUZZLE
        return self.board == eight_goal_state

    def find_misplaced_distance(self):
        # take board indexes, check against goal state, (ignore 0s)
        # if they don't match, then increment misplaced_distance
        # TODO: HANDLE N SIZE PUZZLE
        misplaced_distance = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] != 0 and (self.board[i][j] != eight_goal_state[i][j]):
                    misplaced_distance += 1
        self.g_n = misplaced_distance
        return misplaced_distance

    def find_manhattan_distance_heuristic(self):
        manhattan_distance = 0
        # TODO: HANDLE N SIZE PUZZLE
        for m in range(0, 3):
            for n in range(0, 3):
                if self.board[m][n] != 0 and (self.board[m][n] != eight_goal_state[m][n]):
                    manhattan_distance += manhattan_distance_matrix[self.board[m][n] - 1][eight_goal_state[m][n] - 1]
        return manhattan_distance

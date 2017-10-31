# TODO link to nPuzzle.py
import heapq
import copy


class TreeNode:

    # TODO: CHANGE TO ACCEPT N PUZZLE
    eight_goal_state = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 0]]

    def __init__(self, parent_node, board, h_n, g_n):

        self.board = board
        self.parent = parent_node
        self.g_n = g_n # how far you've travelled (not the heuristic)
        self.h_n = h_n # the heuristic

    def expand_children(self):
        # viable moves
        # TODO: CHANGE TO ACCEPT N PUZZLE
        children = []
        z = self.zero_position()  # position of the zero in the parent
        # the following if statements determine the new position of the 0 in the child node
        if z[1] in range(0, 2):
            # can move right
            # c_node is the new child node
            c_node = self.child_node(z[0], z[1] + 1) # parameters passed in are the new z position coordinates
            children.append(c_node)
        if z[1] in range(1, 3):
            # can move left
            c_node = self.child_node(z[0], z[1] - 1)
            children.append(c_node)
        if z[0] in range(0, 2):
            # can move down
            c_node = self.child_node(z[0] - 1, z[1])
            children.append(c_node)
        if z[0] in range(1, 3):
            # can move up
            c_node = self.child_node(z[0] + 1, z[1])
            children.append(c_node)

    def zero_position(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == 0:
                    return i, j

    def child_node(self, y_val, x_val):
        # a copy of the board
        board_copy = copy.deepcopy(self.board)
        # on the parent board: x and y position values of the tile 0 is being swapped with
        swapped_val = board_copy[y_val][x_val]
        child = TreeNode.TreeNode(self, board_copy, 0, self.g_n + 1)
        child.board[y_val][x_val] = 0 # the board now has 2 0's
        # set parent 0 position to the swapped value
        child.board[self.zero_position()[0]][self.zero_position()[1]] = swapped_val
        # now, the nodes have achieved a similar affect to being expanded

        return child

    def solved(self):
        # TODO: CHANGE TO ACCEPT N PUZZLE
        if self.board == self.eight_goal_state:
            return True
        else:
            return False

def move_zero(direction, zero_position):
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
# Find problem statement here https://gist.github.com/mukundmr/c546a8ad8d8bf52cda163824f2eefb88

class OrangeState(object):
    VOID = 0
    FRESH = 1
    ROTTEN = 2

class TheOrangeMatrix(object):
    def __init__(self, array, m, n):
        self.array = array
        self.no_of_rows = m
        self.no_of_cols = n       

    def get_cell_value(self, i, j, direction):
        array, m, n = self.array, self.no_of_rows - 1, self.no_of_cols -1
        directions_and_value = {
            "north": lambda param: 0 if (i - 1) < 0 else array[i-1][j],
            "south": lambda param: 0 if (i + 1) > m else array[i+1][j],
            "east": lambda param: 0 if (j - 1) < 0 else array[i][j-1],
            "west": lambda param: 0 if (j + 1) > n else array[i][j+1],
            "northeast": lambda param: 0 if (i - 1) < 0 or (j - 1) < 0 else array[i-1][j-1],
            "northwest": lambda param: 0 if (i - 1) < 0 or (j + 1) > n else array[i-1][j+1],
            "southeast": lambda param: 0 if (i + 1) > m or (j - 1) < 0 else array[i+1][j-1],
            "southwest": lambda param: 0 if (i + 1) > m or (j + 1) > n else array[i+1][j+1],
        }
        try:
            return directions_and_value[direction]("")
        except Exception as e:
            print(f"Error = {str(e)}, {i}, {j}, {direction}")
            # if invalid direction return -1
            return -1

    def can_rot_from_direction(self, direction, i, j):
        orange_state = self.get_cell_value(i, j, direction)
        fresh_orange = (self.array[i][j] == OrangeState.FRESH)
        return True if fresh_orange and orange_state == OrangeState.ROTTEN else False

    def can_rot_from_north(self, i, j):
        return self.can_rot_from_direction("north", i, j)

    def can_rot_from_south(self, i, j):
        return self.can_rot_from_direction("south", i, j)

    def can_rot_from_east(self, i, j):
        return self.can_rot_from_direction("east", i, j)

    def can_rot_from_west(self, i, j):
        return self.can_rot_from_direction("west", i, j)

    def can_rot_from_north_west(self, i, j):
        return self.can_rot_from_direction("northwest", i, j)

    def can_rot_from_north_east(self, i, j):
        return self.can_rot_from_direction("northeast", i, j)

    def can_rot_from_south_west(self, i, j):
        return self.can_rot_from_direction("southwest", i, j)

    def can_rot_from_south_east(self, i, j):
        return self.can_rot_from_direction("southeast", i, j)

    def can_rot_immediately(self, i, j):
        if self.can_rot_from_north(i, j) or self.can_rot_from_south(i, j) or \
            self.can_rot_from_east(i, j) or  self.can_rot_from_west(i, j) or \
            self.can_rot_from_north_east(i, j) or self.can_rot_from_north_west(i, j) or \
            self.can_rot_from_south_east(i, j) or self.can_rot_from_south_west(i, j):
            return True
        else:
            return False

    def cannot_rot_at_all(self, i, j):
        orange_north = self.get_cell_value(i, j, "north")
        orange_south = self.get_cell_value(i, j, "south")
        orange_east = self.get_cell_value(i, j, "east")
        orange_west = self.get_cell_value(i, j, "west")
        orange_north_east = self.get_cell_value(i, j, "northeast")
        orange_north_west = self.get_cell_value(i, j, "northwest")
        orange_south_east = self.get_cell_value(i, j, "northeast")
        orange_south_west = self.get_cell_value(i, j, "northwest")
        
        empty_cell = OrangeState.VOID
        if orange_north == empty_cell and orange_south == empty_cell and \
            orange_east == empty_cell and orange_west == empty_cell and \
            orange_north_east == empty_cell and orange_north_west == empty_cell and \
            orange_south_east == empty_cell and orange_south_west == empty_cell:
            return True
        else:
            return False

    def get_largest_neighbour(self, i, j):
        orange_north = self.get_cell_value(i, j, "north")
        orange_south = self.get_cell_value(i, j, "south")
        orange_east = self.get_cell_value(i, j, "east")
        orange_west = self.get_cell_value(i, j, "west")
        orange_north_east = self.get_cell_value(i, j, "northeast")
        orange_north_west = self.get_cell_value(i, j, "northwest")
        orange_south_east = self.get_cell_value(i, j, "northeast")
        orange_south_west = self.get_cell_value(i, j, "northwest")

        return max([orange_north, orange_south, orange_east, orange_south,
            orange_north_east, orange_north_west, orange_south_east, orange_south_west])

    def get_time_to_rot(self):
        time_to_rot = 0
        for i in range(0, self.no_of_rows):
            for j in range(0, self.no_of_cols):
                fresh_orange = (array[i][j] == OrangeState.FRESH)
                if fresh_orange and self.can_rot_immediately(i, j):
                    array[i][j] = OrangeState.ROTTEN + 1
                    time_to_rot = 1 if time_to_rot == 0 else time_to_rot
                elif fresh_orange and self.cannot_rot_at_all(i, j):
                    return -1
                elif fresh_orange:
                    largest_neighbour = self.get_largest_neighbour(i, j)
                    time_to_rot = largest_neighbour - 1 if time_to_rot < largest_neighbour else time_to_rot

        return -1 if time_to_rot == 0 else time_to_rot


# Note: I have not considered the complexity for the input.
# The complexity is only considered for the processing of the actual problem which is O(m * n)
# Also note that there is minimal or no error handling, so expect failures for some scenrios
if __name__ == "__main__":
    no_of_test_cases = int(input())
    test_cases = []
    for i in range(0, no_of_test_cases):
        m, n = tuple(map(int, input().split()))
        oranges = input()
        array = []
        row_start = 0
        for idx in range(0, m):
            # get each row from the line
            row = oranges[row_start:(row_start + n + n - 1)].split()
            # convert the row, which is string to list so that a 2D array is created.
            array.append(list(map(int, row)))
            row_start += 2 * n   # n spaces
        test_cases.append(array)

    print("Output:")
    for array in test_cases:
        m, n = len(array), len(array[0])
        orange_matrix = TheOrangeMatrix(array, m, n)
        print(orange_matrix.get_time_to_rot())
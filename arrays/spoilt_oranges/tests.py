from spoilt_oranges import TheOrangeMatrix
def test_1():
    array = [
        [1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1]
    ]
    oranges_matrix = TheOrangeMatrix(array, 7, 7)
    assert oranges_matrix.get_time_to_rot() == -1

def test_2():
    array = [
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    oranges_matrix = TheOrangeMatrix(array, 7, 7)
    assert oranges_matrix.get_time_to_rot() == 3

def test_3():
    array = [
        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 2]
    ]
    oranges_matrix = TheOrangeMatrix(array, 7, 7)
    assert oranges_matrix.get_time_to_rot() == 6

def test_4():
    array = [
        [2, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 2]
    ]
    oranges_matrix = TheOrangeMatrix(array, 7, 7)
    assert oranges_matrix.get_time_to_rot() == 4

def test_5():
    array = [
        [2, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1]
    ]
    oranges_matrix = TheOrangeMatrix(array, 7, 7)
    assert oranges_matrix.get_time_to_rot() == 6

def test_6():
    array = [
        [2, 1, 0, 2, 1],
        [1, 0, 1, 2, 1],
        [1, 0, 0, 2, 1]
    ]
    oranges_matrix = TheOrangeMatrix(array, 3, 5)
    assert oranges_matrix.get_time_to_rot() == 2

def test_7():
    array = [
        [2, 1, 0, 2, 1],
        [0, 0, 1, 2, 1],
        [1, 0, 0, 2, 1]
    ]
    oranges_matrix = TheOrangeMatrix(array, 3, 5)
    assert oranges_matrix.get_time_to_rot() == -1
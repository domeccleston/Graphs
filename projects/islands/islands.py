from util import Stack
# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An isand consists of 1s that are connect to the north, south, east, or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

def get_neighbours(row, col, matrix):

    neighbours = []
    # check north
    if row > 0 and matrix[row-1][col] == 1:
        neighbours.append( (row-1, col) )
    # check south
    if row < len(matrix) - 1 and matrix[row+1][col] == 1:
        neighbours.append( (row+1, col) )
    # check east
    if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
        neighbours.append( (row, col+1) )
    # check west
    if col > 0 and matrix[row][col-1] == 1:
        neighbours.append( (row, col-1) )
    
    return neighbours

def dft(start_row, start_col, matrix, visited):

    s = Stack()

    s.push( (start_row, start_col) )

    while s.size() > 0:
        v = s.pop()
        row = v[0]
        col = v[1]
        if not visited[row][col]:
            visited[row][col] = True

            for neighbour in get_neighbours(row, col, matrix):
                s.push(neighbour)
    
    return visited
       

def island_counter(matrix):
    visited = []
    island_count = 0

    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    visited = dft(row, col, matrix, visited)
                    island_count += 1

    return island_count


print(island_counter(islands))
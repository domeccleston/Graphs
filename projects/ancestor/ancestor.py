from util import Queue

def bfs(vertices, starting_vertex):
    # create a queue to hold the vertex ids
    q = Queue()
    # enqueue the start vertex id
    q.enqueue( [starting_vertex] ) 
    # create an empty visited set
    visited = set()
    # while the queue is not empty
    while q.size() > 0:
        # set vert to the dequeued element
        path = q.dequeue()
        last_vertex = path[-1]
        # if the vert is not in visited
        if last_vertex not in visited:
            # add the vert to visited set
            visited.add(last_vertex)

            # if node has no ancestors
            if not last_vertex in vertices:
                if last_vertex == starting_vertex:
                    return -1
                return path[-1]

            neighbours = vertices[last_vertex]

            smallest_neighbour = min(neighbours)
            path_copy = list(path)
            path_copy.append(smallest_neighbour)
            # enqueue the next vert
            q.enqueue(path_copy)
    # return False
    return visited[-1]


def earliest_ancestor(ancestors, starting_node):
    # build graph with adjacency list
    vertices = {}
    
    for ancestor in ancestors:
        vertices[ancestor[1]] = set()
    
    for ancestor in ancestors:
        vertices[ancestor[1]].add(ancestor[0])
    
    return bfs(vertices, starting_node)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 4))
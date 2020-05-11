"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            current_vertex = q.dequeue()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)

                for neighbor in self.get_neighbors(current_vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            current_vertex = s.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)

                for neighbor in self.get_neighbors(current_vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):

        print(starting_vertex)

        visited.add(starting_vertex)
    
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex_id, target_value):
        # create a queue to hold the vertex ids
        q = Queue()
        # enqueue the start vertex id
        q.enqueue([starting_vertex_id])
        # create an empty visited set
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # set vert to the dequeued element
            vert = q.dequeue()
            last_vertex = vert[-1]
            # if the vert is not in visited
            if last_vertex not in visited:
                # if vert is target value
                if last_vertex == target_value:
                    # return True
                    return vert
                # add the vert to visited set
                visited.add(last_vertex)
                # loop over next vert in the vertices at the index of vert
                for next_vert in self.vertices[last_vertex]:
                    paths = list(vert)
                    paths.append(next_vert)
                    # enqueue the next vert
                    q.enqueue(paths)
        # return False
        return False

    def dfs(self, starting_vertex_id, target_value):

        s = Stack()

        s.push([starting_vertex_id])
        # create an empty visited set
        visited = set()
        # while the queue is not empty
        while s.size() > 0:
            vert = s.pop()
            last_vertex = vert[-1]
            # if the vert is not in visited
            if last_vertex not in visited:
                # if vert is target value
                if last_vertex == target_value:
                    # return True
                    return vert
                # add the vert to visited set
                visited.add(last_vertex)
                # loop over next vert in the vertices at the index of vert
                for next_vert in self.vertices[last_vertex]:
                    paths = list(vert)
                    paths.append(next_vert)
                    # enqueue the next vert
                    s.push(paths)
        # return False
        return False

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        
        if visited is None:
            visited = set()

        if path is None:
            path = list()

        visited.add(starting_vertex) 

        path_copy = path.copy()

        path_copy.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path_copy

        for neighbor in self.get_neighbors(starting_vertex):
            new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
            if new_path:
                return new_path
            return None






#     def dfs_recursive(self, start_vert, target_value):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.

#         This should be done using recursion.
#         """
#         visited = set()
#         # add start vert to visited
#         visited.add(start_vert)
#         # if the start vert is equal to the target value
#         if start_vert == target_value:
#             # return True
#             return True
#         # loop over every child vertex in vertices set at the start vertex
#         for child_vert in self.vertices[start_vert]:
#             # if child vert is not in visited
#             if child_vert not in visited:
#                 # if the recursive call to dfs
#                 if self.dfs(child_vert, target_value):
#                     # return True
#                     return True
#         # Return False
#         return False


# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
#     graph.bft(1)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     graph.dft(1)
#     graph.dft_recursive(1)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))

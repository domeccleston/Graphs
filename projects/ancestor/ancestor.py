
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
                s.enqueue(paths)
    # return False
    return False


def earliest_ancestor(ancestors, starting_node):
    # 


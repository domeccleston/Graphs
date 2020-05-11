import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append( (user_id, friend_id ))
        
        random.shuffle(possible_friendships)
        
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # Create friendships
    
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
                for next_vert in self.friendships[last_vertex]:
                    paths = list(vert)
                    paths.append(next_vert)
                    # enqueue the next vert
                    q.enqueue(paths)
        # return False
        return False


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        neighbours = self.friendships[user_id]
        print(neighbours)

        # create a queue to hold the vertex ids
        q = Queue()
        # enqueue the start vertex id
        q.enqueue([user_id])

        # while the queue is not empty
        while q.size() > 0:
            # set vert to the dequeued element
            path = q.dequeue()
            last_vertex = path[-1]
            # if the vert is not in visited
            if last_vertex not in visited:
                visited[last_vertex] = path
                # loop over next vert in the vertices at the index of vert
                for neighbour in self.friendships[last_vertex]:
                    new_path = list(path)
                    new_path.append(neighbour)
                    # enqueue the next vert
                    q.enqueue(new_path)
        # return False
        return visited

        # for each user (self.friendships.keys)
            # do a breadth first traversal for that user
            # return a path
        # return a dict mapping users to paths


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    # print(sg.friendships)
    sg.get_all_social_paths(1)
    # print(connections)
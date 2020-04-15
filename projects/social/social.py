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

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i + 1}")


        # Create friendships
        # Generate all possible friendships
        possible_friendships = []

        # avoid dupes by making sure first number is smaller than second
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))
        
        # random seed for testing code
        # random.seed(a=2020)

        # shuffle all possible friendships
        random.shuffle(possible_friendships)

        # create for first X pairs x is total // 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Pseudo code notes
        # loop while queue is non empty

        # get user
        # add user to path
        # add user-path pair to visited if the user has not already been added, 

        # get user's direct friends (self.friendships[user])
        # and add them to the queue with the current path

        visited = {}  # Note that this is a dictionary, not a set
        q = []
        # structure of items in q is: (user, list(path_to_user))
        q.append((user_id, []))
        while len(q) > 0:
            # get (user, path_to_user) node
            node = q.pop(0)
            # user is the first thing in a node
            user = node[0]
            # path is the second thing in a node
            path = node[1].copy()
            # add the current user the path to itself
            path.append(user)
            if user not in visited.keys():
                # if this user isn't already in our dictionary of users, add it and its path
                visited[user] = path

            # add all friends of current user to the queue 
                # user's direct friends, connections is a set()
            friends = self.friendships[user]
            for friend in friends:
                # make sure we don't double up on friends
                if friend not in visited.keys():
                    # queue the friend, with the path up to this point 
                    # This has the effect of adding the friend to its own path
                        # when it comes up in the queue
                    q.append((friend, path))

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    num_users = 10
    avg_friends = 2
    user = 1

    sg.populate_graph(num_users, avg_friends)

    # Print all connections
    print("Friendships: \n", sg.friendships)
    connections = sg.get_all_social_paths(user)
    print("Connections: \n", connections)

    def percent_connected_and_avg_path_length(sg, num_users):

        # Print average percentage of tree that is connected and average path length
        avg = 0
        path_avg = 0
        for user in range(num_users):
            # get connections for the user we are currently on
            connections = sg.get_all_social_paths(user + 1)
            num_connections = len(connections)
            # print("Connections: \n", connections)
            # count people not in the keys of connections
            count = 0
            # keep track of average path length
            path_length = 0
            # loop through all users, checking connections with current user
            for i in range(num_users):
                if i+1 not in connections.keys():
                    pass
                    # print(i)
                    # count people not connected
                else:
                    count += 1
                    # get path length of people who are connected
                    path = connections[i+1]
                    # print(path)
                    # add path length to sum of path lengths
                    path_length += len(path)
            # get average path length for the current user
            path_avg += path_length/num_connections
            # print(f"Total people in network not connected to {user}: {count}")
            avg += count
        avg = avg/num_users
        path_avg = path_avg/num_users
        print(f"Average people not connected to a given user: {num_users - avg}")
        print(f"Average Percentage of people connected to a given user: {(avg/num_users * 100)}")
        print(f"Average path length between connected people: {path_avg}")
    
    percent_connected_and_avg_path_length(sg, num_users)

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
        # create key for the vertex in the dictionary, with an empty set as value
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if the two verticies are in the graph
        if v1 in self.vertices and v2 in self.vertices:
            # add the connected vertex to the set of the first vertex
            self.vertices[v1].add(v2)
        else:
            print("Error: inputed verticies not found in vertex set")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create queue
        queue = Queue()
        # create visited set
        visited = set()
        # add starting vertex to queue
        queue.enqueue(starting_vertex)
        # loop until the queue is empty
        while queue.size() > 0:
            # dequeue the first node
            node = queue.dequeue()
            # if the node hasn't been visited, add node to visited and print the node, and enqueue unvisted children
            if node not in visited:
                visited.add(node)
                print(node)
                # enqueue any unvisited neighbors of the node
                for child in self.vertices[node]:
                    if child not in visited:
                        queue.enqueue(child)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create stack
        stack = Stack()
        # created a set of visited nodes
        visited = set()
        # add the first node to the stack
        stack.push(starting_vertex)
        # loop until the stack is empty
        while stack.size() > 0:
            # pop the last element
            node = stack.pop()
            # print unvisited nodes, add unvisited nodes to visited, add their unvisited children to stack
            if node not in visited:
                print(node)
                visited.add(node)
                # add unvisited children to the stack
                for child in self.vertices[node]:
                    if child not in visited:
                        stack.push(child)
    
    def dft_recursive_visited(self, node, visited):
        """
        Helper function for dft_recursive.
        Calls itself, 
        updates an inputed set of visited nodes given it by dft_recursive
        """
        # add current node to the set of visited nodes
        visited.add(node)
        # print the current node
        print(node)
        # recur this function on any unvisited neighbors
        for neighbor in self.vertices[node]:
            if neighbor not in visited:
                self.dft_recursive_visited(neighbor, visited)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        Keeps a set of visited nodes for dft_recursive_visited to use as a reference
        """
        # instantiate visited set
        visited = set()
        # run the helper function
        self.dft_recursive_visited(starting_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create queue
        queue = Queue()
        # create visited set
        visited = set()
        # add list containing the starting vertex to queue
        queue.enqueue([starting_vertex])
        # loop until the queue is empty
        while queue.size() > 0:
            # dequeue the first path
            path = queue.dequeue()
            if path[-1] == destination_vertex:
                return path
            # if the node hasn't been visited, add node to visited and print the node, and enqueue unvisted children
            if path[-1] not in visited:
                visited.add(path[-1])
                # enqueue any unvisited neighbors of the node
                for child in self.vertices[path[-1]]:
                    if child not in visited:
                        new_path = list(path)
                        new_path += [child]
                        queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create stack
        stack = Stack()
        # create visited set
        visited = set()
        # add list containing the starting vertex to stack
        stack.push([starting_vertex])
        # loop until the stack is empty
        while stack.size() > 0:
            # pop the first path
            path = stack.pop()
            # if the current path ends in the destination vertex, return the path
            if path[-1] == destination_vertex:
                return path
            # if the node hasn't been visited, add node to the end of current path
            visited.add(path[-1])
            # push paths ending in any unvisited neighbors of the node onto the stack
            for child in self.vertices[path[-1]]:
                if child not in visited:
                    new_path = list(path)
                    new_path += [child]
                    stack.push(new_path)

    def dfs_recursive(self, vertex, destination_vertex, path=None, visited=None):
        # instantiate the path
        if not path:
            path = list()
        # instantiate our visited set
        if not visited:
            visited = set()
        # check if we've already been to this vertex
        if vertex not in visited:
            # add vertex to the path
            new_path = path + [vertex]
            # add vertex to visited
            visited.add(vertex)
            # base case: we've found our destination vertex, return the path to it
            if vertex == destination_vertex:
                return new_path
            # recurse over each neighbor
            for neighbor in self.get_neighbors(vertex):
                # do the recursion
                path_or_none = self.dfs_recursive(neighbor, destination_vertex, new_path, visited)
                # then return the path if it exists
                if path_or_none:
                    return path_or_none


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

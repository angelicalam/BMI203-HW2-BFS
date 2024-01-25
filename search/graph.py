import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # Raise ValueError if graph is empty
        # or a nonexistent start/end node is given
        if self.graph.number_of_nodes() == 0:
            raise ValueError(f"Graph object is empty.")
        if not self.graph.has_node(start):
            raise ValueError(f"{start} is not an existing node.")
        if end and not self.graph.has_node(end):
            raise ValueError(f"{end} is not an existing node.")
        
        # If the end node is the start node
        if start == end:
            return [start]
        
        # Although python has its own implementation of a queue object,
        # here I use a list as if it were a first-in first-out queue
        q = []
        visited = []
        q.append(start)
        visited.append(start)

        # Because [visited] will record nodes not in the shortest path,
        # links serves as a pseudo- reverse direction graph.
        if end:
            links = [[None, start]]

        # while the queue is not empty
        while len(q) > 0:
            # Pop the first element out
            v = q[0]
            q = q[1:]
            # Get the neighbors of node v
            N = list(self.graph.neighbors(v))
            for w in N:
                if w not in visited:
                    # Add w to the traversed nodes
                    visited.append(w)
                    # Add w to the end of the queue
                    q.append(w)

                    # If there is an end node input, 
                    # BFS needs to stop when the end node is visited,
                    # and it needs to trace the shortest path via 
                    # node n --> node n-1
                    if end:
                        links.append([v, w])
                    if w == end:
                        q = []  # Empty queue so that outer while loop breaks
                        break
                    
        if end:
            # Pop off last element of links
            prev, current = links[-1]
            links = links[:-1]
            if current != end:
                # Path to the end node does not exist
                return None
            else:
                # Trace the shortest path by following the pseudo-
                # reverse direction graph represented in links.
                shortest_path = [prev, current]
                while prev != start:
                    # Pop last element of links and check if it
                    # has the earliest element in shortest_path
                    if prev == links[-1][1]:
                        shortest_path = [links[-1][0]] + shortest_path
                        prev, current = links[-1]
                    links = links[:-1]
                return shortest_path
        
        else:
            # If no end node is provided return the order of BFS traversal
            return visited

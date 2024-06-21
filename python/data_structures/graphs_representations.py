class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0]*num_vertices for _ in range(num_vertices)]
        self.adjacency_list = [[] for _ in range(num_vertices)]
        self.edge_list = []
        
    def add_edge(self, u, v):
        # Update adjacency matrix
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1  # Assuming it's an undirected graph
        
        # Update adjacency list
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
        
        # Update edge list
        self.edge_list.append((u, v))
    
    def display_adjacency_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)
    
    def display_adjacency_list(self):
        print("Adjacency List:")
        for index, neighbors in enumerate(self.adjacency_list):
            print(f"{index}: {neighbors}")
    
    def display_edge_list(self):
        print("Edge List:")
        print(self.edge_list)

# Create a graph with 5 vertices
graph = Graph(5)

# Add some edges
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

# Display the graph representations
graph.display_adjacency_matrix()
graph.display_adjacency_list()
graph.display_edge_list()

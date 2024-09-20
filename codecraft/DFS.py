# Function to perform DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(start)
    print(start, end=' ')  # For displaying the traversal order
    
    # Recursively visit all the adjacent vertices
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform DFS starting from vertex 'A'
dfs(graph, 'A')
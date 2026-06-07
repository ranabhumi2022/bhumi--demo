def dfs(graph, node, visited): 
    if node not in visited: 
        print(node, end=" ") 
        visited.add(node) 
    for neighbor in graph[node]: 
        dfs(graph, neighbor, visited) 
# Graph representation 
graph = { 
'A': ['B', 'C'], 
'B': ['D', 'E'], 
'C': ['F'], 
'D': [], 
'E': [], 
'F': [] 
} 
visited = set() 
print("DFS Traversal:") 
dfs(graph, 'A', visited)
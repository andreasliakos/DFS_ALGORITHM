def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for i in graph[node]:
            dfs(graph,i, visited)
    return visited
 

if __name__ == '__main__':
    graph = {
    'A' : ['B','C'],
    'B' : ['A'],
    'C' : ['D','E','B'],
    'D' : ['C','E'],
    'E' : ['E']   
}
    visited = dfs(graph,'A', [])
    print(visited)

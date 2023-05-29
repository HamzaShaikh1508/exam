graph={
 'L':['M','N','O'],
 'M':['N','O'],
 'N':['P'],
 'O':[],
 'P':[]
}
visited=set() #set to keep track of visited nodes of graph.
def dfs(visited, graph, node): #function for dfs
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
#driver code
print("Following is the Depth First Search:")
dfs(visited,graph,'L')

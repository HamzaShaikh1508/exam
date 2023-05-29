graph={
    'L':['M','N','O'],
    'M':['N','O'],
    'N':['P'],
    'O':[],
    'P':[]
}
visited=[] #list for visited nodes
queue=[] #initialize a queue
def bfs(visited, graph, node): #function for BFS
    visited.append(node)
    queue.append(node)
 
    while queue: #creating loop to visit each node
        m=queue.pop(0)
        print(m)
 
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
 
#driver code
print("Following is the Breadth First Search:")
bfs(visited, graph, 'L') #function calling
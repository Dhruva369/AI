#Depth-First Search

#adjacency list (neighbouring nodes)
graph = {
          'A':['B','C'],
          'B':['D','E'],
          'C':['F'],
          'D':[],
          'E':['F'],
          'F':[],
        }

#initializing empty set for visited nodes (can also use list)
visited = set()

#dfs function
def dfs(visited, graph, node):

  if node not in visited:   #if node not yet visited then print it and add it to the set
    print(node, end=' ')
    visited.add(node)

    for neighbour in graph[node]:   #visit the neighbours of the current node
      dfs(visited, graph, neighbour)  #system stack to keep track of nodes

print("Following is the Depth-First Search\n")
dfs(visited, graph, 'A')  #dfs function call

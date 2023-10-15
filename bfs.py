#Breadth-First Search

#adjaceny list (neighbouring nodes)
graph = {
          'P':['Q','R','S'],
          'Q':['P','R'],
          'R':['P','Q','T'],
          'T':['R'],
          'S':['P'],
        }

#initializing two empty lists for visited nodes and the queue (nodes to be visisted)
visited = []
queue = []

#bfs function
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:         #till the queue is not empty
    s = queue.pop(0)
    print(s, end=' ')      #printing the current traversal node

    for neighbour in graph[s]:      #visiting the neighbouring nodes of current node
      if neighbour not in visited:    #if neighbour not yet visited then put it in queue and visited list
        visited.append(neighbour)
        queue.append(neighbour)

print('Following is the Breadth-First Search\n')
bfs(visited, graph, 'P')  #bfs function call

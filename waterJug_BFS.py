#water jug problem using BFS

from collections import deque

def bfs(a, b, target, jug):
 
    visited = {}
    isSolvable = False
    path = []
 
    q = deque()
 
    q.append((0, 0))
 
    while len(q) > 0:
 
        u = q.popleft()
 
        if (u[0], u[1]) in visited:  #if already visited then skip
            continue
 
        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:  #checking for overflow or underflow
            continue
 
        path.append([u[0], u[1]])
 
        visited[(u[0], u[1])] = 1

      #if one of the jug has reached the target
        if u[0] == target or u[1] == target:
            isSolvable = True

         #if jug A has reached the target
            if u[0] == target:
              if jug=='a':  #if jug A the selected jug
                if u[1] != 0:
                  path.append([u[0], 0])
              else:         #if jug B is the selected jug
                if u[1] != 0:
                  path.append([u[0], 0])
                path.append([0, u[0]])

        #if jug A has reached the target
            else:
              if jug=='b':   #if jug B is the selected jug
                if u[0] != 0:
                  path.append([0, u[1]])
              else:          #if jug A the selected jug
                if u[0] != 0:  
                  path.append([0, u[1]])
                path.append([u[1], 0])

 
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",", path[i][1], ")")
            break
 
        q.append([u[0], b])  # Fill Jug B
        q.append([a, u[1]])  # Fill Jug A
 
        for i in range(max(a, b) + 1):
 
            c = u[0] + i
            d = u[1] - i
 
            if c == a or (d == 0 and d >= 0):
                q.append([c, d])
 
            c = u[0] - i
            d = u[1] + i
 
            if (c == 0 and c >= 0) or d == b:
                q.append([c, d])
 
        q.append([a, 0])
        q.append([0, b])
    if not isSolvable:
        print('\nNo Solution')


a=int(input("\nCapacity of Jug A: "))
b=int(input("\nCapacity of Jug B: "))
jug=input('\nChoose a Jug (A or B) to enter final state: ').lower()
target=int(input(f'\nEnter final state of Jug {jug.upper()}: '))

bfs(a,b,target,jug)

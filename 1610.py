
# Python3 implementation of the approach 
  
# Graph class 
class Graph: 
    def __init__(self, v): 
  
        # No. of vertices of graph 
        self.v = v 
  
        # Adjacency List 
        self.l = [0] * v 
        for i in range(self.v): 
            self.l[i] = [] 
  
    def addedge(self, i: int, j: int): 
        self.l[i].append(j) 
        self.l[j].append(i) 
  
# Function to find a cycle in the given graph if exists 
def findCycle(n: int, e: int, g: Graph) -> None: 
  
    # HashMap to store the degree of each node 
    degree = dict() 
  
    for i in range(len(g.l)): 
        degree[i] = len(g.l[i]) 
  
    # Array to track visited nodes 
    visited = [0] * g.v 
  
    # Initially all nodes are not visited 
    for i in range(len(visited)): 
        visited[i] = 0
  
    # Queue to store the nodes of degree 1 
    q = list() 
  
    # Continuously adding those nodes whose 
    # degree is 1 to the queue 
    while True: 
  
        # Adding nodes to queue whose degree is 1 
        # and is not visited 
        for i in range(len(degree)): 
            if degree[i] == 1 and visited[i] == 0: 
                q.append(i) 
  
        # If queue becomes empty then get out 
        # of the continuous loop 
        if len(q) == 0: 
            break
  
        while q: 
  
            # Remove the front element from the queue 
            temp = q.pop() 
  
            # Mark the removed element visited 
            visited[temp] = 1
  
            # Decrement the degree of all those nodes 
            # adjacent to removed node 
            for i in range(len(g.l[temp])): 
                value = degree[g.l[temp][i]] 
                degree[g.l[temp][i]] = value - 1
  
    flag = 0
  
    # Checking all the nodes which are not visited 
    # i.e. they are part of the cycle 
    for i in range(len(visited)): 
        if visited[i] == 0: 
            flag = 1
  1
    if flag == 0: 
        print("NAO") 
    else: 
        print("SIM")
     
# Driver Code 
if __name__ == "__main__": 
  
    t = int(input())
    while t > 0:
        t-=1
        n,e = map(int, input().split())
        g = Graph(n)
        for x in range(e):
            a, b = map(int, input().split())
            g.addedge(a-1, b-1)
        findCycle(n,e,g)
        


   

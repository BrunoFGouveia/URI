# Python program to check if a given directed graph is strongly  
# connected or not 
  
from collections import defaultdict 
   
#This class represents a directed graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
      
   
    #A function used by isSC() to perform DFS 
    def DFSUtil(self,v,visited): 
  
        # Mark the current node as visited  
        visited[v]= True
  
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited) 
  
  
    # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
  
        g = Graph(self.V) 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
          
        return g 
  
          
    # The main function that returns true if graph is strongly connected 
    def isSC(self): 
  
        # Step 1: Mark all the vertices as not visited (For first DFS) 
        visited =[False]*(self.V) 
          
        # Step 2: Do DFS traversal starting from first vertex. 
        self.DFSUtil(0,visited) 
  
        # If DFS traversal doesnt visit all vertices, then return false 
        if any(i == False for i in visited): 
            return False
  
        # Step 3: Create a reversed graph 
        gr = self.getTranspose() 
          
        # Step 4: Mark all the vertices as not visited (For second DFS) 
        visited =[False]*(self.V) 
  
        # Step 5: Do DFS for reversed graph starting from first vertex. 
        # Staring Vertex must be same starting point of first DFS 
        gr.DFSUtil(0,visited) 
  
        # If all vertices are not visited in second DFS, then 
        # return false 
        if any(i == False for i in visited): 
            return False
  
        return True
  
while True:
    n, m = map(int , input().split())
    if n==0 and m==0:
        break 
    g1 = Graph(n)
    for x in range(m):
        v,w,p = map(int , input().split())
        g1.addEdge(v-1, w-1)
        if p == 2:
            g1.addEdge(w-1, v-1)
        
    if g1.isSC():
        print(1)
    else:
        print(0)        


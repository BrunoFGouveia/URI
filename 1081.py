     
class Graph: 
      
    # init function to declare class variables 
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
        
  
    def DFSUtil(self, temp, v, visited,space): 
  
        # Mark the current vertex as visited 
        visited[v] = True
  
        # Store the vertex to list 
        temp.append(v) 
        
        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.adj[v]:
            a = ''
            for x in range(space):
                a+=' '

            if visited[i] == False: 
               
                
               
                print('{}{}-{} pathR(G,{})'.format(a,v,i,i)) 

                # Update the list 
                temp = self.DFSUtil(temp, i, visited,space+2) 
            else:
                print('{}{}-{}'.format(a,v,i))  
             
        return temp 
  
    # method to add an undirected edge 
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
  
    # Method to retrieve connected components 
    # in an undirected graph 
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited,2)) 
                print()          
        return cc 

    
# Driver Code 
if __name__=="__main__": 
      
    t = int(input())
    caso = 0
    while t > caso:
        caso+=1
        
        m,n = map(int, input().split())
        ls = []
        g = Graph(m); 
        for x in range(n):
            o,d = map(int,input().split())

            g.addEdge(o,d)
        if caso>1:
            print()    
        print('Caso {}:'.format(caso))


        
        cc = g.connectedComponents() 
       

    

    
# Python code to count the singleton sub-graphs 
# in a disconnected graph 

# Function to compute the count 
def compute(graph, N): 
	# Storing intermediate result 
	count = 0
	
	# Traversing the Nodes 
	for i in range(1, N+1): 
	
		# Singleton component 
		if (len(graph[i]) == 0): 
			count += 1	
	
	# Returning the result 
	return count 
	
# Driver 
if __name__ == '__main__': 

    t = int(input())
    caso = 0
    while t > caso:
        caso+=1
        N = int(input())
        graph = [[] for i in range(N+1)]
        M = int(input())
        for i in range(M):
            x,y = map(int, input().split())
            graph[x].append(y)
        calc = compute(graph, N)
        if (calc>1):
            print('Caso #{}: ainda falta(m) {} estrada(s)'.format(caso,calc-1))
        else:
            print('Caso #{}: a promessa foi cumprida'.format(caso))


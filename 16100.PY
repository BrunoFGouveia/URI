# A Python3 program to check if there is a cycle in 
# directed graph using BFS. 
import math 
import sys 
from collections import defaultdict 

# Class to represent a graph 
class Graph: 
	def __init__(self,vertices): 
		self.graph=defaultdict(list) 
		self.V=vertices # No. of vertices' 
	
	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

# This function returns true if there is a cycle 
# in directed graph, else returns false. 
def isCycleExist(n,graph): 

	# Create a vector to store indegrees of all 
	# vertices. Initialize all indegrees as 0. 
	in_degree=[0]*n 

	# Traverse adjacency lists to fill indegrees of 
	# vertices. This step takes O(V+E) time 
	for i in range(n): 
		for j in graph[i]: 
			in_degree[j]+=1
	
	# Create an queue and enqueue all vertices with 
	# indegree 0 
	queue=[] 
	for i in range(len(in_degree)): 
		if in_degree[i]==0: 
			queue.append(i) 
	
	# Initialize count of visited vertices 
	cnt=0

	# One by one dequeue vertices from queue and enqueue 
	# adjacents if indegree of adjacent becomes 0 
	while(queue): 

		# Extract front of queue (or perform dequeue) 
		# and add it to topological order 
		nu=queue.pop(0) 

		# Iterate through all its neighbouring nodes 
		# of dequeued node u and decrease their in-degree 
		# by 1 
		for v in graph[nu]: 
			in_degree[v]-=1

			# If in-degree becomes zero, add it to queue 
			if in_degree[v]==0: 
				queue.append(v) 
		cnt+=1

	# Check if there was a cycle 
	if cnt==n: 
		return False
	else: 
		return True
		

# Driver program to test above functions 
if __name__=='__main__': 

	
    t = int(input())
    while t > 0:
        t-=1
        n,e = map(int, input().split())
        g = Graph(n)
        for x in range(e):
            a, b = map(int, input().split())
            g.addEdge(a-1, b-1)
        if isCycleExist(g.V,g.graph):
            print("SIM")
        else:
            print("NAO")
        


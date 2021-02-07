
# This code is contributed by Neelam Yadav
# Python program to print topological sorting of a DAG 
from collections import defaultdict 


# topolicical sort was implimented from from https://www.geeksforgeeks.org/topological-sorting/
# start of Neelam Yadev's code
#Class to represent a graph 
class Graph: 
	def __init__(self,vertices): 
		self.graph = defaultdict(list) #dictionary containing adjacency List 
		self.V = vertices #No. of vertices 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# A recursive function used by topologicalSort 
	def topologicalSortUtil(self,v,visited,stack): 

		# Mark the current node as visited. 
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Push current vertex to stack which stores result 
		stack.insert(0,v) 

	# The function to do Topological Sort. It uses recursive 
	# topologicalSortUtil() 
	def topologicalSort(self): 
		# Mark all the vertices as not visited 
		visited = [False]*self.V 
		stack =[] 

		# Call the recursive helper function to store Topological 
		# Sort starting from all vertices one by one 
		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Print contents of stack 
		print(stack) 
# end of Neelam Yadev's code

class DAG:
	def makeEdges(self, dagList):
		DAG = []#dag list
		#takes in a list and cleans the input before giving it to the topsort
		splitList = dagList.replace('[','').replace(']','').replace('(','').replace(')','').split(',')
		for edge in splitList:
			if edge[0] == ' ': edge = edge[1:]
			if edge[len(edge)-1] == ' ': edge = edge[:len(edge)-1]
			edge = edge.split(' ')
			DAG.append(edge)
			#print(edge)
		return DAG
		#print(DAG, len(DAG))
	def getTopSort(self, DAG):
		DAG_L = len(DAG)
		g = Graph(DAG_L)
		for edge in DAG:
			g.addEdge(edge[0],edge[1])
		print("Following is a Topological Sort of the given graph")
		g.topologicalSort() 

# this is the given input, spaces between the numbers are required 
dag1 = "[ (5 2), (5 0) , (4 0) , (4 1) , (2 3) , (3 1) ]"
# this creates a DAG object
DAG_OBJ = DAG()
# this will take in the string and split it accordingly for the
# resulting list to contain an edge which is also a list
DAG_LIST = DAG_OBJ.makeEdges(dag1)
# with the given edges, the function returns a topologically sorted list
DAG_OBJ.getTopSort(DAG_LIST)



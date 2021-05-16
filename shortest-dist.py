# Python3 implementation to find minimum
# spanning tree for adjacency representation.
from sys import maxsize
INT_MAX = maxsize
def initialise(V):
	global dis, Next

	for i in range(V):
		for j in range(V):
			dis[i][j] = graph[i][j]

			# No edge between node
			# i and j
			if (graph[i][j] == INF):
				Next[i][j] = -1
			else:
				Next[i][j] = j

def constructPath(u, v):
	global graph, Next
	
	# If there's no path between
	# node u and v, simply return
	# an empty array
	if (Next[u][v] == -1):
		return {}

	# Storing the path in a vector
	path = [u]
	while (u != v):
		u = Next[u][v]
		path.append(u)

	return path

# Standard Floyd Warshall Algorithm
# with little modification Now if we find
# that dis[i][j] > dis[i][k] + dis[k][j]
# then we modify next[i][j] = next[i][k]
def floydWarshall(V):
	global dist, Next
	for k in range(V):
		for i in range(V):
			for j in range(V):
				
				# We cannot travel through
				# edge that doesn't exist
				if (dis[i][k] == INF or dis[k][j] == INF):
					continue
				if (dis[i][j] > dis[i][k] + dis[k][j]):
					dis[i][j] = dis[i][k] + dis[k][j]
					Next[i][j] = Next[i][k]

# Prthe shortest path
def printPath(path):
	n = len(path)
	for i in range(n - 1):
		print(path[i], end=" -> ")
	print (path[n - 1])

# Returns true if edge u-v is a valid edge to be
# include in MST. An edge is valid if one end is
# already included in MST and other is not in MST.
def isValidEdge(u, v, inMST):
	if u == v:
		return False
	if inMST[u] == False and inMST[v] == False:
		return False
	elif inMST[u] == True and inMST[v] == True:
		return False
	return True

def primMST(cost):
	inMST = [False] * V1

	# Include first vertex in MST
	inMST[0] = True

	# Keep adding edges while number of included
	# edges does not become V-1.
	edge_count = 0
	mincost = 0
	while edge_count < V1 - 1:

		# Find minimum weight valid edge.
		minn = INT_MAX
		a = -1
		b = -1
		for i in range(V1):
			for j in range(V1):
				if cost[i][j] < minn:
					if isValidEdge(i, j, inMST):
						minn = cost[i][j]
						a = i
						b = j

		if a != -1 and b != -1:
			print("Edge %d: (%d, %d) cost: %d" %
				(edge_count, a, b, minn))
			printPath(constructPath(a,b))
			edge_count += 1
			mincost += minn
			inMST[b] = inMST[a] = True

	print("Minimum cost = %d" % mincost)

# Driver Code
if __name__ == "__main__":
	''' Let us create the following graph
		2 3
	(0)--(1)--(2)
	| / \ |
	6| 8/ \5 |7
	| /	 \ |
	(3)-------(4)
			9		 '''

	# Print the solution
	
	V=4
	MAXM,INF = 100,INT_MAX
	dis = [[-1 for i in range(MAXM)] for i in range(MAXM)]
	Next = [[-1 for i in range(MAXM)] for i in range(MAXM)]

	
	graph = [ [ 0, 3, INF, 7 ],
			[ 8, 0, 2, INF ],
			[ 5, INF, 0, 1 ],
			[ 2, INF, INF, 0 ] ]

	# Function to initialise the
	# distance and Next array
	initialise(V)
	#Calling Floyd Warshall Algorithm,
	# this will update the shortest
	# distance as well as Next array
	floydWarshall(V)
	required=[0,1,2]
	result= [[-1 for i in range(len(required))] for i in range(len(required))]
	global V1
	V1=len(required)
	for i in range(len(required)):
		for j in range(i,len(required)):
			result[i][j]=dis[required[i]][required[j]]
			result[j][i]=dis[required[j]][required[i]]
	print(result)
	primMST(result)
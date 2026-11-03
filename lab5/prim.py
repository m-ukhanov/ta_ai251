INF=float('inf') #infinity
V=8 # graph size
graph = [ # weighted adjacency matrix of a graph
	[INF, INF, 7, 3, INF, 6, INF, INF],
    [INF, INF, 2, 9, INF, 9, INF, INF],
    [7, 2, INF, INF, INF, INF, INF, 4],
    [3, 9, INF, INF, 5, INF, INF, INF],
    [INF, INF, INF, 5, INF, 4, 1, INF],
    [6, 9, INF, INF, 4, INF, 8, 7],
    [INF, INF, INF, INF, 1, 8, INF, 5],
    [INF, INF, 4, INF, INF, 7, 5, INF]
]

def prim(graph):
	selected = [False]*V # tracking vertices that are included in MST
	selected[0] = True # picking vertex 1 as starting

	total=0 # total weight
	mst=[]

	while len(mst) < V-1: # filling mst up until it contains V - 1 edges
		min_weight = INF
		x = y = -1

		for i in range(V): #checking vertices that are in the mst
			if selected[i]:
				for j in range(V): #checking vertices outside the mst
					# if not in the mst and has the minimal weight - saving the edge
					if not selected[j] and graph [i][j] < min_weight:  
						min_weight = graph[i][j]					  
						x,y=i,j
		if y==-1: 
			raise Exception("Граф не є зв'зяним")

		# adding the edge in the mst
		selected[y] = True
		mst.append((x+1,y+1, min_weight))
		total += min_weight

	for u,v,w in mst:
		print(f"({u},{v}) = {w}")
	print(f"Total weight: {total}")

prim(graph)

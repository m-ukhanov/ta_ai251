import heapq

INF=float('inf')
graph = [ # weighted adjacency matrix of a graph
	[0, INF, 7, 3, INF, 6, INF, INF],
    [INF, 0, 2, 9, INF, 9, INF, INF],
    [7, 2, 0, INF, INF, INF, INF, 4],
    [3, 9, INF, 0, 5, INF, INF, INF],
    [INF, INF, INF, 5, 0, 4, 1, INF],
    [6, 9, INF, INF, 4, 0, 8, 7],
    [INF, INF, INF, INF, 1, 8, 0, 5],
    [INF, INF, 4, INF, INF, 7, 5, 0]
]

def dijkstra(graph: list[list[float]], start: int) -> tuple[list[int], list[float]]:
	n = len(graph)
	#Init
	dist = [INF] * n
	pred = [-1] * n
	dist[start] = 0
	pq = [(0,start)]

	comps=0
	updates=0

	while pq: #Process vertices in order of their shortest known distance
		current_dist, u = heapq.heappop(pq)

		if current_dist>dist[u]: #Skip outdated entries in the prioirity queue
			continue

		for v,weight in enumerate(graph[u]): #Check all possible neighbors of u
			if weight == INF or u == v: #Skip missing
				continue

			comps+=1
			new_dist = dist[u]+weight
			if new_dist < dist[v]: #Update if shorter path is found
				dist[v] = new_dist
				pred[v] = u
				updates+=1
				heapq.heappush(pq, (new_dist,v))

	print(f"Starting vertex: {start + 1}")

	for v in range(n):
		if dist[v] == INF: 
			print(f"Vertex {v + 1}: no path")
			continue

		path = []
		current = v

		while current != -1: #Reconstruct the shortest path
			path.append(current + 1)
			current = pred[current]

		path.reverse()

		print(
			f"Vertex {v + 1}: "
			f"distance = {dist[v]}, "
			f"path = {' -> '.join(map(str, path))}"
		)

	print(f"\nComps: {comps}")
	print(f"Updates: {updates}")

	return pred, dist

def floyd(graph: list[list[float]]) -> list[list[float]]:
	n=len(graph)
	dist = [row.copy() for row in graph]
	comps=0
	updates=0

	for k in range(n): #k - intermediate vertex, i - starting vertex, j - destination vertex
		for i in range(n):
			for j in range(n):
				comps+=1
				new_dist = dist[i][k] + dist[k][j]

				if new_dist < dist[i][j]: #Update if the path through k is shorter
					dist[i][j] = new_dist
					updates+=1

	print("Shortest distance matrix:")
	for row in dist:
		print(" ".join(
			f"{'INF' if value == INF else int(value):>3}"
			for value in row
		))

	print(f"\nComps: {comps}")
	print(f"Updates: {updates}")

	return dist

print("Dijkstra's:")
dijkstra(graph, 0)

print("\n")
print("-"*64)
print("Floyd's:")
floyd(graph)
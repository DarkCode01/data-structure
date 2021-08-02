graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = []
queue = []

def bfs(visitedList: list, graph: dict, node: str):
	visited.append(node)
	queue.append(node)

	while queue:
		m = queue.pop(0)
		print(m)
		for adjacent in graph[m]:
      if adjacent not in visitedList:
          visitedList.append(adjacent)
          queue.append(adjacent)

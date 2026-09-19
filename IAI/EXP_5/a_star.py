import heapq

graph = {
    'S':[('A',7),('B',2),('C',3)],
    'A': [('B', 3), ('D', 4)],
    'B': [('H', 1), ('D', 4)],
    'C': [('L', 2)],
    'D': [('F', 5)],
    'E': [],
    'H':[('F',3),('G',2)],
    'L':[('I',4),('J',4)],
    'K':[('E',5)],
    'I':[('K',4)],
    'J':[('K',4)],
    'F':[],
    'G':[('E',2)]
}
h = {
    'S':10,
    'A': 9,
    'B': 7,
    'C': 8,
    'D': 8,
    'E': 0,
    'F':6,
    'G':3,
    'I':4,
    'J':4,
    'K':3,
    'L':6,
    'H':6
}

def a_star(start, goal):
    queue = [(h[start], 0, start)]
    cost = {start: 0}
    parent = {start: None}

    while queue:
        f, g, current = heapq.heappop(queue)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]

            return path[::-1], g

        for neighbor, edge in graph[current]:
            new_g = g + edge

            if neighbor not in cost or new_g < cost[neighbor]:
                cost[neighbor] = new_g
                f = new_g + h[neighbor]
                parent[neighbor] = current
                heapq.heappush(queue, (f, new_g, neighbor))

    return None, float('inf')
    
path, total_cost = a_star('S', 'E')
print("Path:", " -> ".join(path))
print("Cost:", total_cost)

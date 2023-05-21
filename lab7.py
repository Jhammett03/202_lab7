from collections import deque

class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjacent = {}
        self.visited = False
        self.distance = float('inf')
        self.previous = None

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setVisited(self):
        self.visited = True

    def setDistance(self, dist):
        self.distance = dist

    def setPrevious(self, prev):
        self.previous = prev

    def __str__(self):
        return str(self.id)


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def getVertex(self, key):
        return self.vertices.get(key)

    def addEdge(self, src, dest, weight=0):
        if src not in self.vertices:
            self.addVertex(src)
        if dest not in self.vertices:
            self.addVertex(dest)
        self.vertices[src].addNeighbor(self.vertices[dest], weight)

    def getVertices(self):
        return self.vertices.values()


def shortest_path(vertex):
    queue = deque()
    queue.append(vertex)
    vertex.setDistance(0)
    paths = [(vertex, [], 0)]  # (vertex, path, cost)
    visited = {vertex}

    while queue:
        current_vertex = queue.popleft()
        current_vertex.setVisited()

        for neighbor in current_vertex.getConnections():
            if neighbor not in visited:
                visited.add(neighbor)
                new_distance = current_vertex.distance + current_vertex.getWeight(neighbor)
                if new_distance < neighbor.distance:
                    neighbor.setDistance(new_distance)
                    neighbor.setPrevious(current_vertex)
                    queue.append(neighbor)

                    # Update paths
                    path = [neighbor.getId()]  # Start path with the current neighbor
                    v = neighbor
                    while v.previous is not None:
                        path.insert(0, v.previous.getId())  # Store vertices instead of edges
                        v = v.previous
                    paths.append((neighbor, path, new_distance))

    return paths


# Test the shortest_path function
graph = Graph()

# Add vertices
for i in range(1, 8):
    graph.addVertex("v" + str(i))

# Add edges
graph.addEdge("v1", "v2", 2)
graph.addEdge("v1", "v4", 1)
graph.addEdge("v2", "v4", 3)
graph.addEdge("v2", "v5", 10)
graph.addEdge("v3", "v1", 4)
graph.addEdge("v3", "v6", 5)
graph.addEdge("v4", "v5", 2)
graph.addEdge("v4", "v3", 2)
graph.addEdge("v4", "v6", 8)
graph.addEdge("v4", "v7", 4)
graph.addEdge("v5", "v7", 6)
graph.addEdge("v7", "v6", 1)

# Run shortest_path function on v1
result = shortest_path(graph.getVertex("v4"))


# Print the results
def get_vertex_id(item):
    return item[0].getId()


for vertex, path, cost in sorted(result, key=get_vertex_id):
    print((vertex.getId(), [v for v in path], cost))


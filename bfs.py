from collections import deque
from vertex import Vertex
from load_graph import load_graph


def bfs(start, end):
    
    vertices = load_graph("dartmouth_graph.txt")
    q = deque()
    q.append(start)
    
    while len(q) != 0:
        for adjacent_vertex in vertices[q[0]].list:
            if adjacent_vertex.back_pointer == None :
                q.append(adjacent_vertex.name)
                adjacent_vertex.back_pointer = vertices[q[0]]
        
        if q.popleft() == end:
            route = []
            end_vertex = vertices[end]
            while end_vertex.name != start:
                route.append(end_vertex)
                end_vertex = end_vertex.back_pointer
            route.append(vertices[start])

            return route
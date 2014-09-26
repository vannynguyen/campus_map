from cs1lib import *
from load_graph import load_graph
from bfs import bfs
from math import *

vertices = load_graph("dartmouth_graph.txt")

WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

def main():
    img = load_image("dartmouth_map")
    draw_image(img, 0, 0)
    
    start = None
    goal = None
    
    #initialize map with blue vertices
    for key in vertices:
        vertices[key].draw_vertex(0,0,1)
        for adjacent_vertex in vertices[key].list:
            vertices[key].draw_edge(adjacent_vertex, 0, 0, 1)
    
    while not window_closed(): 
        
        for key in vertices:
            if vertices[key].is_touched() and mouse_down():
                #reset map every time new starting vertex selected
                for generic_vertex in vertices:
                    vertices[generic_vertex].draw_vertex(0,0,1)
                    for adjacent_vertex in vertices[generic_vertex].list:
                        vertices[generic_vertex].draw_edge(adjacent_vertex, 0, 0, 1)
                
                #draw starting vertex        
                vertices[key].draw_vertex(1, 0, 0)
            
                start = key
                
        #check if start vertex selected        
        if start != None:        
            for key in vertices:
                if vertices[key].is_touched() and not vertices[start].is_touched():
                    goal = key
            
                    #start and goal vertices selected and start is not goal
                    if goal != None and start != goal:
                        for key in vertices:
                            vertices[key].draw_vertex(0,0,1)
                            for adjacent_vertex in vertices[key].list:
                                vertices[key].draw_edge(adjacent_vertex, 0, 0, 1)
                        path = bfs(start, goal)
                        if path != None:
                            for vertex in path:
                                if vertex != goal and vertex.back_pointer != None:
                                    vertex.draw_edge(vertex.back_pointer, 1, 0, 0)
                                    vertex.draw_vertex(1, 0, 0)
                        
        request_redraw()
        sleep(.02)
    
start_graphics(main, "Dartmouth map", WINDOW_WIDTH, WINDOW_HEIGHT)
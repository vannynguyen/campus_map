from cs1lib import *
from math import *
#CONSTANTS FOR VERTEX AND EDGE SIZE
v_size = 5
e_width = 2.5

class Vertex:
    #constructor
    def __init__(self, name, x_coord, y_coord):
        self.name = name
        self.x = int(x_coord)
        self.y = int(y_coord)
        self.list = []
        self.list_of_names = []
        self.back_pointer = None
  
    def __str__(self):
        s = ""
        index = 0
        while index < len(self.list_of_names):
            s+=str(self.list_of_names[index])
            if index + 1 < len(self.list_of_names):
                s+=", "
            index+=1
        #print self.list_of_names
        return self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: "+s
    
    def draw_vertex(self, r, g, b):
        #set fill color
        set_fill_color(r,g,b)
        #set stroke color
        set_stroke_color(r,g,b)
        #draw a single vertex
        draw_circle(self.x,self.y,v_size)
    
    def draw_edge(self, vertex_2, r, g, b):
        enable_smoothing()
        #set stroke color
        set_stroke_color(r,g,b)
        #set stroke width
        set_stroke_width(e_width)
        #draw edge from this vertex to another
        draw_line(self.x,self.y,vertex_2.x,vertex_2.y)
    
    def draw_adjacent(self, r, g, b):
        enable_smoothing()
        #set stroke color
        set_stroke_color(r,g,b)
        #set stroke width
        set_stroke_width(e_width)
        #loop over list of adjacent vertices and draw edges
        for generic_vertex in self.list:
            draw_line(self.x, self.y, generic_vertex.x, generic_vertex.y)
    
    def is_touched(self):
        #if distance of mouse position less than radius away from center of circle, mouse is touching vertex
        return abs(mouse_x() - self.x) < v_size and abs(mouse_y() - self.y) < v_size
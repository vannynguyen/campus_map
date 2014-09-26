from vertex import Vertex
def load_graph(filename):
    #dictionary of vertices
    vertices = {}
    #reading from file; fill dictionary with vertices
    in_file = open(filename, "r")
    for line in in_file:
        #strip away whitespace and then delimit semicolons
        clean_line = line.strip()
        info = clean_line.split(";")
        #separate coordinates
        coordinates = info[2].strip().split(",")
        x = coordinates[0].strip()
        y = coordinates[1].strip()
        #create Vertex based off info
        generic_vertex = Vertex(info[0],x,y)
        #add Vertex to list, name = key and reference = value
        vertices[info[0]] = generic_vertex
    in_file.close()
    
    #second time looping; fill in adjacent vertices
    in_file = open(filename, "r")
    for line in in_file:
        #strip away whitespace and then delimit semicolons
        clean_line = line.strip()
        info = clean_line.split(";")
        #for each line, find vertex reference using dictionary and then add references to adjacent vertices
        for adjacent_vertex in info[1].split(","):
            av = adjacent_vertex.strip()
            vertices[info[0]].list.append(vertices[av])
            vertices[info[0]].list_of_names.append(av)
    
    return vertices

    
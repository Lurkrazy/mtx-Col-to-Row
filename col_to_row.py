import glob
import os

path = "./input"

def read_mtx(filename):
    contents = filename.readlines()
    #edges = []
    #first = 0
    for i in range(len(contents)):
        words = contents[i].split()
        if words[0][0] != '%':
            print(words)
            #exit()
            #if first == 0:
            #    first = 1
            #else:
            #    if(len(words) == 3):
            #        edges.append((int(words[0]), int(words[1]), float(words[2])))
            #    else:
            #        edges.append((int(words[0]), int(words[1]), None))

    #g = Graph()
    #g.add_edges(edges)
    #return g



if __name__ == "__main__":

    for filename in glob.glob(os.path.join(path, '*.mtx')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            print(filename)
            #exit()
            read_mtx(f)
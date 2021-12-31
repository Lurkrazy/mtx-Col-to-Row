import glob
import os
import sys
path = "./"

class Edge():
    def __init__(self, row, col, weight):
        self.row = row
        self.col = col
        self.weight = weight

def write(out_file_path, line):
    f = open(out_file_path, 'a+')
    f.write(line+'\n')
    f.close()

def mkdir(path):
    
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("---  new folder...  ---")
        print("---  OK  ---")
    else:
        print("---  There is this folder!  ---")
		
#file = "G:\\xxoo\\test"
#mkdir(file)

def col_to_row(file, filename, output):
    contents = file.readlines()
    print(filename)
    index = filename.find('.mtx')
    out_file_path = filename[:index] + '_row' + filename[index:]
    print(out_file_path)
    # out_file_path = tmp_file_path
    out_file_path = out_file_path.replace("input", output)
    #exit()

    write(out_file_path, contents[0].strip('\n'))
    #exit()
    #print(contents[0])
    #exit()
    #edges = []
    #first = 0
    ite = 0
    for i in range(len(contents)):
        words = contents[i].split()
        if words[0][0] != '%' and ite == 0:
            #print(words)
            #exit()
            #print(words[2][0])
            #exit()
            M = int(words[0])#str
            N = int(words[1])#str
            L = int(words[2])#str
            L = L - 2
            write(out_file_path, str(M) + " " + str(N) + " " + str(L))
            ite += 1
            rows = [[] for i in range(M+1)]

            #print(M, N, L)
            continue

        #print(words)
        if words[0][0] != '%':
            #print(words)
            #print(int(words[0]))
            #exit()

            rows[int(words[0])].append(Edge(int(words[0]), int(words[1]), str(words[2])))
            #print(rows[int(ite)+1][0].weight)
            #exit()
            #rows[0].append(Edge( 2, 3, 4))
            #print(rows[int(words[0])][0].row, rows[int(words[0])][0].col, rows[int(words[0])][0].weight)
            #print(rows[2][0].row, rows[2][0].col, rows[2][0].weight)
            #exit()
            #print(rows[1][0].row, rows[1][0].col, rows[1][0].weight)
            #print(rows[0][1].row, rows[0][1].col, rows[0][1].weight)
            #print(rows[0][0].weight)
            #exit()
            ite += 1
            #if first == 0:
            #    first = 1
            #else:
            #    if(len(words) == 3):
            #        edges.append((int(words[0]), int(words[1]), float(words[2])))
            #    else:
            #        edges.append((int(words[0]), int(words[1]), None))
    #print(rows[2][0].row, rows[2][0].col, rows[2][0].weight)
    for i in range(1, M+1):
        for j in range(len(rows[i])):
            if rows[i][j]:
                write(out_file_path, str(rows[i][j].row) + " " + str(rows[i][j].col) + " " + str(rows[i][j].weight))

def removeDup(f, filename):
    writeDir = "./" + filename.replace(".mtx", "_final.mtx")
    outfile=open(writeDir,"w")
    
    lines_seen = set()  # Build an unordered collection of unique elements.
    
    for line in f:
        line = line.strip('\n')
        if line not in lines_seen:
            outfile.write(line+ '\n')
            lines_seen.add(line)

if __name__ == "__main__":
    output="../mtx_data"
    #output="./output"
    mkdir(output)

    #print(sys.argv[1])
    os.system('bash symmetric_handle.sh '+ sys.argv[1])

    #exit()
    #for filename in glob.glob(os.path.join(path, '*.mtx')):
    for filename in glob.glob(os.path.join(path, sys.argv[1].replace(".mtx", "_symm.mtx"))):
        print("dealing with " + sys.argv[1].replace(".mtx", "_symm.mtx"))
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            col_to_row(f, filename, output)

    #remove redundant lines    
    for filename in glob.glob(os.path.join(output, '*')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            #col_to_row(f, filename, output)
            removeDup(f, filename)
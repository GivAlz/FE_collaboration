import numpy as np

def read_msh(filename):

    x = np.array([])
    y = np.array([])

    nodes = np.array([])

    b_nodes = np.array([])

    topo = np.array([])

    num_line = 0

    f = open(filename,"r")

    for line in f:
        if line[0] == "$":
            print "This is useless"
        else:
            l = map(float,line.split())
            #print map(float,line.split())
            if len(l) == 4:
                x = np.append(x,l[1])
                y = np.append(y,l[2])
                nodes = np.append(nodes,l[0])

            if len(l) == 8:
                num_line += 1
                topo = np.append(topo,l[5:8])

            if len(l) == 7:
                b_nodes = np.append(b_nodes,l[5:])


    b_nodes_unique = np.array([])
    for elem in b_nodes:
        elem = elem - 1
        if elem not in b_nodes_unique:
            b_nodes_unique = np.append(b_nodes_unique,elem)

    b_nodes = b_nodes_unique


    topo = np.reshape(topo,(num_line,3))
    topo = topo - 1
    f.close()


    r_id = 0
    for row in topo:
        ck =      (x[row[1]]-x[row[0]])*(y[row[2]]-y[row[0]])
        ck = ck - (x[row[2]]-x[row[0]])*(y[row[1]]-y[row[0]])
        if ck < 0:
            topo[r_id,:] = np.array([[row[0],row[2],row[1]]])
        r_id+=1

    #print r_id

    topo = topo.astype(int)
    b_nodes = b_nodes.astype(int)

    return topo , x , y , nodes , b_nodes

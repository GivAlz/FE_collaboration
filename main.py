import numpy as np

from mesh import *
from basis_func import *
from assemble import *

from viewer import *

def clear_rows(A,b_nodes):

    for i in b_nodes:
        A[i,np.arange(A.shape[0])!=i]=np.zeros(A.shape[0]-1)

    return A


if __name__ == "__main__":
    topo, x, y, nodes, b_nodes = read_mesh(mesh/square.msh)

    A = gradu_gradv(topo,x,y)

    F = f_v(topo,x,y)

    F[b_nodes] = np.zeros(b_nodes.shape[0])

    A = clear_rows(A,b_nodes)

    sol = np.linalg.solve(A,F)

    plot_sol_p1(x,y,sol,topo)
    

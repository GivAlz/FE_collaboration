from basis_func import *
import numpy as np

def gradu_gradv(topo,x,y):
    A = np.zeros((x.shape[0],x.shape[0]))
    for elem in topo:
        x_l = x[elem]
        y_l = y[elem]
        (dx_phi,dy_phi,phi,surf_e) = tri_p1(x_l,y_l,np.zeros((1,2)))

        local_x = np.einsum('i,j->ij',dx_phi,dx_phi)
        local_y = np.einsum('i,j->ij',dy_phi,dy_phi)

        local_matrix = surf_e*(local_x + local_y)

        col,row = np.meshgrid(elem,elem)
        A[np.ndarray.flatten(row),np.ndarray.flatten(col)] += local_matrix.reshape(-1)

    return A

def f_v(topo,x,y):
    """ F assembly code """
    return F

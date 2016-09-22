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
        A[np.ndarray.flatten[row],np.ndarray[col]] += local_matrix

    return A

def f_v(topo,x,y):
    """ F assembly code """
    
    #Code to assemble the matrix for area computations
    Length = x.shape[0]
    AreaMatrix = np.ones((Length,3))
    AreaMatrix[:,:2] = np.array((x,y)).T
    
    #Assemblying F with f CONSTANT 1
    
    F = np.zeros(Length)
    
    for j in range(Length/3):
        k = j*3
        print AreaMatrix[j:k,:].shape
        K3 = abs(np.linalg.det(AreaMatrix[k:(k+3),:]))/6.0 #Area divided by 3
        F[topo[j]] += K3
        
    return F

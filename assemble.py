from basis_func import *
import numpy as np

def gradu_gradv(topo,x,y):
    """ A assembly code """
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

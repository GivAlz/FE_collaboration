import numpy as np

def tri_p1(x,y,eval_p):
    """
    Linear shape function on triangles, namely p1.

    Input:

    x : one dimensional array of triangle vertices x coords.\n
    y : one dimensional array of triangle vertices y coords.\n
    eval_p: (n,2) array of the n evaluation points. first
            column indicates x-coord, second y-coord.\n

    The basis functions are of the type:
    
                f(x,y) = ax+by+c
    
    where a is the x-derivative and y is the y-derivative.
    The coefficients are obtained solved a linear system:
                
                f(x,y) = A.dot(dx,dy,c) = (1,0,0) [or similar]
    
    Output:

    dx_phi : the three x-derivatives.\n
    dy_phi : the three y-derivatives.\n
    phi    : (n,3) array of the three shape funtions at the n eval points.\n
    surf_e : the triangle area.\n

    Notice: all the quantities are computed on the current element

    """
    
    #Building matrix A=(x,y,1)
    EvalMatrix = np.ones((3,3))
    EvalMatrix[:,:2] = np.array((x,y)).T
    
    dx_phi = np.zeros(3)
    dy_phi = np.zeros(3)
    c = np.zeros(3)
    I = np.eye(3)
    
    #Solving Ax=b with b = (1,0,0), (0,1,0), (0,0,1)
    for i in range(3):
        dx_phi[i],dy_phi[i],c[i] = np.linalg.solve(EvalMatrix,I[:,i])
        
    #Evaluating the phi functions
    CoeffMatrix = np.array((dx_phi,dy_phi))
    
    if eval_p.shape == (2,):
        Length = 1
        eval_p = eval_p.reshape((1,2))
        print("\nWARNING: THE SHAPE OF eval_p SHOULD BE (n,2)!!!\n")
    else:
        Length = eval_p.shape[0]
    
    phi = np.einsum('ji,ij->i',CoeffMatrix,eval_p)+c

    #Computes the area using cross product
    surf_e = abs(np.linalg.det(EvalMatrix))/2.0
    
    return dx_phi,dy_phi,phi,surf_e

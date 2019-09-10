# This function calculates the difference between two meshes.
# The difference is calculated by subtracting the the value of the coarser mesh
# from the sum of the values of the finer mesh covered by each element of the coarser
# mesh.
import numpy as np

def mesh_difference(mesh_c,mesh_f):
    shape_c=mesh_c.shape
    shape_f=mesh_f.shape
    
    for i in range(mesh_f[1]+1):
        
    return 

mesh_difference(np.zeros((4,2)),np.ones((8,4)))
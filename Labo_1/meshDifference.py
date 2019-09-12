# This function calculates the difference between two meshes.
# The difference is calculated by subtracting the the value of the coarser mesh
# from the sum of the values of the finer mesh covered by each element of the coarser
# mesh.
import numpy as np

def mesh_difference(coarseMesh, fineMesh):
    errorMatrix = np.zeros(coarseMesh.shape)
    numRows = errorMatrix.shape[0]
    numCols = errorMatrix.shape[1]
    for row in range(numRows):
        for col in range(numCols):
            errorMatrix[row,col] = fineMesh[]

# This function calculates the difference between two meshes.
# The difference is calculated by subtracting the the value of the coarser mesh
# from the sum of the values of the finer mesh covered by each element of the coarser
# mesh.
import numpy as np

def meshDifference(coarseMesh, fineMesh):
    errorMatrix = np.zeros(coarseMesh.shape)
    numRows = errorMatrix.shape[0]
    numCols = errorMatrix.shape[1]
    for row in range(numRows):
        for col in range(numCols):
            fineMeshRows = (2 * row, 2 * row + 1)
            fineMeshCols = (2 * col, 2 * col + 1)
            fineMeshSum = 0
            for fineMeshRow in fineMeshRows:
                for fineMeshCol in fineMeshCols:
                    fineMeshSum += fineMesh[fineMeshRow, fineMeshCol]

            errorMatrix[row, col] = fineMeshSum - coarseMesh[row, col]

    errorMatrixSum = np.sum(errorMatrix)

    return errorMatrixSum

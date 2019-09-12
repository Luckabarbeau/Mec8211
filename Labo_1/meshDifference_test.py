from meshDifference import meshDifference
import numpy as np


a = np.array([[4, 5],
              [6, 7]])
b = np.array([2])
expectedOutput = 14

functionOutput = meshDifference(b, a)

if functionOutput == expectedOutput:
    print('Test passed.')

else:
    print('Test failed. Error between coarse and fine mesh was not calculated properly.')

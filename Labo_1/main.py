# Read all files and add data to appropriate arrays
from read_file import read_file
from meshDifference import meshDifference
from plot_error import  plot_error
import numpy as np

mesh4_2 = read_file("p242_T_directe_4x2.txt")
mesh8_4 = read_file("p242_T_directe_8x4.txt")
mesh16_8 = read_file("p242_T_directe_16x8.txt")
mesh32_16 = read_file("p242_T_directe_32x16.txt")
mesh64_32 = read_file("p242_T_directe_64x32.txt")
mesh128_64 = read_file("p242_T_directe_128x64.txt")

Error = np.zeros((5,1))
Error[0] = meshDifference(mesh4_2,mesh8_4)
Error[1] = meshDifference(mesh8_4,mesh16_8)
Error[2] = meshDifference(mesh16_8,mesh32_16)
Error[3] = meshDifference(mesh32_16,mesh64_32)
Error[4] = meshDifference(mesh64_32,mesh128_64)

nb_cells = np.array([4,8,16,32,64])
a,b = plot_error(Error,nb_cells)
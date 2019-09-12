import matplotlib
import numpy as np


def graph(error , nb_cell):
    log_e = np.log(error)
    log_nb = np.log(1/nb_cell)
    a , b = np.polyfit(log_nb , log_e , 1)

    matplotlib.pyplot.loglog(matplotlib)
    return a , b
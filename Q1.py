import math
import numpy as np
import matplotlib.pyplot as plt
import scipy
#from plot_ksdensity import ksdensity

N = 1000
num_bins = 30

def plot_data(N, num_bins):
    # plot gaussian data and uniform data with length N
    # in a histogram with bins number of num_bins
    gaussian_data = np.random.normal(0, 1, N)
    unif_data = np.random.uniform(1, 0, N)
    #print(Gaussian_data)

    plt.subplot(1,2,1)
    plt.hist(gaussian_data, bins = num_bins)



    plt.subplot(1,2,2)
    plt.show()



plot_data(N, num_bins)
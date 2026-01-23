import numpy as np
import matplotlib.pyplot as plt


#true for square wave case and false for triangular wave
#case = False
case = True
#measured on the spectrum
sq_measure = [1.279, -8.082, -12.44, -15.7, -17.6, -19.78, -22.23, -25.5, -30.12, -35.02]
tri_measure = [-2.37,-21.53,-30.51,-36.49,-40.57,-44.38,-49.01,-53.36]
#transfer number to decibel
def num_to_dec(n):
    return 20*np.log10(n)
def sq_theory():
    sq_coefficients = []
    n = 1
    while len(sq_coefficients) < 10:
        coe = num_to_dec(4/(n*np.pi))
        sq_coefficients.append(coe)
        n += 2
    return sq_coefficients
def tri_theory():
    tri_coefficients = []
    n = 1
    while len(tri_coefficients) < 8:
        coe = num_to_dec(abs((8*(-1)^int((n-1)/2))/(np.pi*n)**2))
        tri_coefficients.append(coe)
        n += 2
    return tri_coefficients




plt.figure()
if case:
    x = [1,2,3,4,5,6,7,8,9,10]
    plt.scatter(x,sq_theory(),label="theory",color='b',marker='o')
    plt.scatter(x,sq_measure,label='measured',color='r',marker='x')
    plt.title(r"Theoretical v.s. measured $b_n$ for square wave")
else:
    x = [1,2,3,4,5,6,7,8]
    plt.scatter(x,tri_theory(),label="theory",color='b',marker='o')
    plt.scatter(x,tri_measure,label='measured',color='r',marker='x')
    plt.title(r"Theoretical v.s. measured $b_n$ for triangular wave")
plt.xlabel("n")
plt.ylabel("dBu")
plt.legend()
plt.grid(True)
plt.show()


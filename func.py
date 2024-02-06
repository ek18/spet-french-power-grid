import matplotlib.pyplot as plt

def f(X):
    L = []
    for k in range(X[1]):
        if k%1000000 ==0:
            print(X[0],k)
        L+=[X[0]**k]
    return L
# print(min([1,2])),

# plt.errorbar([1,2,3,4,5],[10,20,30,40,50],yerr= 2 ,label = 'A',alpha = 0.6)
# plt.errorbar([1,2,3,4,5],[1,20,3,40,5],yerr= [[0,2,1,7,2],[2,0,1,2,7]],label = 'B' ,alpha = 0.6)
# plt.legend()
# plt.show()
import numpy as np

print(np.logspace(-3,0,2))
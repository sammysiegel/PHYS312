import matplotlib.pyplot as plt
import numpy as np


def d2psi_dx2(x, psi, K):
    return (1*x**2 -K-.1*x**4) * psi

def get_psi(x_list, psi_list, d, K):
    for i in range(len(x_list) - 2):
        psi_list.append((d ** 2 * d2psi_dx2(x_list[i + 1], psi_list[i + 1], K)) - psi_list[i] + 2 * psi_list[i + 1])
    return psi_list[-1]

def K_search(K_start, K_stop, d, precision):
    x_list = np.arange(-4, 4, d)

    place = 0
    k=K_start

#searches for odd eigenstates
    while place < 15 and k <= K_stop and k>=K_start:
        psi_list = [0, 0.00001]
        psi = get_psi(x_list, psi_list, d, k)
        if psi > precision:
            k = k+1*10**(-1*place)
        elif psi < -1*precision:
            k = k-1*10**(-1*place)
            place += 1
        else:
            plt.scatter(x_list, psi_list)
            plt.show()
            return k

    place = 0
    k = K_start

# searches for even eigenstates
    while place < 15 and k <= K_stop and k>=K_start:
        psi_list = [0, 0.00001]
        psi = get_psi(x_list, psi_list, d, k)
        if -1*precision< psi < precision:
            plt.scatter(x_list, psi_list)
            plt.show()
            return k
        elif psi < precision:
            k = k + 1 * 10 ** (-1 * place)
        elif psi > -1*precision:
            k = k - 1 * 10 ** (-1 * place)
            place += 1


print(K_search(5, 7, .01, .0000001))
from matplotlib.pylab import *
import matplotlib.pylab as plt
import numpy as np


def courbe3(x):
    return (x  *  x - 2  *  x + 2) / 1000


def graphe():
    x = [i for i in np.arange(-10, 10, 0.5)]
    print(x)
    y = [i * i - 2 * i - 10 for i in x]  # x² -2 x -10
    z = [f(i) for i in x]  # ensemble en compréhension
    print(z)
    plt.plot(x, y)
    plt.show()

    plt.plot(z)
    plt.show()

    x = np.arange(-0.5, 0.5, 0.001)
    y = absolute(x * sin(1 / x))
    plt.plot(x, y, 'r')
    plt.show()


def randomGrapg():
    set = np.random.rand(20)

def exponentielle():
    debut = -1
    fin = 4
    pas = 0.1
    x = np.arange(debut,fin,pas)
    f = np.exp(x)
    plt.plot(x,f)
    lx = 'e = '+str(np.exp(1))
    plt.xlabel(lx)
    plt.ylabel('f(x) = exp(x)')
    plt.tile('Fct exponentielle')
    plt.show()

if _name_ == '__main__':
    graphe()
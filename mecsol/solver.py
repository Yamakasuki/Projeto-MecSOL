'''
import numpy
from truss1 import Result, init_truss,plot_diagram
from truss import Truss
import string
alphabet = list(string.ascii_uppercase)
xs=[]

def pontos(truss: Truss):
    listaids = truss.getMembersid(1)
    ab = truss.getID

    for i in range(len(ab)):
        a,b,c = truss.get_coordinates(ab[i])
        xs.append((a,b))
    my_truss = init_truss('trelica')
    my_truss.add_joints(xs)
    
    ys=[]
    for i in range(len(listaids[0])):
        if i % 2 == 0 and i != 0:
            ys.append(ab.index([i]))
'''
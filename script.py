import matplotlib.pyplot as grafica
import math
import numpy as np

#Datos del problema
R = 0.2
C = 1
dVc_dts = []
Vcs = []
#Datos del Método del Euler
x0 = 0
xf = 10
def h(n):
    return (xf-x0)/n

#Formulas del método de Euler
def Vc(t,n):
    global Vcs
    global dVc_dts

    Vct = Vcs[len(Vcs)-1] + (h(n)*(dVc_dts[len(dVc_dts)-1]))
    Vcs.append(round(Vct,2))
    dVc_dts.append(round(dVc_dt(t,Vcs[len(Vcs)-1]),2))
    return Vct

def ts(n):
    ts = []
    i = 0
    while i <= xf:
        ts.append(round(i,1))
        i += h(n)
    return np.array(ts)

#Formulas del problema
def V(t):
    return math.exp(-0.1*t)

def dVc_dt(t,Vc):
    return (V(t)-Vc)/(R*C)

def Vcts(n,Vc0):
    global dVc_dts
    global Vcs
    dVc_dts = [dVc_dt(x0,Vc0)]
    Vcs = [Vc0]
    i = 0
    tss = ts(n)
    #print("t -> " + str(tss))
    while i < len(tss)-1:
        Vc(tss[i],n)
        i += 1
    print("Vc(0)= " + str(Vc0) +" -> " + str(Vcs))
    return np.array(Vcs)

#Vc(0)=0
#grafica.plot(ts(10),Vcts(10,0))
#grafica.plot(ts(20),Vcts(20,0))
#grafica.plot(ts(30),Vcts(30,0))
#grafica.plot(ts(50),Vcts(50,0))
#grafica.plot(ts(100),Vcts(100,0))
#grafica.plot(ts(500),Vcts(500,0))
#grafica.plot(ts(1000),Vcts(1000,0))

#Vc(0)=2
""" grafica.plot(ts(10),Vcts(10,2))
grafica.plot(ts(20),Vcts(20,2))
grafica.plot(ts(30),Vcts(30,2)) """
grafica.plot(ts(50),Vcts(50,2))
grafica.plot(ts(100),Vcts(100,2))
grafica.plot(ts(500),Vcts(500,2))
grafica.plot(ts(1000),Vcts(1000,2)) 

#Vc(0)=-2
""" #grafica.plot(ts(10),Vcts(10,-2))
#grafica.plot(ts(20),Vcts(20,-2))
#grafica.plot(ts(30),Vcts(30,-2))
grafica.plot(ts(50),Vcts(50,-2))
grafica.plot(ts(100),Vcts(100,-2))
grafica.plot(ts(500),Vcts(500,-2))
grafica.plot(ts(1000),Vcts(1000,-2))  """
#Vc(0)=4
""" grafica.plot(ts(10),Vcts(10,4))
grafica.plot(ts(20),Vcts(20,4))
grafica.plot(ts(30),Vcts(30,4)) 
grafica.plot(ts(50),Vcts(50,4))
grafica.plot(ts(100),Vcts(100,4))
grafica.plot(ts(500),Vcts(500,4))
grafica.plot(ts(1000),Vcts(1000,4))  """




# Establecer el color de los ejes.
grafica.axhline(0, color="black")
grafica.axvline(0, color="black")
grafica.xlabel("t - Tiempo (s)")
grafica.ylabel("Vc - Voltage en el capacitor (V)")
grafica.show()
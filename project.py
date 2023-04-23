# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 19:43:05 2023

@author: nyank
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
fi_0=0.1 #концентрация твердого
fi_krit=0.27 #критичсекая концентрация
fi_under=1 #концентрация в нижней части
kpronic=1.1*10**5 #коэффициент проникаемости осадка
d_rho=2000 #разность плотностей
g=9.81 #гравитайция
mu=1.789*10**6 # вязкость
q=90 # Средняя скорость потока на выходе
fbk=0
diff=0
sigma0 = 2
n=6.5
fi_arr=[]
z_arr=[]
while fi_0<fi_under:
    
    vr=d_rho*fi_0*(1-fi_0)*g/(mu*(kpronic))
   # def FBK(d_rho, fi,):
    if fi_0<fi_krit:
        fbk=-d_rho*(fi_0**2)*((1-fi_0)**2)*g/(mu*(kpronic))
        sigma_e=0
    else:
        fbk=-kpronic*d_rho*(fi_0**2)*g/mu
        sigma_e=sigma0*(((fi_0/fi_krit)**n)-1); 
   # return fbk
    
    #def DIFFUSION (fbk, sigma_e, d_rho, fi_0, g):
        if fi_0<fi_krit:
            diff=0
        else:
            diff=-fbk*sigma_e/(d_rho*fi_0*g)
            #return diff

    z=-fbk*sigma_e/(d_rho*fi_0*g*q*fi_under-fbk-q*fi_0)
    fi_arr.append(fi_0)
    z_arr.append(z)
    fi_0=fi_0+0.01

print( z_arr)
plt.plot(fi_arr,z_arr)
plt.show

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.special as special
t = np.linspace(0, 10, 101)
result = integrate.quad(lambda x: special.jv(2.5,x), 0, 19)
print(result)"""
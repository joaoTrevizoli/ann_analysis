#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy import stats
from scipy.interpolate import spline
import matplotlib.pyplot as plt
import numpy as np

x_tk = ["3 days average", "4 days average", "5 days average", "6 days average", "7 days average"]
y = [1, 2, 3, 4]
x = [1, 2, 3, 4, 5]

# -------------------------------- Estimativa ---------------------------------------------------#
y_tk = ["autumn", "spring", "summer", "winter"]

z = np.array([[86.2639777541, 91.7085907336, 92.6752320789,	95.3093500985, 97.608992404],
             [88.7806137049, 88.8802508711, 89.9631424714, 90.4234966701, 92.7750794607],
             [79.4089316549, 85.5515584599, 90.3337106968, 92.3013136073, 95.1794977926],
             [77.1505598149, 81.5162093743, 87.3006637892, 90.2343727288, 90.291782772]])

fig = plt.figure()
ax = fig.gca(projection='3d')

x_prev, y_prev = np.meshgrid(x, y)


surf = ax.plot_surface(x_prev, y_prev, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
ax.set_zlim3d(50, 100)
ax.set_xlim3d(1, 5)
ax.set_ylim3d(1, 4)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))


ax.set_xticks([i for i in range(1, 6)])
ax.set_yticks([i for i in range(1, 7)])
ax.set_xticklabels(x_tk)
ax.set_yticklabels(y_tk)


fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

# -------------------------------- Fim Estimativa ---------------------------------------------------#
# -------------------------------- Previsao ---------------------------------------------------#

y_tk = ["winter", "summer", "spring", "autumn"]


z = np.array([[87.1393915552, 78.027100271, 77.3696257233, 76.6421890025, 73.6246612466],
              [64.3232675184, 66.1467286101, 73.3550135501,	75.3904132791, 79.8416327913],
              [58.4432978945, 63.5612466125, 60.1390243903, 64.9502382955, 65.7023486902],
              [63.7171081388, 56.3130518402, 53.193898068, 53.1401346271, 56.5023712737]])

fig = plt.figure()
plt.title("Forecasting")
ax = fig.gca(projection='3d')

x_prev2, y_prev2 = np.meshgrid(x, y)

surf = ax.plot_surface(x_prev2, y_prev2, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
ax.set_zlim3d(50, 100)
ax.set_xlim3d(1, 5)
ax.set_ylim3d(1, 4)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.set_xticks([i for i in range(1, 6)])
ax.set_yticks([i for i in range(1, 7)])
ax.set_xticklabels(x_tk)
ax.set_yticklabels(y_tk)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
# -------------------------------- Fim Previsão ---------------------------------------------------#


# -------------------------------- Macroclimática -------------------------------------------------#
distancia_mar = np.array([0, 31.4, 183, 363, 435, 480, 500, 670, 830, 1500])

media_primavera = np.array([53.248138324, 97.2222222222,
                            60.9756097561, 56.5853658536,
                            59.4444444444, 58.5365853658,
                            59.0243902439, 55.0000000000,
                            58.8888888889, 66.6666666667])

z_primavera = np.polyfit(distancia_mar, media_primavera, 2)
primavera_liner_reg = stats.linregress(distancia_mar, media_primavera)
p_primavera = np.poly1d(z_primavera)
print pow(primavera_liner_reg.rvalue, 2), z_primavera

media_verao = np.array([60.2380952381, 53.6585365854,
                        66.8292682927, 73.6585365853,
                        75.6944444444, 75.6097560976,
                        78.5365853658, 65.5555555556,
                        82.7777777778, 85.5555555556])

z_verao = np.polyfit(distancia_mar, media_verao, 2)
verao_liner_reg = stats.linregress(distancia_mar, media_verao)
p_verao = np.poly1d(z_verao)
print pow(verao_liner_reg.rvalue, 2), z_verao

media_outono = np.array([61.4919354839, 65.0000000000,
                         60.0000000000, 57.0731707317,
                         47.2222222222, 54.6341463415,
                         49.7560975610, 60.0000000000,
                         60.0000000000, 50.5555555556])

z_outono = np.polyfit(distancia_mar, media_outono, 2)
outono_liner_reg = stats.linregress(distancia_mar, media_outono)
p_outono = np.poly1d(z_outono)
print pow(outono_liner_reg.rvalue, 2), z_outono

media_inverno = np.array([97.3978494624, 75.1219512195,
                          70.7317073171, 78.5365853658,
                          80.6606606607, 65.3658536585,
                          83.9024390244, 82.7777777778,
                          85.0000000000, 66.1111111111])

z_inverno = np.polyfit(distancia_mar, media_inverno, 2)
inverno_liner_reg = stats.linregress(distancia_mar, media_inverno)
p_inverno = np.poly1d(z_inverno)
print pow(inverno_liner_reg.rvalue, 2), z_inverno


#suavizando curva do grafico no eixo x para todos os valores
dist_mar_smooth = np.linspace(distancia_mar.min(), distancia_mar.max(), 300)
#fim

plt.subplot(221)
#suavisando no eixo y
smooth_primavera = spline(distancia_mar, p_primavera(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_primavera, 'ks', dist_mar_smooth, smooth_primavera, 'r-', lw=1)
plt.axis([0, 1600, 45, 100])
plt.setp(plt.gca(), yticks=(50, 75, 100), xticks=(0, 183, 363, 500, 670, 830, 1500))
plt.text(50, 90, 'Spring', fontsize=15)

plt.subplot(222)
#suavisando no eixo y
smooth_verao = spline(distancia_mar, p_verao(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_verao, 'ks', dist_mar_smooth, smooth_verao, 'r-', lw=1)
plt.axis([0, 1600, 45, 100])
plt.setp(plt.gca(), yticks=(50, 75, 100), xticks=(0, 183, 363, 500, 670, 830, 1500))
plt.text(50, 90, 'Summer', fontsize=15)

plt.subplot(223)
#suavisando no eixo y
smooth_outono = spline(distancia_mar, p_outono(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_outono, 'ks', dist_mar_smooth, smooth_outono, 'r-', lw=1)
plt.axis([0, 1600, 45, 100])
plt.setp(plt.gca(), yticks=(50, 75, 100), xticks=(0, 183, 363, 500, 670, 830, 1500))
plt.text(50, 90, 'Autumn', fontsize=15)

plt.subplot(224)
#suavisando no eixo y
smooth_inverno = spline(distancia_mar, p_inverno(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_inverno, 'ks', dist_mar_smooth, smooth_inverno, 'r-', lw=1)
plt.axis([0, 1600, 45, 100])
plt.setp(plt.gca(), yticks=(50, 75, 100), xticks=(0, 183, 363, 500, 670, 830, 1500))
plt.text(50, 90, 'Winter', fontsize=15)

plt.show()
# -------------------------------- Fim macroclimática ---------------------------------------------#

# -------------------------------- Mesoclimática --------------------------------------------------#

altitude = np.array([11.7, 64.5, 286.3, 369.2, 435.5, 547, 605, 616.4, 737, 774.6])

media_primavera = np.array([97.2222222222, 53.248138324,
                            66.6666666667, 55.000000000,
                            58.5365853658, 60.9756097561,
                            56.5853658536, 59.4444444444,
                            59.0243902439, 58.8888888889])

z_primavera = np.polyfit(altitude, media_primavera, 2)
primavera_liner_reg = stats.linregress(altitude, media_primavera)
p_primavera = np.poly1d(z_primavera)
print pow(primavera_liner_reg.rvalue, 2), z_primavera


media_verao = np.array([53.6585365854, 60.2380952381,
                        85.5555555556, 65.5555555556,
                        75.6097560976, 66.8292682927,
                        73.6585365853, 75.6944444444,
                        78.5365853658, 82.7777777778])

z_verao = np.polyfit(altitude, media_verao, 2)
verao_liner_reg = stats.linregress(altitude, media_verao)
p_verao = np.poly1d(z_verao)
print pow(verao_liner_reg.rvalue, 2), z_verao

media_outono = np.array([65.0000000000, 61.4919354839,
                          50.5555555556, 60.0000000000,
                          54.6341463415, 60.0000000000,
                          57.0731707317, 47.2222222222,
                          49.756097561, 60.0000000000])

z_outono = np.polyfit(altitude, media_outono, 2)
verao_liner_reg = stats.linregress(altitude, media_outono)
p_outono= np.poly1d(z_outono)
print pow(verao_liner_reg.rvalue, 2), z_outono

media_inverno = np.array([75.1219512195, 97.3978494624,
                          85.0000000000, 66.1111111111,
                          65.3658536585, 70.7317073171,
                          78.5365853658, 80.6606606607,
                          83.9024390244, 82.7777777778])

z_inverno = np.polyfit(altitude, media_inverno, 2)
verao_liner_reg = stats.linregress(altitude, media_inverno)
p_inverno= np.poly1d(z_inverno)
print pow(verao_liner_reg.rvalue, 2), z_inverno

#suavizando curva do grafico no eixo x para todos os valores
altitude_mar_smooth = np.linspace(altitude.min(), altitude.max(), 300)
#fim

plt.subplot(221)
#suavisando no eixo y
smooth_primavera = spline(altitude, p_primavera(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_primavera, 'ks', altitude_mar_smooth, smooth_primavera, 'r-', lw=1)
plt.axis([0, 800, 45, 100])
plt.setp(plt.gca(), yticks=(50, 75, 100), xticks=(0, 100, 200, 300, 400, 500, 600, 700, 800))
plt.text(50, 90, 'Spring', fontsize=15)

plt.subplot(222)
#suavisando no eixo y
smooth_verao = spline(altitude, p_verao(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_verao, 'ks', altitude_mar_smooth, smooth_verao, 'r-', lw=1)
plt.axis([0, 800, 45, 100])
plt.setp(plt.gca(), yticks=(50, 75, 100), xticks=(0, 100, 200, 300, 400, 500, 600, 700, 800))
plt.text(50, 90, 'Summer', fontsize=15)

plt.subplot(223)
#suavisando no eixo y
smooth_outono = spline(altitude, p_outono(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_outono, 'ks', altitude_mar_smooth, smooth_outono, 'r-', lw=1)
plt.axis([0, 800, 45, 100])
plt.setp(plt.gca(), yticks=(50, 75, 100), xticks=(0, 100, 200, 300, 400, 500, 600, 700, 800))
plt.text(50, 90, 'Autumn', fontsize=15)

plt.subplot(224)
#suavisando no eixo y
smooth_inverno = spline(altitude, p_inverno(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_inverno, 'ks', altitude_mar_smooth, smooth_inverno, 'r-', lw=1)
plt.axis([0, 800, 45, 100])
plt.setp(plt.gca(), yticks=(50, 75, 100), xticks=(0, 100, 200, 300, 400, 500, 600, 700, 800))
plt.text(50, 90, 'Winter', fontsize=15)

plt.show()

# -------------------------------- Fim Mesoclimática ----------------------------------------------#

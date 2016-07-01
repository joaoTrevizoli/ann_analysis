#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from scipy import stats, interpolate
from scipy.interpolate import spline
import matplotlib.pyplot as plt
import numpy as np
from coleta_dados_bdclima import campo_mourao, jaguaruana
from change_z_position import MyAxes3D
from time import sleep

x_tk = ["3d", "4d", "5d", "6d", "7d"]
y = [1, 2, 3, 4]
x = [1, 2, 3, 4, 5]
x_n, y_n = np.mgrid[1:5:125j, 1:4:100j]
x_prev, y_prev = np.meshgrid(x, y)

# -------------------------------- Estimativa ---------------------------------------------------#
y_tk = ["Autumn", "Spring", "Summer", "Winter"]

z = np.array([[86.2639777541, 91.7085907336, 92.6752320789,	95.3093500985, 97.608992404],
             [88.7806137049, 88.8802508711, 89.9631424714, 90.4234966701, 92.7750794607],
             [79.4089316549, 85.5515584599, 90.3337106968, 92.3013136073, 95.1794977926],
             [77.1505598149, 81.5162093743, 87.3006637892, 90.2343727288, 90.291782772]])

fig = plt.figure()
ax = fig.gca(projection='3d')

tck = interpolate.bisplrep(x_prev, y_prev, z, s=0)
z_new = interpolate.bisplev(x_n[:,0], y_n[0,:], tck)


surf = ax.plot_surface(x_n, y_n, z_new, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
ax.set_zlim3d(50, 100)
ax.set_xlim3d(1, 5)
ax.set_ylim3d(1, 4)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))


ax.set_xticks([i for i in range(1, 6)])
ax.set_yticks([i for i in range(1, 7)])
ax.set_zticks([i for i in range(50, 105, 5)])
ax.set_xticklabels(x_tk)
ax.set_yticklabels(y_tk)

fig.colorbar(surf, shrink=0.6, aspect=5)

ax = fig.add_axes(MyAxes3D(ax, 'l'))

plt.tight_layout(pad=1.01)

plt.show()

# -------------------------------- Fim Estimativa ---------------------------------------------------#
# -------------------------------- Previsao ---------------------------------------------------#

y_tk = ["Winter", "Summer", "Spring", "Autumn"]


z = np.array([[87.1393915552, 78.027100271, 77.3696257233, 76.6421890025, 73.6246612466],
              [64.3232675184, 66.1467286101, 73.3550135501,	75.3904132791, 79.8416327913],
              [58.4432978945, 63.5612466125, 60.1390243903, 64.9502382955, 65.7023486902],
              [63.7171081388, 56.3130518402, 53.193898068, 53.1401346271, 56.5023712737]])

fig = plt.figure()
ax = fig.gca(projection='3d')

tck = interpolate.bisplrep(x_prev, y_prev, z, s=0)
z_new = interpolate.bisplev(x_n[:,0], y_n[0,:], tck)

surf = ax.plot_surface(x_n, y_n, z_new, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
ax.set_zlim3d(50, 100)
ax.set_xlim3d(1, 5)
ax.set_ylim3d(1, 4)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.set_xticks([i for i in range(1, 6)])
ax.set_yticks([i for i in range(1, 7)])
ax.set_zticks([i for i in range(50, 105, 5)])
ax.set_xticklabels(x_tk)
ax.set_yticklabels(y_tk)

fig.colorbar(surf, shrink=0.6, aspect=5)

ax = fig.add_axes(MyAxes3D(ax, 'l'))

plt.tight_layout(pad=1.01)

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
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 300, 600, 900, 1200, 1500))
plt.text(50, 90, 'A - Spring', fontsize=15)
plt.ylabel('%')
plt.xlabel('km')
plt.text(300, 80, r'$f(x) = 2.54e^{-5} x^2 - 0.0416x + 72.63$', fontsize=10)
plt.text(300, 75, r'$R^2 = 0.24$', fontsize=10)

plt.subplot(222)
#suavisando no eixo y
smooth_verao = spline(distancia_mar, p_verao(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_verao, 'ks', dist_mar_smooth, smooth_verao, 'r-', lw=1)
plt.axis([0, 1600, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 300, 600, 900, 1200, 1500))
plt.text(50, 90, 'B - Summer', fontsize=15)
plt.ylabel('%')
plt.xlabel('km')
plt.text(300, 55, r'$f(x) = -1.40e^{-5} x^2 + 0.0386x + 58.46$', fontsize=10)
plt.text(300, 50, r'$R^2 = 0.73$', fontsize=10)

plt.subplot(223)
#suavisando no eixo y
smooth_outono = spline(distancia_mar, p_outono(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_outono, 'ks', dist_mar_smooth, smooth_outono, 'r-', lw=1)
plt.axis([0, 1600, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 300, 600, 900, 1200, 1500))
plt.text(50, 90, 'C - Autumn', fontsize=15)
plt.ylabel('%')
plt.xlabel('km')
plt.text(300, 80, r'$f(x) = 6.00e^{-6} x^2 - 0.0152x + 61.62$', fontsize=10)
plt.text(300, 75, r'$R^2 = 0.30$', fontsize=10)

plt.subplot(224)
#suavisando no eixo y
smooth_inverno = spline(distancia_mar, p_inverno(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_inverno, 'ks', dist_mar_smooth, smooth_inverno, 'r-', lw=1)
plt.axis([0, 1600, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 300, 600, 900, 1200, 1500))
plt.text(50, 90, 'S - Winter', fontsize=15)
plt.ylabel('%')
plt.xlabel('km')
plt.text(300, 55, r'$f(x) = -3.70e^{-6} x^2 - 0.0032x + 81.71$', fontsize=10)
plt.text(300, 50, r'$R^2 = 0.16$', fontsize=10)

plt.tight_layout()
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
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 200, 400, 600, 800))
plt.text(50, 90, 'A - Spring', fontsize=15)
plt.ylabel('%')
plt.xlabel('m')
plt.text(150, 80, r'$f(x) = 8.17e^{-5} x^2 - 0.0883x + 80.59$', fontsize=10)
plt.text(150, 75, r'$R^2 = 0.40$', fontsize=10)

plt.subplot(222)
#suavisando no eixo y
smooth_verao = spline(altitude, p_verao(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_verao, 'ks', altitude_mar_smooth, smooth_verao, 'r-', lw=1)
plt.axis([0, 800, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 200, 400, 600, 800))
plt.text(50, 90, 'B - Summer', fontsize=15)
plt.ylabel('%')
plt.xlabel('m')
plt.text(150, 55, r'$f(x) = -3.37e^{-5} x^2 + 0.0528x + 57.09$', fontsize=10)
plt.text(150, 50, r'$R^2 = 0.52$', fontsize=10)

plt.subplot(223)
#suavisando no eixo y
smooth_outono = spline(altitude, p_outono(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_outono, 'ks', altitude_mar_smooth, smooth_outono, 'r-', lw=1)
plt.axis([0, 800, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 200, 400, 600, 800))
plt.text(50, 90, 'C - Autumn', fontsize=15)
plt.ylabel('%')
plt.xlabel('m')
plt.text(150, 80, r'$f(x) = 3.10e^{-5} x^2 - 0.0351x + 64.12$', fontsize=10)
plt.text(150, 75, r'$R^2 = 0.34$', fontsize=10)

plt.subplot(224)
#suavisando no eixo y
smooth_inverno = spline(altitude, p_inverno(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_inverno, 'ks', altitude_mar_smooth, smooth_inverno, 'r-', lw=1)
plt.axis([0, 800, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 100, 200, 300, 400, 500, 600, 700, 800))
plt.text(50, 90, 'D - Winter', fontsize=15)
plt.ylabel('%')
plt.xlabel('m')
plt.tight_layout()
plt.text(150, 55, r'$f(x) = 8.77e^{-5} x^2 - 0.0732x + 88.32$', fontsize=10)
plt.text(150, 50, r'$R^2 = 0.30$', fontsize=10)

plt.show()

# -------------------------------- Fim Mesoclimática ----------------------------------------------#
# -------------------------------- Normais Climatológicas -----------------------------------------#
# Legends
red_line = mlines.Line2D([], [], color='red', marker='o',
                         linewidth=2, label='Temperature')
red_patch = mpatches.Patch(facecolor='red', label='Deficit')
blue_patch = mpatches.Patch(facecolor='blue', label='Excess')
green_patch = mpatches.Patch(hatch='///', facecolor='green', label='Precipitation',)


x_months = ['Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug',
            'Sep', 'Oct', 'Nov', 'Dec']

# Campo mourao
campo_mourao['def'] = [-i if i != 0 else 0 for i in campo_mourao['def']]

fig = plt.figure()

ax = fig.gca()

ax.bar(range(1, 13), campo_mourao['precipitation'], align='center', color='green', hatch='///')

ax.plot(range(1, 13), campo_mourao['exc'], range(1, 13), campo_mourao['def'], color='black', label='water balance')
ax.fill_between(range(1, 13), 0, campo_mourao['exc'], facecolor='blue', zorder=5)
ax.fill_between(range(1, 13), 0, campo_mourao['def'], facecolor='red')

ax2 = ax.twinx()
ax2.plot(range(1, 13), campo_mourao['temperature'],
         linestyle='-', marker='o', linewidth=2,
         label="Temperature", color='red')
ax2.set_ylim(0, 35)

ax.set_ylabel('mm')
ax.set_xlim(1, 12)
ax.set_ylim(0, 275)

ax2.set_ylim(0, 40)
ax2.set_ylabel(u'⁰C')

plt.legend(handles=[red_patch, blue_patch, green_patch, red_line], loc='best', frameon=False)
plt.xticks(range(1, 13), x_months)

plt.show()

# Jaguaruana

jaguaruana['def'] = [-i if i != 0 else 0 for i in jaguaruana['def']]

fig = plt.figure()

ax = fig.gca()
ax.bar(range(1, 13), jaguaruana['precipitation'], align='center', color='green', hatch='///')

ax.plot(range(1, 13), jaguaruana['exc'], range(1, 13), jaguaruana['def'], color='black', label='water balance')
ax.fill_between(range(1, 13), 0, jaguaruana['exc'], facecolor='blue', zorder=5)
ax.fill_between(range(1, 13), 0, jaguaruana['def'], facecolor='red')


ax2 = ax.twinx()
ax2.plot(range(1, 13), jaguaruana['temperature'],
         linestyle='-', marker='o', linewidth=2,
         label="Temperature", color='red')

ax.set_ylabel('mm')
ax.set_xlim(1, 12)
ax.set_ylim(-175, 275)

ax2.set_ylim(0, 40)
ax2.set_ylabel(u'⁰C')


plt.legend(handles=[red_patch, blue_patch, green_patch, red_line], frameon=False)
plt.xticks(range(1, 13), x_months)

plt.show()
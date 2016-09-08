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
# from coleta_dados_bdclima import campo_mourao, jaguaruana
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
                       linewidth=0, antialiased=True, alpha=0.7)
ax.set_zlim3d(50, 100)
ax.set_xlim3d(1, 5)
ax.set_ylim3d(1, 4)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.contour(x_n, y_n, z_new, cmap='coolwarm', linewidths=2.5, alpha=1, origin='lower', extend='both')

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
z_new = interpolate.bisplev(x_n[:, 0], y_n[0,:], tck)

surf = ax.plot_surface(x_n, y_n, z_new, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, alpha=0.7)
ax.set_zlim3d(50, 100)
ax.set_xlim3d(1, 5)
ax.set_ylim3d(1, 4)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.contour(x_n, y_n, z_new, cmap='coolwarm', linewidths=2.5, alpha=1, origin='lower', extend='both')

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

# -------------------------------- Chuva -------------------------------------------------#
vol_primavera = np.array([22.00, 186.70,
                         447.00, 472.00,
                         494.10, 562.00,
                         603.60,   632.80,
                         649.20,  754.10])

media_primavera = np.array([97.22, 53.25,
                            56.59,  59.02,
                            58.89, 60.98,
                            66.67, 59.44,
                            58.54, 55.00])

z_primavera = np.polyfit(vol_primavera[1:], media_primavera[1:], 2)
primavera_liner_reg = stats.linregress(vol_primavera[1:], media_primavera[1:])
p_primavera = np.poly1d(z_primavera)
print(pow(primavera_liner_reg.rvalue, 2), z_primavera)

vol_verao = np.array([376.80, 384.20,
                      459.90, 481.40,
                      503.00, 540.00,
                      606.00, 674.70,
                      682.50, 707.00])

media_verao = np.array([60.24, 53.66,
                        82.78, 75.69,
                        73.66, 78.54,
                        66.83, 75.61,
                        65.56, 85.56])

z_verao = np.polyfit(vol_verao, media_verao, 2)
verao_liner_reg = stats.linregress(media_verao, media_verao)
p_verao = np.poly1d(z_verao)
print(pow(verao_liner_reg.rvalue, 2), z_verao)

vol_outono= np.array([144.00, 172.80,
                      174.80, 182.00,
                      192.00, 202.80,
                      276.40,  344.70,
                      351.60, 951.60])

media_outono = np.array([60.00, 54.63,
                         60.00, 49.76,
                         57.07, 50.56,
                         47.22, 60.00,
                         65.00, 61.49 ])

z_outono = np.polyfit(vol_outono, media_outono, 2)
outono_liner_reg = stats.linregress(vol_outono, media_outono)
p_outono = np.poly1d(z_outono)
print(pow(outono_liner_reg.rvalue, 2), z_outono)

vol_inverno = np.array([92.70, 97.10,
                        106.40, 109.00,
                        133.00, 146.00,
                        148.30, 221.90,
                        305.10, 652.50])

media_inverno = np.array([65.37, 66.11,
                          85.00, 70.73,
                          83.90, 78.54,
                          75.12, 80.66,
                          82.78, 97.40])

z_inverno = np.polyfit(vol_inverno, media_inverno, 2)
inverno_liner_reg = stats.linregress(vol_inverno, media_inverno)
p_inverno = np.poly1d(z_inverno)
print(pow(inverno_liner_reg.rvalue, 2), z_inverno)


#suavizando curva do grafico no eixo x para todos os valores
vol_primavera_smooth = np.linspace(vol_primavera[1:].min(), vol_primavera[1:].max(), 300)
vol_verao_smooth = np.linspace(vol_verao.min(), vol_verao.max(), 300)
vol_outono_smooth= np.linspace(vol_outono.min(), vol_outono.max(), 300)
vol_inverno_smooth = np.linspace(vol_inverno.min(), vol_inverno.max(), 300)
#fim



plt.subplot(221)

#suavisando no eixo y
smooth_primavera = spline(vol_primavera[1:], p_primavera(vol_primavera[1:]), vol_primavera_smooth)
print(smooth_primavera)
# fim
plt.plot(vol_primavera, media_primavera, 'ks', vol_primavera_smooth, smooth_primavera, 'r-', lw=1)
plt.axis([0, 1100, 45, 100])
plt.setp(plt.gca(),  yticks=range(50, 105, 5), xticks=(0, 200, 400, 600, 800, 1000), xticklabels=[])
plt.text(50, 90, 'A - Spring', fontsize=15)
plt.ylabel('Accuracy (%)')
plt.text(300, 75, r'$R^2 = 0.73$', fontsize=10)

plt.subplot(222)
#suavisando no eixo y
smooth_verao = spline(vol_verao, p_verao(vol_verao), vol_verao_smooth)
print(smooth_verao)
# fim
plt.plot(vol_verao, media_verao, 'ks', vol_verao_smooth, smooth_verao, 'r-', lw=1)
plt.axis([0, 1100, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), yticklabels=[], xticks=(0, 200, 400, 600, 800, 1000), xticklabels=[])
plt.text(50, 90, 'B - Summer', fontsize=15)
# plt.ylabel('%')
# plt.xlabel('mm')
plt.text(300, 50, r'$R^2 = 0.38$', fontsize=10)

plt.subplot(223)
#suavisando no eixo y
smooth_outono = spline(vol_outono, p_outono(vol_outono), vol_outono_smooth)
# fim
plt.plot(vol_outono, media_outono, 'ks', vol_outono_smooth, smooth_outono, 'r-', lw=1)
plt.axis([0, 1100, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 200, 400, 600, 800, 1000))
plt.text(50, 90, 'C - Autumn', fontsize=15)
plt.ylabel('Accuracy (%)')
plt.xlabel('Precipitation (mm)')
plt.text(300, 75, r'$R^2 = 0.15$', fontsize=10)

plt.subplot(224)
#suavisando no eixo y
smooth_inverno = spline(vol_inverno, p_inverno(vol_inverno), vol_inverno_smooth)
# fim
plt.plot(vol_inverno, media_inverno, 'ks', vol_inverno_smooth, smooth_inverno, 'r-', lw=1)
plt.axis([0, 1100, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5),  yticklabels=[], xticks=(0, 200, 400, 600, 800, 1000))
plt.text(50, 90, 'D - Winter', fontsize=15)
plt.xlabel('Precipitation (m)')
plt.text(300, 75, r'$R^2 = 0.62$', fontsize=10)

plt.tight_layout(pad=0.1, h_pad=0.1, w_pad=0.1)
plt.show()
# -------------------------------- Fim chuva ---------------------------------------------#


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
print(pow(primavera_liner_reg.rvalue, 2), z_primavera)

media_verao = np.array([60.2380952381, 53.6585365854,
                        66.8292682927, 73.6585365853,
                        75.6944444444, 75.6097560976,
                        78.5365853658, 65.5555555556,
                        82.7777777778, 85.5555555556])

z_verao = np.polyfit(distancia_mar, media_verao, 2)
verao_liner_reg = stats.linregress(distancia_mar, media_verao)
p_verao = np.poly1d(z_verao)
print(pow(verao_liner_reg.rvalue, 2), z_verao)

media_outono = np.array([61.4919354839, 65.0000000000,
                         60.0000000000, 57.0731707317,
                         47.2222222222, 54.6341463415,
                         49.7560975610, 60.0000000000,
                         60.0000000000, 50.5555555556])

z_outono = np.polyfit(distancia_mar, media_outono, 2)
outono_liner_reg = stats.linregress(distancia_mar, media_outono)
p_outono = np.poly1d(z_outono)
print(pow(outono_liner_reg.rvalue, 2), z_outono)

media_inverno = np.array([97.3978494624, 75.1219512195,
                          70.7317073171, 78.5365853658,
                          80.6606606607, 65.3658536585,
                          83.9024390244, 82.7777777778,
                          85.0000000000, 66.1111111111])

z_inverno = np.polyfit(distancia_mar, media_inverno, 2)
inverno_liner_reg = stats.linregress(distancia_mar, media_inverno)
p_inverno = np.poly1d(z_inverno)
print(pow(inverno_liner_reg.rvalue, 2), z_inverno)


#suavizando curva do grafico no eixo x para todos os valores
dist_mar_smooth = np.linspace(distancia_mar.min(), distancia_mar.max(), 300)
#fim


plt.subplot(221)

#suavisando no eixo y
smooth_primavera = spline(distancia_mar, p_primavera(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_primavera, 'ks', dist_mar_smooth, smooth_primavera, 'r-', lw=1)
plt.axis([0, 1700, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5),
         xticks=(0, 300, 600, 900, 1200, 1500), xticklabels=[])
plt.text(50, 90, 'A - Spring', fontsize=15)
plt.ylabel('Accuracy (%)')
# plt.text(300, 80, r'$f(x) = 2.54e^{-5} x^2 - 0.0416x + 72.63$', fontsize=10)
plt.text(300, 75, r'$R^2 = 0.24$', fontsize=10)

plt.subplot(222)
#suavisando no eixo y
smooth_verao = spline(distancia_mar, p_verao(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_verao, 'ks', dist_mar_smooth, smooth_verao, 'r-', lw=1)
plt.axis([0, 1700, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), yticklabels=[],
         xticks=(0, 300, 600, 900, 1200, 1500), xticklabels=[])
plt.text(50, 90, 'B - Summer', fontsize=15)

# plt.text(300, 55, r'$f(x) = -1.40e^{-5} x^2 + 0.0386x + 58.46$', fontsize=10)
plt.text(300, 50, r'$R^2 = 0.73$', fontsize=10)

plt.subplot(223)
#suavisando no eixo y
smooth_outono = spline(distancia_mar, p_outono(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_outono, 'ks', dist_mar_smooth, smooth_outono, 'r-', lw=1)
plt.axis([0, 1700, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 300, 600, 900, 1200, 1500))
plt.text(50, 90, 'C - Autumn', fontsize=15)
plt.ylabel('Accuracy (%)')
plt.xlabel('Distance from sea (km)')

# plt.text(300, 80, r'$f(x) = 6.00e^{-6} x^2 - 0.0152x + 61.62$', fontsize=10)
plt.text(300, 75, r'$R^2 = 0.30$', fontsize=10)

plt.subplot(224)
#suavisando no eixo y
smooth_inverno = spline(distancia_mar, p_inverno(distancia_mar), dist_mar_smooth)
# fim
plt.plot(distancia_mar, media_inverno, 'ks', dist_mar_smooth, smooth_inverno, 'r-', lw=1)
plt.axis([0, 1700, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), yticklabels=[], xticks=(0, 300, 600, 900, 1200, 1500))
plt.text(50, 90, 'S - Winter', fontsize=15)
plt.xlabel('Distance from sea (km)')
# plt.text(300, 55, r'$f(x) = -3.70e^{-6} x^2 - 0.0032x + 81.71$', fontsize=10)
plt.text(300, 50, r'$R^2 = 0.16$', fontsize=10)

plt.tight_layout(pad=0.1, h_pad=0.1, w_pad=0.1)
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
print(pow(primavera_liner_reg.rvalue, 2), z_primavera)


media_verao = np.array([53.6585365854, 60.2380952381,
                        85.5555555556, 65.5555555556,
                        75.6097560976, 66.8292682927,
                        73.6585365853, 75.6944444444,
                        78.5365853658, 82.7777777778])

z_verao = np.polyfit(altitude, media_verao, 2)
verao_liner_reg = stats.linregress(altitude, media_verao)
p_verao = np.poly1d(z_verao)
print(pow(verao_liner_reg.rvalue, 2), z_verao)

media_outono = np.array([65.0000000000, 61.4919354839,
                          50.5555555556, 60.0000000000,
                          54.6341463415, 60.0000000000,
                          57.0731707317, 47.2222222222,
                          49.756097561, 60.0000000000])

z_outono = np.polyfit(altitude, media_outono, 2)
verao_liner_reg = stats.linregress(altitude, media_outono)
p_outono= np.poly1d(z_outono)
print(pow(verao_liner_reg.rvalue, 2), z_outono)

media_inverno = np.array([75.1219512195, 97.3978494624,
                          85.0000000000, 66.1111111111,
                          65.3658536585, 70.7317073171,
                          78.5365853658, 80.6606606607,
                          83.9024390244, 82.7777777778])

z_inverno = np.polyfit(altitude, media_inverno, 2)
verao_liner_reg = stats.linregress(altitude, media_inverno)
p_inverno= np.poly1d(z_inverno)
print(pow(verao_liner_reg.rvalue, 2), z_inverno)

#suavizando curva do grafico no eixo x para todos os valores
altitude_mar_smooth = np.linspace(altitude.min(), altitude.max(), 300)
#fim

plt.subplot(221)

#suavisando no eixo y
smooth_primavera = spline(altitude, p_primavera(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_primavera, 'ks', altitude_mar_smooth, smooth_primavera, 'r-', lw=1)
plt.axis([0, 900, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 100, 200, 300, 400, 500, 600, 700, 800), xticklabels=[])
plt.text(50, 90, 'A - Spring', fontsize=15)
plt.ylabel('Accuracy (%)')
# plt.text(150, 80, r'$f(x) = 8.17e^{-5} x^2 - 0.0883x + 80.59$', fontsize=10)
plt.text(150, 75, r'$R^2 = 0.40$', fontsize=10)

plt.subplot(222)
#suavisando no eixo y
smooth_verao = spline(altitude, p_verao(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_verao, 'ks', altitude_mar_smooth, smooth_verao, 'r-', lw=1)
plt.axis([0, 900, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), yticklabels=[], xticks=(0, 100, 200, 300, 400, 500, 600, 700, 800), xticklabels=[])
plt.text(50, 90, 'B - Summer', fontsize=15)
# plt.ylabel('%')
# plt.xlabel('m')
# plt.text(150, 55, r'$f(x) = -3.37e^{-5} x^2 + 0.0528x + 57.09$', fontsize=10)
plt.text(150, 50, r'$R^2 = 0.52$', fontsize=10)

plt.subplot(223)
#suavisando no eixo y
smooth_outono = spline(altitude, p_outono(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_outono, 'ks', altitude_mar_smooth, smooth_outono, 'r-', lw=1)
plt.axis([0, 900, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), xticks=(0, 100, 200, 300, 400, 500, 600, 700, 800))
plt.text(50, 90, 'C - Autumn', fontsize=15)
plt.ylabel('Accuracy (%)')
plt.xlabel('Altitude (m)')
# plt.text(150, 80, r'$f(x) = 3.10e^{-5} x^2 - 0.0351x + 64.12$', fontsize=10)
plt.text(150, 75, r'$R^2 = 0.34$', fontsize=10)

plt.subplot(224)
#suavisando no eixo y
smooth_inverno = spline(altitude, p_inverno(altitude), altitude_mar_smooth)
# fim
plt.plot(altitude, media_inverno, 'ks', altitude_mar_smooth, smooth_inverno, 'r-', lw=1)
plt.axis([0, 900, 45, 100])
plt.setp(plt.gca(), yticks=range(50, 105, 5), yticklabels=[], xticks=(0, 100, 200, 300, 400, 500, 600, 700, 800))
plt.text(50, 90, 'D - Winter', fontsize=15)
# plt.ylabel('%')
plt.xlabel('Altitude (m)')
# plt.text(150, 55, r'$f(x) = 8.77e^{-5} x^2 - 0.0732x + 88.32$', fontsize=10)
plt.text(150, 50, r'$R^2 = 0.30$', fontsize=10)

plt.tight_layout(pad=0.1, h_pad=0.1, w_pad=0.1)
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

campo_mourao = {'temperature': [22.9, 22.7, 21.3, 19.1, 16.4, 15.4, 16.2, 16.9, 18.2, 18.6, 21.8, 22.4],
                'precipitation': [175.0, 165.0, 120.0, 97.0, 124.0, 123.0, 83.0, 84.0, 138.0, 162.0, 136.0, 196.0],
                'pet': [112.68, 100.53, 93.36, 67.98, 48.43, 39.37, 44.76, 50.43, 60.15, 69.02, 97.78, 110.67],
                'storage': [100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00],
                'ret': [112.7, 100.5, 93.4, 68.0, 48.4, 39.4, 44.8, 50.4, 60.2, 69.0, 97.8, 110.7],
                'def': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                'exc': [62.3, 64.5, 26.6, 29.0, 75.6, 83.6, 38.2, 33.6, 77.8, 93.0, 38.2, 85.3]
                }

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
ax.set_ylim(-175 , 275)

ax2.set_ylim(0, 40)
ax2.set_ylabel(u'⁰C')

plt.legend(handles=[red_patch, blue_patch, green_patch, red_line], loc='lower right', frameon=False)
plt.xticks(range(1, 13), x_months)

plt.show()

# Jaguaruana

jaguaruana = {'temperature': [27.9, 24.0, 26.9, 26.9, 25.2, 26.1, 26.0, 26.4, 27.3, 27.5, 28.1, 26.0],
              'precipitation': [30.0, 123.0, 231.0, 181.0, 115.0, 55.0, 46.0, 55.0, 48.0, 3.0, 1.0, 17.0],
              'pet': [166.21, 87.81, 147.69, 141.30, 113.15, 123.91, 126.03, 134.18, 148.69, 159.68, 169.33, 131.75,],
              'storage': [0.01, 35.21, 100.00, 100.00, 100.00, 50.20, 22.55, 10.22, 3.73, 0.78, 0.14, 0.05,],
              'ret': [30.0, 87.8, 147.7, 141.3, 113.1, 104.8, 73.7, 67.3, 54.5, 6.0, 1.6, 17.1],
              'def': [136.2, 0.0, 0.0, 0.0, 0.0, 19.1, 52.4, 66.8, 94.2, 153.7, 167.7, 114.6],
              'exc': [0.0, 0.0, 18.5, 39.7, 1.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
              }

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


# plt.legend(handles=[red_patch, blue_patch, green_patch, red_line], frameon=False)
plt.xticks(range(1, 13), x_months)

plt.show()
import numpy as np
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import os

# http://www.gadm.org/country Joao do futuro, lebrar desse site

basepath = os.path.abspath(os.path.dirname(__file__))
shapefile = ''.join([basepath, '/mapas/BRA_adm1'])

fig, ax = plt.subplots()

m = Basemap(projection='merc', llcrnrlat=-35, urcrnrlat=7,
            llcrnrlon=-77, urcrnrlon=-32, resolution='i')

m.ax = ax

m.fillcontinents()


shp = m.readshapefile(shapefile, 'states', drawbounds=True)
for nshape, seg in enumerate(m.states):
    poly = Polygon(seg, facecolor='0.75', edgecolor='k')
    ax.add_patch(poly)

lats = np.array([-21.2525, -4.8361, -22.725,
                 -24.04309, -14.4041, -22.305,
                 -9.6663, -22.1211, -17.7927,
                 -19.7474])
lons = np.array([-48.3257, -37.7815, -47.6476,
                 -52.37929, -56.4371, -53.8189,
                 -35.7351, -51.393, -50.9197,
                 -47.9392])

x, y = m(lons, lats)

m.scatter(x, y, s=50, marker='o', c='red', cmap=cm.cool, alpha=0.7, zorder=100.)

m.drawmapscale(-43., -32., -47.1, -28.1,  1000, fontsize=10, zorder=5, barstyle='fancy')


parallels = np.arange(-50.,10,5.)

print parallels

m.drawparallels(parallels, labels=[1, 0, 0, 1])

meridians = np.arange(70., 360., 5.)
print meridians
m.drawmeridians(meridians,labels=[1, 0, 0,1])

plt.show()
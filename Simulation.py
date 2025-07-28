import Evolution as evo
import Map as map
import Display as dsp

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


map.world = evo.World() #create instance of world

evo.create_creature(world = map.world, number=50) #create 50 creatures

map.create_base_map() #creates map size 51, 50 food tiles, 3 water sources


plt.style.use('_mpl-gallery-nogrid')
cmap = ListedColormap(["mediumseagreen","powderblue","firebrick","ivory"])

fig, ax = plt.subplots(figsize = (5,5))
fig.canvas.mpl_connect('button_press_event', dsp.onclick)

map.image = ax.imshow(map.Z_update(), origin='lower',cmap=cmap)

map.update_map(None)#runs a day without updadting display - good for error looking ;)

ani = FuncAnimation(fig, map.update_map, frames = 100, interval = 2000, blit = True) #for animation of graph
plt.show()

#dsp.end_stats()
# Evolution-Simulator
Small program designed to follow the change in 'creature' traits in response to stressers, to weakly mimick a form of 'evolution' displayed using matplotlib.

Creatures must eat and drink to maintain a level of energy and thirst. Creatures can develop/inherit preffered directions and distance of movement, strength, growth rates, energy given children upon birth, etc. This inheritance is subject to minor change on random due to 'random mutation'.

Movement and population of creatures are tracked/displayed using matplotlib, a creature's information (e.g. position, size, energy, etc.) can be accessed by clicking on a given creature:

<p align="center">
  <img src="https://github.com/EvaWXHenderson/Evolution-Simulator/blob/main/images/Screenshot%202025-07-28%20at%2014.26.14.png" width="200" />
  <img src="https://github.com/EvaWXHenderson/Evolution-Simulator/blob/main/images/Screenshot%202025-07-28%20at%2014.26.30.png" width="200" /> 
  <img src="https://github.com/EvaWXHenderson/Evolution-Simulator/blob/main/images/Screenshot%202025-07-28%20at%2014.27.05.png" width="200" /> 
</p>

## Files:
### Evolution.py:
Definition of classes: World and Creature
- World: contains functions for events
- Creature: contains variables defining creature traits and functions defining actions creatures may take

### Map.py:
Functions for generation and updating of maps containing: food sources (red), water sources (blue), and creatures (white).

### Display.py:
Contains counters, lists, and functions to hold information for the display of creature trait information during simulation.

### Simulation.py:
Used to run simulation program using Map.py, Evolution.py, and Display.py.

## Running and Customising a Simulation:
Prior to any initiation of the program, an instance of the world class should be used (example seen in Simulation.py).

**Number of starting organisms (creatures)** - to alter the number of creatures that 'spawn' at the beginning of the simulation use:
```
Evolution.create_creature(world = 'instance of world class', number='number of initial creatures')
```

**Number of starting food tiles** - to alter the number of food tiles are 'spawn' at the beginning of the simulation:
```
map.create_food_points(items = 'number of food tiles')
```
**Rate of decay of food tiles**  - to alter the number of days that food items remain on the grid/are accessible by creatures:
```
map.food.decay(item, decay_rate='number of days until decay')
```
_(note: decay rate is default set to 10, this can be found in the World.day() function in Evolution.py)_

**Number and size of water sources** - to alter the number and size of water sources that appear on the map use the map.create_water_points() function, creating an instance per water source desired:
```
map.create_water_points(water_source = 'list that contains all water coordinates', size = 'number of water tiles')
```
_(note: recommended sequence of tile assignment is to first create instances of creatures desired, water sources, then food tiles. This is done to ensure that food tiles do not spawn in water sources.)_    
_(note: using the create_base_map() function will produce 50 initial food tiles and 2 water sources; one of size 25, the other 200.)_    

**To run the simulation** - the following can be used:
```
plt.style.use('_mpl-gallery-nogrid')
cmap = ListedColormap(["mediumseagreen","powderblue","firebrick","ivory"])

fig, ax = plt.subplots(figsize = (5,5))
map.image = ax.imshow(map.Z_update(), origin='lower',cmap=cmap)

map.update_map(None)#runs a day without updadting display - good for error looking ;)

ani = FuncAnimation(fig, map.update_map, frames = 100, interval = 1000, blit = True) #for animation of graph
plt.show()
```
with "mediumseagreen" associated with the base map colour, "powderblue" with the water tiles, "firebrick" with the food tiles, and "ivory" with the creature tiles.

_(note: colours of base map (i.e. grass), water source tiles, food tiles, and creature tiles can be altered by altering the colours of cmap noted above)_
_(note: the time between each frame may be altered by the interval argument of ani (in ms))_

## Displaying Information
At the end of every 'day' (iteration), the following information appears in the terminal:
```
Day: 1
number of creatures: 51
babies born: 1
deaths: 0
food eaten: 1
```
By clicking creature tiles during the running of the program, the following information will be displayed in the terminal:
```
Position: (20, 45)
Horizontal bias: 1
Vertical bias: 3
Energy: -10
Thirst: 19
Strength: 38
Growth threshold: 11
Growth expenditure: 10
Birth threshold: 22
Birth expenditure: 13
```
The end_stats() function (optional) can be used after plt.show() in the/your simulation file if the information for all creatures that were present in the 'day' prior to termination of program.

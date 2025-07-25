# Evolution-Simulator
Small program designed to follow the change in 'creature' traits in response to stressers, to weakly mimick a form of 'evolution'.

Creatures must eat (from limited changing food sources) and drink (from water sources), creatures can develop preffered directions and distance of movement, fight, pass traits onto children.

Creatures most suited to their environment will be most likely to survive and grow in population.

### Evolution.py
Definition of classes: World and Creature
- World: contains functions for events
- Creature: contains variables defining creature traits and functions defining actions creatures may take

### Map.py
Functions for generation and updating of maps containing: food sources (red), water sources (blue), and creatures (brown).

Note: Water sources must be generated prior to the addition of food tiles to ensure that food tiles do not spawn in water sources.

### Simulation.py
Runs program using Map.py and Evolution.py.
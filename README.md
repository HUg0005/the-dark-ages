# The Dark Ages

## Game Mechanics:
* 1 tick is equal to 1 second.
* Units require food every 10 ticks except for rams. Knights consume 2 food every 10 ticks; all other units 1 food every 10 ticks.
* Idle villagers decrease working villagers of the same type efficiency.
* To win all built buildings (not including walls) must to be destroyed.
* Archers have a attack radius of 3.
* Villagers will yield 10 items every 10 ticks if next their specified resource.
* WARNING: YOU CANNOT CHANGE A VILLAGER'S JOB!
* Units will spawn under their buildings. Units cannot spawn if this site is blocked.
* The map refreshes every second.
* Limit of 5 villagers.
* All units enter and leave the map on the right hand side.
* To move units to the enemy's map, move the unit off the right hand side of the map.
* All enemy units except for villagers are red on the map.
* WARNING: If you change your map to view the enemies (map *enemy number*) then your units will be shown as the enemy.
* All error messages end with a !

## Game Commands:
* b coordinates building(archery, stable, workshop, barracks, wall)
    build; everything but wall can only can only be built once.

* c unit(farmer, lumberjack, miner, archer, militia, knight, ram)
    create; creates unit underneath their respective building.

* m unit_name direction distance
    move; moves unit specified distance. Speed depends on unit.

* map [start, stop, player number]
    map; controls map display. player number; change what map player the map is shown, start; start map refreshing, stop; stops map refreshing (WARNING: unit movement, unit creation and building creation after map refreshing stopped will not be shown!)

* f unit_name/building/coordinates
    focus; displays information in stats

## Server Commands:
* start
    starts game.
* save
    saves current game to text files.
* load
    load a previously saved game.

## Extra Information

### Unit Spawn Buildings:
* villagers = town_center
* militia = barracks
* archer = archery
* knights = stable
* ram = workshop

### Building Build Time:
* wall = 2 ticks
* barracks = 5 ticks
* archery = 5 ticks
* stable = 10 ticks
* workshop = 10 ticks

### Unit Health:
* town_center = 3000
* barracks = 1000
* archery = 1000
* stable = 2000
* workshop = 2500
* walls = 500

### Building Health

* villager = 100
* militia = 150
* archer = 125
* knight = 200
* ram = 100

### Unit Movement Speed:
* villager = 1 place per tick
* militia = 1 place per tick
* archer = 1 place per tick
* knight = 2 places per tick
* ram = 1 place per tick

### Unit Delt Damage:
* villager = 1
* militia = 50
* archer = 25
* knight = 100
* ram = 200 (only buildings)

### Required Resources for Buildings:
* barracks = 200 stone
* archery = 200 stone 100 wood
* stable = 300 stone 200 wood
* workshop = 400 stone 300 wood

### Required Resources for Units:
* villager = 100 food
* militia = 100 food 50 stone
* archer = 100 food 50 stone 50 wood
* knight = 200 food 50 wood
* ram = 100 wood 100 stone

### Map symbols:
* green @ = tree
* yellow ; = farm
* cyan ~ = water
* black o = stone

* yellow 0 = farmer villager
* green 0 = lumberjack villager
* black 0 = miner villager
* red unit = enemy unit

* ! = militia
* ) = archer
* ^ = knight
* = = ram

* X = town_center
* B = barracks
* A = archery
* S = stable
* W = workshop
* % = not built building


### Unit Resource Usage:
* knights = 2 food per 10 ticks
* all other units (except rams)= 1 food per 10 ticks

## Developer's Notes:
* unit_data(symbol, health, movement_speed, food_consumption, unit_type, unit_status, damage)

*Hayden Hughes*
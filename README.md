# Simple Math Game made in Python

I made a simple Math Game as a final project in my SENAI course.

## Brief Explanation
Here you can choose one of 3 players: 
Warrior, Archer, and Witch.  
With 3 difficulties: Easy, Medium, Hard.  

The battle is simple: You have to solve the math questions! Easy. But if you answer correctly too many times, you're gonna have problems!!!

Entity Class Documentation
==========================

Overview
--------

The `Entity` class represents a character or object in the game with attributes such as health, damage, and inventory.

Class Definition
----------------
```python
    class Entity:
        def __init__(self, emoji, health, damage) -> None:
```
### Parameters:

*   **emoji (str):** A string representing the character's emoji.
*   **health (int):** The initial health points of the entity.
*   **damage (int):** The amount of damage the entity can inflict.

Methods
-------

### `print_health()`

Displays the current health of the entity along with its emoji.

### `attack(enemy)`

Inflicts damage on the specified enemy entity.

#### Parameters:

*   **enemy (Entity):** The enemy entity that will receive the damage.

### `add_item(item)`

Adds an item to the entity's inventory.

#### Parameters:

*   **item (dict):** A dictionary representing the item to be added, containing at least `name` and `description` keys.

### `print_inventory()`

Displays the items currently in the entity's inventory.

Example Usage
-------------
```python
    # Create an entity instance
    player = Entity(emoji='🧙‍♂️', health=100, damage=20)
    
    # Print health
    player.print_health()
    
    # Create an enemy entity
    enemy = Entity(emoji='🐉', health=80, damage=15)
    
    # Player attacks enemy
    player.attack(enemy)
    
    # Print enemy health after attack
    enemy.print_health()
    
    # Add item to player's inventory
    player.add_item({'name': 'Health Potion', 'description': 'Restores 20 health.'})
    
    # Print inventory
    player.print_inventory()
```
Battle Class Documentation
==========================

Overview
--------

The `Battle` class manages the combat between a player and an enemy in a math-based game. It handles health tracking, player actions, and the mechanics of winning or losing the battle.

Class Definition
----------------
```python
    class Battle:
        def __init__(self, enemy, player) -> None:
```
### Parameters:

*   **enemy (Entity):** The enemy the player is battling.
*   **player (Entity):** The player character involved in the battle.

Methods
-------

### `print_healths()`

Displays the health of both the player and the enemy.

### `guess_number()`

Prompts the player to guess a random number.

#### Returns:

*   **bool:** True if the player's guess is correct, False otherwise.

### `guess_calculation()`

Prompts the player to solve a multiplication problem involving three random numbers.

#### Returns:

*   **bool:** True if the player's answer is correct, False otherwise.

### `result()`

Runs the battle loop, determining the outcome of the battle based on player and enemy actions.

#### Workflow:

1.  Displays current health of both entities.
2.  Allows the player to answer math questions and make guesses.
3.  Alternates turns between the player and the enemy until one is defeated.
4.  Resets player health after the battle.
5.  Displays the outcome of the battle.

#### Returns:

*   **bool:** True if the player wins, False if the player loses.

Example Usage
-------------
```python
    from entity import Entity
    
    # Create player and enemy instances
    player = Entity(max_health=100)
    enemy = Entity(max_health=50)
    
    # Initialize a battle
    battle = Battle(enemy, player)
    
    # Run the battle and get the result
    result = battle.result()
    if result:
        print("You've won the battle!")
    else:
        print("You have been defeated.")
    
```
Notes
-----

*   The class relies on external variables `singleton_guess` and `singleton_wins` from the `game` module to control the difficulty of guessing and the number of wins required to trigger specific actions.
*   The player's health resets to the maximum after the battle concludes.

Scene Class Documentation
=========================

Overview
--------

The `Scene` class represents a scene in an interactive story, allowing users to make choices that influence the narrative.

Features
--------

*   Create scenes with a title and description.
*   Add choices that trigger specific functions when selected.

Installation
------------

No installation is needed; just include the class definition in your Python project.

Usage
-----

### Class Definition

```python
    class Scene:
        def __init__(self, name, description, choices=None):
```

#### Parameters:

*   **name (str):** Title of the scene.
*   **description (str):** Description of the scene.
*   **choices (dict, optional):** A dictionary of choices (default is an empty dictionary).

#### Example:

```python
    scene1 = Scene("Forest", "You are in a dark forest.")
```
### Methods

#### `add_choice(choice, callback_function)`

Adds a choice to the scene.

##### Parameters:

*   **choice (str):** Label for the choice.
*   **callback\_function (function):** Function that runs when the choice is selected.

##### Example:
```python
    def go_north():
        print("You walk north.")
    
    scene1.add_choice("Go North", go_north)
```
Example Usage
-------------
```python
    # Define functions for choices
    def go_north():
        print("You walk north into the forest.")
    
    def go_south():
        print("You head south towards the river.")
    
    # Create a scene
    scene1 = Scene("Forest", "You are in a dark forest.")
    
    # Add choices
    scene1.add_choice("Go North", go_north)
    scene1.add_choice("Go South", go_south)
    
    # Display scene information
    print(scene1.name)
    print(scene1.description)
    for choice in scene1.choices:
        print(choice)
```


## Summary
The ```Scene``` class is a straightforward way to create interactive scenes in a story, allowing users to make choices that shape the narrative.

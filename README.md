# Simple Math Game made in Python

I made a simple Math Game as a final project in my SENAI course.

## Brief Explanation
Here you can choose one of 3 players: 
Warrior, Archer, and Witch.  
With 3 difficulties: Easy, Medium, Hard.  

The battle is simple: You have to solve the math questions! Easy. But if you answer correctly too many times, you're gonna have problems!!!

Scene Class
===========

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

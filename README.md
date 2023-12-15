# GameOfLife

## Features
- Start/Stop Simulation: Toggle the simulation to start or stop the evolution of cells.
- Draw Cells: Click on cells to toggle between alive and dead states while the simulation is paused.
- Save/Load State: Save and load the current state of the simulation.
- Adjust Simulation Speed: Control the speed of the simulation through a delay parameter.

## Code Organization

The code is organized into a class, GameOfLife, which encapsulates the game logic and UI functionalities. Here are key components of the class:

- Initialization: The class initializes Pygame and sets up the game environment, including screen dimensions, grid dimensions, colors, and initial game state.

 - Drawing Functions: Methods for drawing the grid, cells, and buttons on the screen.

- Game Logic: Methods for calculating the next generation of cells based on the rules of Conway's Game of Life.

- Save/Load State: Methods for saving the current game state to a file and loading a previously saved state.

- Simulation Control: Methods for starting and stopping the simulation, adjusting simulation speed, and handling user input.

- Main Loop (run Method): The main loop runs the simulation and continuously updates the screen based on user input and the game state.

## How to Run

- Make sure you have Python installed on your system.
- Install the required libraries by running pip install pygame numpy.
- Run the provided code in a Python environment.

## Controls
- Start/Stop Simulation: Click the "Start/Stop" button.
- Draw Cells: Click on cells when the simulation is paused.
- Save State: Click the "Save" button.
- Load State: Click the "Load" button.
- Quit: Close the window or press Ctrl+C in the terminal.

# Refactoring: 
### Encapsulation:

- The game logic and UI functionalities are encapsulated within a GameOfLife class, promoting a clearer separation of concerns.
### Modularity:

- The code is organized into methods within the GameOfLife class, making it modular and improving readability.
### Separation of Concerns:

- Each method within the class addresses a specific aspect of the program, promoting a separation of concerns. For example, methods handle drawing, game state manipulation, and file I/O.
### Readability:

- By using meaningful method names, grouping related functionality together, and removing redundancy, the code becomes more readable and easier to understand.
### Consistent Naming:

- Consistent naming conventions for variables, methods, and attributes contribute to code clarity.
### Single Responsibility Principle (SRP):

- Methods within the class have a single responsibility, adhering to the SRP from SOLID principles.
### Code Organization:

- The code is organized in a way that makes it easy to find and understand different parts of the program.

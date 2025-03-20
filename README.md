# Game of Life
#### A Python/Pygame implementation of Conway's Game of Life
CS50x Final Project
### How it works
Conway's Game of Life is a logical game created by John Horton Conway in 1970. This game is played in a grid full of square cells, each one having a current life state, dead or alive. The game logic simulates the life of these cells in each generation based on 4 rules:
* Any live cell with fewer than two live neighbors dies (due to underpopulation)
* Any live cell with two or three live neighbors survives to the next generation
*  Any live cell with more than three live neighbors dies (due to overpopulation)
* Any dead cell with exactly three live neighbors becomes a live cell (reproduction)
#### *Neighboring cells: cells that are horizontally, vertically and diagonally adjacent
Those simple rules can produce really interesting patterns, some static, some moving and some curious ones!
### How to use
The project is written in Python, with the Pygame library, so you need to install these two (you can install Pygame with `pip install -r requirements.txt`). When running the game:
* Click each cell to turn it alive or dead
* Press `Space` to skip to the next generation
* Press `r` to set all cells dead
* Press `a` to toggle auto-skip generations (default: off)
* Press `t` to generate a random pattern
* Press `Esc` or click the X button to quit the game

You can skip to next generations from a given initial configuration or modify the current configuration clicking in the cells you want to switch dead/alive if the auto-skip is disabled.
### About the project construction
#### Code structure
The project was entirely written in Python in a file called `life.py`, which must be run by `python life.py` in a command-line terminal. The code is structured in the following way:
* In the beginning, I setted the constanst variables, which are the colors (there are 4 colors configured in this program, black, white, red and green, each one is a tuple with 3 number elements, RGB) and the window.
* I created a class called `Square`, used for storing in objects each square cell properties (x position, y position, color and Rect object to draw in window). This class also has the function `draw_square(self)`, which is used to draw each square cell.
* Next, there is a function to create an array of Square objects (`create_squares()`), a function to draw squares (`show_squares()`, that runs `draw_square(self)` in each square object) and a last one to check which square was clicked (`is_clicked()`).
* The game logic is based in two functions: `find_neighbors()`, which creates an array of arrays, each of them storing the number of alive neighbors of a square cell, and `LoD()` (that means "Life or Death"), which apllies the game rules in each square based on their number of alive neighbors. Running these two functions is done by the `generation()` function.
* Also, there are the functions to reset (`reset()`, set all square cells state to dead) and to create random patterns (`random()`, which goes through each square and defines if it will be dead or alive, based on random values).
* Finally, the main loop runs in a `While True` loop and checks the clicking events, finishes the program if `Esc` or X button is clicked, runs the game's logic and updates window (runs `show_squares()`) in 60 FPS (this is the default if auto-skip is disabled; else, the window update is 10 FPS by default).
* The project also uses a popular library called `Pygame`, which is designed for creating games and animations in Python. I used this library to create the game window, draw the square cells in this window, manage FPS and add user interactivity, like mouse and keyboard clicking.
#### Design choices
I made this game meaning it to be the most interactive and user-friendly as possible. The default choices I made are listed in the very beginning of the code and in the `Square` class definition:
* The window has a proportion of 800x600, defined in `line 7`. It contains a grid of squares, each one 20x20 (square_size is defined in `line 10`). These squares are generated dividing window's width and height by square_size.
* Auto-skip generations is disabled by default (`line 11`).
* Dead square cells are white (`line 35`).
* Alive square cells are green (`line 38`).
* Lines between square cells are black (`lines 39 and 40`).

I chose this duality white/green between dead/alive cells to make it more understandable as a basic 0 or 1, off/on state switching. If wanted, these colors, as well as other design choices, can be changed in the lines described above.
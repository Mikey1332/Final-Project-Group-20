# Sudoku Game

A graphical Sudoku game created with Python and Pygame as a group final project for COP3502: Programming Fundamentals 1 at the University of Florida.

## Overview

The application generates playable 9×9 Sudoku puzzles and allows users to select from multiple difficulty levels. Players can interact with the board, enter numbers, clear their entries, reset the puzzle, and check whether they have successfully completed it.

## Features

* Randomly generated Sudoku puzzles
* Easy, medium, and hard difficulty options
* Interactive graphical interface
* Selectable cells and keyboard number entry
* Reset, restart, and exit controls
* Completed-board validation
* Win and loss screens

The difficulty determines how many cells are removed from the generated board:

* **Easy:** 30 cells
* **Medium:** 40 cells
* **Hard:** 50 cells

## Technologies Used

* Python
* Pygame
* Object-oriented programming
* Two-dimensional lists
* Event-driven programming
* Git and GitHub for team collaboration

## Project Structure

* `sudoku.py` — Runs the application and manages its screens and user input
* `board.py` — Manages the Sudoku board and game state
* `cell.py` — Represents and draws individual cells
* `sudoku_generator.py` — Generates Sudoku boards and removes cells based on difficulty
* `main.sh` — Shell script for launching the game

## How to Play

1. Launch the program.
2. Select easy, medium, or hard.
3. Click an empty cell and enter a number from 1 through 9.
4. Continue until every empty cell has been filled.
5. The game will determine whether the completed board is correct.

Use the available controls to reset the current board, return to the difficulty-selection screen, or exit the game.

## About the Project

This project was developed collaboratively as the final project for COP3502 at the University of Florida. It provided experience with graphical interfaces, object-oriented design, event handling, algorithmic problem-solving, and collaborative development through GitHub.

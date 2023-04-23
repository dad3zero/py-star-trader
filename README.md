# py-star-trader: Star Trader in Python

## What is this all about ?
The original Star Trader game was written by Dave
Kaufman in BASIC back in the 70s. Dave published information about the game in "People's Computer
Company" newsletter in 1974. In 1975, the game code was printed in the wonderful
book [What to Do After You Hit Return](https://archive.org/details/Whattodoafteryouhitreturn).
Back then, it was a time for *hobbyists* so the book describes the mechanics behind
the game and ideas for improvement.

To be honest, I found all the information in [the trader project](https://github.com/true-grue/trader)
by [true-grue (Peter Sovietov)](https://github.com/true-grue). Based on those descriptions,
true-grue made his implementation in Python. He did a great job, expecially because the sources
in Python are much easier to understant than the original in Basic and so, nice to study.

But the source code remained a simple _port_ from Basic to Python and thus the code is not
*Pythonic*.

At first, I cloned the project with the intention to improve and modernize it but to be honest, it
is far better to start from scratch. 

The main reason is that this kind of project needs a lot of modernization. The original game used
a command line inerface and was entirely in memory and of course, the data structure is _simple_.
All this was certainly great in 1974, but far away from today's expectations.

There are several modernization options among which to create a web-interface game. But I wanted
to keep the original stand-alone game so, this project encouraged me to check the
[Pygame](https://www.pygame.org) library, and I decided to use it to learn basic features about
Pygame.

## Current status
With initial commit, the project is still empty.

## How to setup the project
Just do the classic: create a venv if you like, install the requirements from the `requirements.txt` file.

## Dependencies
This project uses the following dependencies:
 * ipython: used for development purpose
 * pygame: the game engine

## Documentation
A documentation with the references and gaming rules and concpets will be added.

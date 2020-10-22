=======================
Monte Carlo Tree Search
=======================

Introduction
------------
Monte Carlo Tree Search (MCTS) is a heuristic search algorithm. It is often used in game theory in the context of game trees.

Background
----------
Monte Carlo methods use random sampling to approximate a solution to a problem that might be difficult to solve analytically.

Monte Carlo tree search is an algorithm used to randomly sample a search tree. It is often useful in game theory and game AIs to search a game tree. A game tree contains all posible game outcomes, with each node being a game state, and edges are moves. For most games, a complete game tree is too large to search.

Method
------
MCTS consists of four steps:
1. Selection
2. Expansion
3. Simulation
4. Backpropagation


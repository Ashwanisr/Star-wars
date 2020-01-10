# Star-wars
Shooting game 2D using pygame

pygame,random,math library are used in this game.

If music file is loaded inside running loop by mixer.Sound it produces following error in Ubuntu 16.04
Fatal Python error: PyEval_SaveThread: NULL tstate

To avoid this mixer.load() and mixer.play() has been used inside running loop and the mixer.Sound is used in beginning to give background music. This can be swapped if it doesn't produce any error which is not the case with Ubuntu 16.04.

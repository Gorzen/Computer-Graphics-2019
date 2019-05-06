---
title: Procedural Rollercoaster
---

![Example of end result](example.jpg)
(_Image from RollerCoaster Tycoon 2_)

## Title and Summary

Rollercoaster built with stochastic L-systems. The idea is to have a functional procedurally generated rollercoaster, using predefined rules and symbols. We chose the algorithm to be stochastic so that we can have some variations. A path will be generated that goes through a set of generated 3D points and a rail segment will be repeated and curved along the path to be the final track. 

## Goals and Deliverables

This is the updated proposal after discussion with one teaching assistant.

The minimum deliverable for a passing grade (4.0) would be fully connected and realistic rollercoaster. "Realistic" means a track that is close to a real one and that *could* be realized.

The first extension would be to be able to "ride" the rollercoaster. That means setting up a camera that follows the track from start to end.

The second extension would be to add some twists to the track such as this:

![Example of end result](rollercoaster_twist.jpg)
(_Example of a rollercoaster performing a twist_)

<!-- The main goal will be to have a fully connected 3D rollercoaster, with a start and a finish point. The rollercoaster has to coherent, no collision with other roads or the ground. We should be able to ride the rollercoaster as if it was a real one.

To this, we could have these extensions (in order of our preferences) for a better grade:

- Being able to "ride" the rollercoaster, from the start to the end, as a first person camera. For this we would have to create a continuous curve that follows the entire track, we are not sure yet on how hard it will be.

- Having wagons moving on the track. When you ride the roller coaster in first person camera, you are in the train and you see it.

- Add some decorations to the track to make it more interesting (such as textures, flames, waterfalls, etc...).

- First generate a terrain procedurally and then building the rollercoaster on it.

- Being able to have options to check before the generation of the rollercoaster (eg. maximum/minimum average slope, number of different rollercoasters, max/min length, etc..)

- Get a rasterization of the final scene with OpenGL.
-->
## Schedule
*We plan to add and detail milestones when we will have a better grasp of the whole workload.*

- 29/04 : Fully understand the algorithm and gather some ideas on how to implement it in `Blender` + readings and understanding of external ressources.

- 06/05 : Implementation of a simple "Wave function collapse" algorithm in python + some basic tiles in `Blender`.

- 13/05 : Functionnal rollercoaster track (the goal of the grade 4.0).

- After that : Beginning of extensions (It will depend on which ones we do).

- 26/05 : Sell the code + demo to Disneyland.

## Resources

`Blender` to create the track, and to render the final scene.

`Python` to code the algorithm for Blender.

https://github.com/mxgmn/WaveFunctionCollapse
https://www.youtube.com/watch?v=JO8OW2zg0gY
http://pcgbook.com/
https://ieeexplore.ieee.org/document/8627334
https://docs.blender.org/api/2.79/

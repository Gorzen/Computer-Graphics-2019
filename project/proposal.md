---
title: Procedural Rollercoaster
---

![Example of end result](example.jpg)
(_Image from RollerCoaster Tycoon 2_)

## Title and Summary

Rollercoaster built with the "wave function collapse" algorithm. The idea is to have a functional procedurally generated rollercoaster, using predefined tiles and the algorithm mentionned above. Some expansions can be made, for example being able to "ride" it, building it on a procedural terrain, etc.

## Goals and Deliverables

The main goal will be to have a fully connected 3D rollercoaster, with a start and a finish point. The rollercoaster has to coherent, no collision with other roads or the ground. We should be able to ride the rollercoaster as if it was a real one.

To this, we could have these extensions (in order of our preferences) for a better grade:

- Being able to "ride" the rollercoaster, from the start to the end, as a first person camera. For this we would have to create a continuous curve that follows the entire track, we are not sure yet on how hard it will be.

- Having wagons moving on the track. When you ride the roller coaster in first person camera, you are in the train and you see it.

- Add some decorations to the track to make it more interesting (such as textures, flames, waterfalls, etc...).

- First generate a terrain procedurally and then building the rollercoaster on it.

- Being able to have options to check before the generation of the rollercoaster (eg. maximum/minimum average slope, number of different rollercoasters, max/min length, etc..)

- Get a rasterization of the final scene with OpenGL.

## Schedule
*We plan to add and detail milestones when we will have a better grasp of the whole workload.*

- 29/04 : Fully understand the algorithm and gather some ideas on how to implement it in `Blender` + readings and understanding of external ressources.

- 06/05 : Implementation of a simple "Wave function collapse" algorithm in python + some basic tiles in `Blender`.

- 13/05 : Functionnal rollercoaster track (the goal of the grade 4.0).

- After that : Beginning of extensions (It will depend on which ones we do).

- 26/05 : Sell the code + demo to Disneyland.

## Resources

`Blender` to create tiles,

`Python` to code the algorithm for Blender,

(Either `OpenGL` or `Blender` to render the scene, depending on if we do the according extension).

https://github.com/mxgmn/WaveFunctionCollapse
https://www.youtube.com/watch?v=JO8OW2zg0gY
http://pcgbook.com/
https://ieeexplore.ieee.org/document/8627334
https://docs.blender.org/api/2.79/

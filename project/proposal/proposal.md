---
title: Procedural Rollercoaster
---

![Example of end result](images/example.jpg)<br/>
(_Image from RollerCoaster Tycoon 2_)

## Title and Summary

Roller coaster built with stochastic L-systems. The idea is to have a functional procedurally generated roller coaster, using predefined rules and symbols. We chose the algorithm to be stochastic so that we can have some variations. A path will be generated that goes through a set of generated 3D points and a rail segment will be repeated and curved along the path to be the final track.

## Goals and Deliverables

This is the updated proposal after discussion with one teaching assistant and the feedback that said we should rather use L-Systems instead of the wave function collapse algorithm.

The minimum deliverable for a passing grade (4.0) would be fully connected and realistic roller coaster. "Realistic" means a track that is close to a real one and that *could* be realized. I.e the roller coaster loops and doesn't collide with itself.

1. The first extension would be to be able to "ride" the roller coaster. That means setting up a camera that follows the track from start to end in order to generate a video.

2. The second extension would be to control the twisting of the rails such that they turn more depending on the speed of the wagon. The twisting should be computed to cancel the centrifugal force, i.e. the passengers should remain on their seats.


<!-- The main goal will be to have a fully connected 3D roller coaster, with a start and a finish point. The roller coaster has to be coherent and have no collision with other roads or the ground. We should be able to ride the roller coaster as if it was a real one.

To do this, we could have these extensions (in order of our preferences) for a better grade:

- Being able to "ride" the roller coaster, from the start to the end, as a first person camera. For this we would have to create a continuous curve that follows the entire track, we are not sure yet on how hard it will be.

- Having wagons moving on the track. When you ride the roller coaster in first person camera, you are in the train and you see it.

- Add some decorations to the track to make it more interesting (such as textures, flames, waterfalls, etc...).

- First generate a terrain procedurally and then building the roller coaster on it.

- Being able to have options to check before the generation of the roller coaster (eg. maximum/minimum average slope, number of different roller coasters, max/min length, etc..)

- Get a rasterization of the final scene with OpenGL.
-->
## Schedule

- 29/04 : Fully understand the algorithm and gather some ideas on how to implement it in `Blender` + readings and understanding of external ressources.

- 06/05 : Implementation of a simple L-system in python + some basic curve in `Blender`.

- 16/05 : Functionnal rollercoaster track (the goal of the grade 4.0).

- 26/05 : Finish both extensions.

- 28/05 : Finish the presentation video.

- 31/05 : Finish webpage (final report) of the project.

- 01/06 : Finally sell the final product to DisneyLand.

## Resources

`Blender` to create the track, and to render the final scene.

`Python` to code the algorithm for Blender.

Assignment 8 of the course.

http://pcgbook.com/
https://ieeexplore.ieee.org/document/8627334
https://docs.blender.org/api/2.79/

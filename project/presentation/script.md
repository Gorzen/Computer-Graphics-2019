# Intro
- Notepad
Core goal:
###OVERVIEW, core goal
Roller coaster, procedural
**Looks reasonable + loops**
3D L System stochastic
Blender, Python
2D L-System from course
Rotation work with **sphere coordinates**

###Explain
We **start** as a loop, and every rule must ensure that the next iteration loops
We wrote all the **rules** and the L-System such that it **loops**
We then output all the points to **Blender** which draws a curve

- Iteration 1
temps
Starting loop, not every track is expandable, to have a reasonable looking coaster
But the ones in blue for example will get replaced
- Iteration 2
- Iteration 3
- Iteration 4
- Iteration 5
temps
### Can go further
All of this looks good, we managed to make a track that **fits our core goal**, looping roller coaster
But we can go **further** and we added some **extensions**
We wanted to **twist** the tracks in order to have a smoother ride, and we also thought it was fun to have random twists.
Twists add a **new dimension** to every point and we found interesting

- Vidéo Maison
court
Here we go

# Random twist
- Vidéo random twist
- Image random twist
- End twist
long
### New dimension, similar to +
Twists add another dimensions to points, to have a twist we have a **symbol** that, like + and -, change the twist angle
### End twist
Because of Blender, 360° != 0° thus to have a track that loops between beginning and end we must ensure that the angles at end and start are the same, or close.

# Twist
- Image basic
- Image realistic
Assez long
### Twist tracks to balance centrifugal force
### Speed + angle matter
### Random twist can interfere -> compromise
We twist the tracks based on an approximation of speed and the turning angles, however we have to be careful about the random twists, and try to make something meaningful with them. A compromise between realistic twists and random twists.

- Vidéo twists + split et arrêt sur image
### Twisted tracks make more sense on video
As we can see the twisted tracks make much more sense to us, on a physical stand point.

### Conclusion
- Vidéos fin
assez court
Thanks

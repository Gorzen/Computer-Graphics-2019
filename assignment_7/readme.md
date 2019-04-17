# Assignment 7

## Building View and Projection Matrices for a Cube Face
### `m_constructLightProjectionMatrix()`
In this method, we just had to use the _perspective_ matrix transformation, with a fovy of $$2*atan(0.5/0.5) * 180/PI = 90° $$ as we are in a box of length 1 (i.e. looking at a distance of 0.5), looking at an elevation height of 0.5. The ratio is 1 as we want it to be a cube, while the _far_ and _low_ values are respectively 6 and 0.1 as indicated in the assignment.

### `m_constructLightViewMatrix()`
There, we separated the cube by its faces using a switch and then computed the _up_ and _center_ value depending on the face, as stated in the theory part of the assignment. Then, we need to rotate them by x and y angles (and add the initial position of the light to the center, so that it is in the correct position), before putting them in the _look_at()_ matrix.

## Writing the Fragment Shaders
### `shadowmap_gen.frag`
This part was really straightforward as we were only asked to compute the distance between the vertex position and the light position, but because we are in eye-coordinates this distance is simply the length of the vertex position:
`dist = length(v2f_lc_vertex);`

### `phong_shadow.frag`
For this part we took our code of the phong shading from the last assignment and added a condition so that the phong is not computed when the vertex is in the shadow.
As instructed, the phong should not be added when the distance between the vertex and the light is bigger than the distance stored in the `shadow_map`. This condition is written as :
```C
if(length(light_position - v2f_ec_vertex)
    <= 1.01f *  texture(shadow_map, -pos_to_light).r)
  {
  //Compute the phong shading
}
```

## Setting the Blend Function
As the documentation indicates, we set the blend function to `glBlend(GL_ONE, GL_ONE)` so that OpenGL adds each color with an equal weight of one.
Just before that we need to enable it with `glEnable(GL_BLEND)` and disable it (`glDisable(GL_BLEND)`) at the end of the `for` loop.

### Workload
- Lucien Michaël Iseli, 274999: **33.33%**
- Lucas Strauss, 272432: **33.33%**
- Joachim Dunant, 262314: **33.33%**

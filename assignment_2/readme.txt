Exercise 1: Phong Lighting Model
  Even though the provided formula let us compute the full color (made from
  ambiant, diffuse and specular), we compute the components individually.
  In the loop that goes through all the lights, we first check (as described in
  the last section) if an object hides the light to not take into account any diffuse or specular component.
  If not we check the condition that the dot product between the normal and the light vector is greater or
  equal to zero in order to proceed. Because if that condition is not met, we don't have to compute the
  diffuse nor the specular component.
  For the specular component, we mixed up the ``reflect`` and ``mirror`` methods. But we figured out that
  ``mirror`` was the one we were looking for because the vector that is given in the parameter acts as the
  mirror plane. Once the mirrored vector is obtained, we have to check the additional condition that the
  dot product between the reflected vector and the vector that points to the camera is positive.
  After that the specular computation is straight forward.

Exercise 2: Shadows
  We implemented the shadows by checking if there is an intersection between the intersection point and the light source as explained in the lecture. If there is one we don't add diffuse and specular lighting.
  We didn't encounter any issues, we just had to make sure our ray was going in the right direction (i.e. from point to light) and to offset the intersection point a little bit to avoid noise.
  We also added a little check in case the intersection we find is beyond the light source, we aren't sure it's necessary but it makes sense so we added it.

Exercise 3: Reflections
  The reflections weren't very hard to compute, as explained in class the way our ray tracer works makes it easy to add reflections.
  We simply need to compute the color of the reflection of the light ray recursively and add it to the color with the mirror factor of the material.
  We also have to offset a little bit the origin of the reflection to make sure that the point doesn't intersect with itself which would remove reflection.


Workload:
- Lucien Michaël Iseli, 274999: 33.33%
- Lucas Strauss, 272432: 33.33%
- Joachim Dunant, 262314: 33.33%

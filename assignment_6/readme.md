# Assignment 6
### Rendering the billboard
In `Texture::createSunBillboardTexture()` we chose to map the pixel distance to the center (in the range 150 - 450) to a red value (in the range 0 - 255) so that we obtain a nice gradient from a yellowish color to a faded red. This mapped value is used to compute both the alpha and the red value.

Then, in `Solar_viewer::paint()` we compute the angles that the billboard needs to always face the camera. For the angle around the Y-axis, we simply use $tan(y_{angle}) = eye.pos_x / eye.pos_z$. It will be a bit trickier for the rotation around the X-axis, as the first rotation will change the relative `x` and `z` coordinates of the eye. To resolve this problem, we can use the `sinus` of the angle, which depends on `y` and the distance between the center of the billboard and the eye, which can be normalized :
$sin(x_{angle}) = eye.pos_y / distance = eye.pos_y / 1 = eye.pos_y$.

Finally, in `Solar_viewer::draw_scene()` we use the computed angles to rotate the billboard around the sun, so that it always faces the camera, and then scale it a bit to make it more visible. After that, we compute the shaders like another planet, i.e. by setting uniform matrices for the view and projection.

### Rendering the planets using the Phong lighting model
In `phong.vert` the function `main` is straightforward. The variables `v2f_texcoord`, `v2f_light` and `v2f_view` are assigned to the rgb values of their namesake.
Then, the remaining variables

`phong.frag` will compute the final phong shaders, by using the "phong equation" seen in the lectures, knowing the contraints written on the assignment sheet.

### Combining multiple textures to get day/night, clouds and water specularity effects for the Earth.
`earth.vert` is the same as `phong.vert` as the `.frag` files both use the same input.

`earth.frag` is a bit more complicated. We compute the ambiant light by linearly interpolating the ambient day light and the ambient night light. To linearly interpolate them we use the dot product of the normal and the light. Because it'll be 1 when the normal points directly at the light, 0 when we are right on the edge of the earth view from the light, and negative behind the earth up to -1 when we are colinear with the light. So it is perfect for this computation.
### Workload
- Lucien Michaël Iseli, 274999: **33.33%**
- Lucas Strauss, 272432: **33.33%**
- Joachim Dunant, 262314: **33.33%**

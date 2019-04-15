//=============================================================================
//
//   Exercise code for "Introduction to Computer Graphics"
//     by Julian Panetta, EPFL
//
//=============================================================================
#version 140

// Eye-space fragment position and normals from vertex shader.
in vec3 v2f_normal;
in vec3 v2f_ec_vertex;

uniform vec3 light_position; // Eye-space light position
uniform vec3 light_color;

// Material parameters
uniform vec3  diffuse_color;
uniform vec3 specular_color;
uniform float shininess;

uniform samplerCube shadow_map; // Distances in the shadow map can be accessed with texture(shadow_map, direction).r

out vec4 f_light_contribution;

void main()
{
    // Normalize the interpolated normal
    vec3 N = -sign(dot(v2f_normal, v2f_ec_vertex)) *  // Orient the normal so it always points opposite the camera rays
             normalize(v2f_normal);

    /** \todo
    * Compute this light's diffuse and specular contributions.
    * You should be able to copy your phong lighting code from assignment 6 mostly as-is,
    * though notice that the light and view vectors need to be computed from scratch
    * here; this time, they are not passed from the vertex shader.
    *
    * The light should only contribute to this fragment if the fragment is not occluded
    * by another object in the scene. You need to check this by comparing the distance
    * from the fragment to the light against the distance recorded for this
    * light ray in the shadow map.
    *
    * To prevent "shadow acne" and minimize aliasing issues, we need a rather large
    * tolerance on the distance comparison. It's recommended to use a *multiplicative*
    * instead of additive tolerance: compare the fragment's distance to 1.01x the
    * distance from the shadow map.
    ***/
    vec3 color = vec3(0.0f);

    vec3 I_l = light_color;
    vec3 m_d = diffuse_color;
    vec3 m_s = specular_color;
    float s = shininess;

    vec3 pos_to_light = normalize(light_position - v2f_ec_vertex);

    if(distance(light_position, v2f_ec_vertex) <= 1.01 *  texture(shadow_map, light_position - v2f_ec_vertex).r) {
      float n_dot_l = dot(N, pos_to_light);
      if (n_dot_l > 0) {
        color += I_l * m_d * n_dot_l;

        vec3 mirrored = (2.0 * dot(N, pos_to_light)) * N - pos_to_light;

        float r_dot_v = dot(mirrored, -normalize(v2f_ec_vertex));

        if (r_dot_v > 0) {
          color += I_l * m_s * pow(r_dot_v, s);
        }
      }
    }

    // append the required alpha value
    f_light_contribution = vec4(color, 1.0);
}

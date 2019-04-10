//=============================================================================
//
//   Exercise code for the lecture "Introduction to Computer Graphics"
//     by Prof. Mario Botsch, Bielefeld University
//
//   Copyright (C) by Computer Graphics Group, Bielefeld University
//
//=============================================================================

#version 140

in vec3 v2f_normal;
in vec2 v2f_texcoord;
in vec3 v2f_light;
in vec3 v2f_view;

out vec4 f_color;

uniform sampler2D tex;
uniform bool greyscale;

const float shininess = 8.0;
const vec3  sunlight = vec3(1.0, 0.941, 0.898);

void main()
{
    vec3 color = vec3(0.0,0.0,0.0);

    vec4 v_texture = texture(tex, v2f_texcoord);

    vec3 I_l = sunlight;
    vec3 I_a = 0.2 * sunlight;
    vec3 m_a = v_texture.rgb;
    vec3 m_d = v_texture.rgb;
    vec3 m_s = v_texture.rgb;

    vec3 pos_to_light = normalize(v2f_light - v2f_view);

    color += I_a * m_a;

    float n_dot_l = dot(v2f_normal, pos_to_light);
    if (n_dot_l > 0) {
      color += I_l * m_d * n_dot_l;

      vec3 mirrored = (2.0 * dot(v2f_normal, pos_to_light)) * v2f_normal - pos_to_light;

      float r_dot_v = dot(mirrored, -normalize(v2f_view));

      if (r_dot_v > 0) {
        color += I_l * m_s * pow(r_dot_v, shininess);
      }
    }

    // convert RGB color to YUV color and use only the luminance
    if (greyscale) color = vec3(0.299*color.r+0.587*color.g+0.114*color.b);

    // add required alpha value
    f_color = vec4(color, 1.0);
}

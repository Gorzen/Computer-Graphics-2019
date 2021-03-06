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

uniform sampler2D day_texture;
uniform sampler2D night_texture;
uniform sampler2D cloud_texture;
uniform sampler2D gloss_texture;
uniform bool greyscale;

const float shininess = 20.0;
const vec3  sunlight = vec3(1.0, 0.941, 0.898);

void main()
{
  vec3 color = vec3(0.0,0.0,0.0);
  vec3 cloud_color = vec3(0.0,0.0,0.0);

  vec4 v_day = texture(day_texture, v2f_texcoord);
  vec4 v_night = texture(night_texture, v2f_texcoord);
  vec4 v_cloud = texture(cloud_texture, v2f_texcoord);
  vec4 v_gloss = texture(gloss_texture, v2f_texcoord);

  vec3 I_l = sunlight;
  vec3 I_a = 0.2 * sunlight;

  vec3 m_a_day = v_day.rgb;
  vec3 m_d_day = v_day.rgb;
  vec3 m_s_day = vec3(1,1,1);
  vec3 m_a_night = v_night.rgb;
  float spec_value = v_gloss.r;
  float cloud_val = v_cloud.r;

  vec3 pos_to_light = normalize(v2f_light - v2f_view);

  float n_dot_l = dot(v2f_normal, pos_to_light);
  float n_dot_l_mapped = (n_dot_l + 1)/2.0;

  //Cloud ambiant color
  vec3 m_cloud = vec3(cloud_val, cloud_val, cloud_val);
  cloud_color += I_a * m_cloud * n_dot_l;

  //Ambiant
  color += I_a * m_a_day * n_dot_l_mapped + m_a_night * (1 - n_dot_l_mapped);

  if (n_dot_l > 0) {
    //Diffuse
    color += I_l * m_d_day * n_dot_l;
    cloud_color += I_l * m_cloud * n_dot_l;

    vec3 mirrored = (2.0 * dot(v2f_normal, pos_to_light)) * v2f_normal - pos_to_light;

    float r_dot_v = dot(mirrored, -normalize(v2f_view));

    //Specular
    if (r_dot_v > 0) {
      color += I_l * m_s_day * pow(r_dot_v, shininess) * spec_value * (1 - cloud_val);
    }
  }

  //Linear interpolation between cloud and phong
  color = color * (1 - cloud_val) + cloud_color * cloud_val;

  // convert RGB color to YUV color and use only the luminance
  if (greyscale) color = vec3(0.299*color.r+0.587*color.g+0.114*color.b);

  // add required alpha value
  f_color = vec4(color, 1.0);
}

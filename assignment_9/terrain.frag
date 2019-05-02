//=============================================================================
//
//   Exercise code for the lecture "Introduction to Computer Graphics"
//     by Prof. Mario Botsch, Bielefeld University
//
//   Copyright (C) by Computer Graphics Group, Bielefeld University
//
//=============================================================================

#version 140

uniform vec3 light_position; // Eye-space light position

in vec3  v2f_ec_vertex;
in vec3  v2f_normal;
in float v2f_height;

out vec4 f_color;

const vec3  sunlight = vec3(1.0, 0.941, 0.898);
// Small perturbation to prevent "z-fighting" on the water on some machines...
const float terrain_water_level    = -0.03125 + 1e-6;
const vec3  terrain_color_water    = vec3(0.29, 0.51, 0.62);
const vec3  terrain_color_mountain = vec3(0.8, 0.5, 0.4);
const vec3  terrain_color_grass    = vec3(0.33, 0.43, 0.18);

void main()
{
	const vec3 ambient = 0.2 * sunlight; // Ambient light intensity
	float height = v2f_height;

    /**
	 * \todo Compute the terrain color ("material") and shininess based on the height as
	 * described in the handout.
	 *
	 * Water:
	 *		color = terrain_color_water
	 *		shininess = 8.0
	 * Ground:
	 *		color = interpolate between terrain_color_grass and terrain_color_mountain, weight is (height - terrain_water_level)*2
	 * 		shininess = 0.5
     */
	vec3 material = vec3(0);
	float shininess = 0;

	if(height > terrain_water_level) {
		// Ground
		material = mix(terrain_color_grass, terrain_color_mountain, (height - terrain_water_level) * 2);
		shininess = 0.5;
	} else {
		// Water
		material = terrain_color_water;
		shininess = 8.0;
	}

    /**
	 * \todo Paste your Phong fragment shading code from assignment 6/7 here,
	 * altering it to use the terrain color as the ambient, diffuse, and
	 * specular materials.
     */
	vec3 color = vec3(0.0,0.0,0.0);

 	vec3 I_l = sunlight;
 	vec3 I_a = ambient;
 	vec3 m_a = material;
 	vec3 m_d = material;
 	vec3 m_s = material;

 	vec3 pos_to_light = normalize(light_position - v2f_ec_vertex);

 	color += I_a * m_a;

 	float n_dot_l = dot(v2f_normal, pos_to_light);
 	if (n_dot_l > 0) {
 		color += I_l * m_d * n_dot_l;

 		vec3 mirrored = (2.0 * dot(v2f_normal, pos_to_light)) * v2f_normal - pos_to_light;

 		float r_dot_v = dot(mirrored, -normalize(v2f_ec_vertex));

 		if (r_dot_v > 0) {
 			color += I_l * m_s * pow(r_dot_v, shininess);
 		}
 	}

 	f_color = vec4(color, 1.0);
}

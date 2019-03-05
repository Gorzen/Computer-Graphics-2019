//=============================================================================
//
//   Exercise code for the lecture
//   "Introduction to Computer Graphics"
//   by Prof. Dr. Mario Botsch, Bielefeld University
//
//   Copyright (C) Computer Graphics Group, Bielefeld University.
//
//=============================================================================

//== INCLUDES =================================================================

#include "Cylinder.h"
#include "SolveQuadratic.h"

#include <array>
#include <cmath>

//== IMPLEMENTATION =========================================================

bool
Cylinder::
intersect(const Ray&  _ray,
          vec3&       _intersection_point,
          vec3&       _intersection_normal,
          double&     _intersection_t) const
{
  const vec3 d = _ray.direction;
  const vec3 y = _ray.origin - center;
  const vec3 v = axis;
  const double r = radius;

  const double a = dot(d, d) - dot(d, v) * dot(d, v);
  const double b = 2 * (dot(d, y) - dot(d, v) * dot(y, v));
  const double c = dot(y, y) - r * r - dot(y, v) * dot(y, v);

  std::array<double, 2> t;
  size_t nsol = solveQuadratic(a, b, c, t);

  _intersection_t = NO_INTERSECTION;

  vec3 normal;

  // Find the closest valid solution (in front of the viewer)
  /**
   * Le problème est là ! Si on inverse le signe
   * _intersection_t = -std::min(_intersection_t, t[i]);
   * alors on voit que l'intérieur du cylindre (plus l'extérieur)
   */
  for (size_t i = 0; i < nsol; ++i) {
    if(t[i] > 0 && (_intersection_t == NO_INTERSECTION || _intersection_t > t[i])) {
      vec3 point = _ray(t[i]);
      vec3 projection = dot((point - center), v) * v + center;

      // Check point is on cylinder
      if (norm(projection - center) <= height / 2.0) {
        _intersection_t = t[i];
        normal = (point - projection) / r;
      }
    }
  }

  if (_intersection_t == NO_INTERSECTION) return false;

  /**
   * J'essaie de tester si l'angle entre le rayon et la normale est plus grand que 90°, dans ce cas
   * ça veut dire que la normale est dans le mauvais sens
  double angle_ray_normal = dot(d, normal)/(norm(normal)*norm(d)); //Donne le cos de l'angle
  if (angle_ray_normal < 0){ // cos négatif => angle plus grand que 90°
    const vec3 null_vec = vec3(0);
    normal = null_vec - normal; //pour inverser les composantes
    normal = reflect(normal, d); //un autre essai pour tenter de changer la direction du vecteur
  }
  */

  double angle_ray_normal = dot(d, normal)/(norm(normal)*norm(d)); //Donne le cos de l'angle
  if (angle_ray_normal > 0){ // cos négatif => angle plus grand que 90°
    const vec3 null_vec = vec3(0);
    normal = null_vec - normal; //pour inverser les composantes
  }

  _intersection_point  = _ray(_intersection_t);
  _intersection_normal = normal;

  return true;
}
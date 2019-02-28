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

  // Find the closest valid solution (in front of the viewer)
  for (size_t i = 0; i < nsol; ++i) {
      if (t[i] > 0) _intersection_t = std::min(_intersection_t, t[i]);
  }

  if (_intersection_t == NO_INTERSECTION) return false;

  const vec3 point = _ray(_intersection_t);
  const vec3 projection = dot((point - center), v) * v + center;
  const vec3 normal = (point - projection) / r;

  // Check point is on cylinder
  if(norm(projection - center) > height / 2.0){
    _intersection_t = NO_INTERSECTION;
    return false;
  }

  _intersection_point  = point;
  _intersection_normal = normal;

  return true;
}

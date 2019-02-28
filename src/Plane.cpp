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

#include "Plane.h"
#include <limits>


//== CLASS DEFINITION =========================================================



Plane::Plane(const vec3& _center, const vec3& _normal)
: center(_center), normal(_normal)
{
}


//-----------------------------------------------------------------------------


bool
Plane::
intersect(const Ray& _ray,
          vec3&      _intersection_point,
          vec3&      _intersection_normal,
          double&    _intersection_t ) const
{
   double divisor = dot(normal, _ray.direction);

    _intersection_t = NO_INTERSECTION;

    if(abs(divisor) < 1e-6)
      return false;

    double t = dot(normal, (center - _ray.origin)) / divisor;

    if(t < 0) return false;
    else {
        _intersection_t = t;
        _intersection_point = _ray(t);
        _intersection_normal = normal;
    }
    return true;
}


//=============================================================================

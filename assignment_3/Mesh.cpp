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

#include "Mesh.h"
#include <fstream>
#include <string>
#include <stdexcept>
#include <limits>


//== IMPLEMENTATION ===========================================================


Mesh::Mesh(std::istream &is, const std::string &scenePath)
{
    std::string meshFile, mode;
    is >> meshFile;

    // load mesh from file
    read(scenePath.substr(0, scenePath.find_last_of("/\\") + 1) + meshFile); // Use both Unix and Windows path separators

    is >> mode;
    if      (mode ==  "FLAT") draw_mode_ = FLAT;
    else if (mode == "PHONG") draw_mode_ = PHONG;
    else throw std::runtime_error("Invalid draw mode " + mode);

    is >> material;
}


//-----------------------------------------------------------------------------


bool Mesh::read(const std::string &_filename)
{
    // read a mesh in OFF format


    // open file
    std::ifstream ifs(_filename);
    if (!ifs)
    {
        std::cerr << "Can't open " << _filename << "\n";
        return false;
    }


    // read OFF header
    std::string s;
    unsigned int nV, nF, dummy, i;
    ifs >> s;
    if (s != "OFF")
    {
        std::cerr << "No OFF file\n";
        return false;
    }
    ifs >> nV >> nF >> dummy;
    std::cout << "\n  read " << _filename << ": " << nV << " vertices, " << nF << " triangles";


    // read vertices
    Vertex v;
    vertices_.clear();
    vertices_.reserve(nV);
    for (i=0; i<nV; ++i)
    {
        ifs >> v.position;
        vertices_.push_back(v);
    }


    // read triangles
    Triangle t;
    triangles_.clear();
    triangles_.reserve(nF);
    for (i=0; i<nF; ++i)
    {
        ifs >> dummy >> t.i0 >> t.i1 >> t.i2;
        triangles_.push_back(t);
    }


    // close file
    ifs.close();


    // compute face and vertex normals
    compute_normals();

    // compute bounding box
    compute_bounding_box();


    return true;
}


//-----------------------------------------------------------------------------

// Determine the weights by which to scale triangle (p0, p1, p2)'s normal when
// accumulating the vertex normals for vertices 0, 1, and 2.
// (Recall, vertex normals are a weighted average of their incident triangles'
// normals, and in our raytracer we'll use the incident angles as weights.)
// \param[in] p0, p1, p2    triangle vertex positions
// \param[out] w0, w1, w2    weights to be used for vertices 0, 1, and 2
void angleWeights(const vec3 &p0, const vec3 &p1, const vec3 &p2,
                  double &w0, double &w1, double &w2) {
    // compute angle weights
    const vec3 e01 = normalize(p1-p0);
    const vec3 e12 = normalize(p2-p1);
    const vec3 e20 = normalize(p0-p2);
    w0 = acos( std::max(-1.0, std::min(1.0, dot(e01, -e20) )));
    w1 = acos( std::max(-1.0, std::min(1.0, dot(e12, -e01) )));
    w2 = acos( std::max(-1.0, std::min(1.0, dot(e20, -e12) )));
}


//-----------------------------------------------------------------------------

void Mesh::compute_normals()
{
    // compute triangle normals
    for (Triangle& t: triangles_)
    {
        const vec3& p0 = vertices_[t.i0].position;
        const vec3& p1 = vertices_[t.i1].position;
        const vec3& p2 = vertices_[t.i2].position;

        t.normal = normalize(cross(p1-p0, p2-p0));
    }

    // initialize vertex normals to zero
    for (Vertex& v: vertices_)
    {
        v.normal = vec3(0,0,0);
    }

     // For each triangle, compute the normal of its vertices, depending of their weights.
     for (const Triangle& t: triangles_)
     {
       // The vertices of the triangle
       Vertex& v0 = vertices_[t.i0];
       Vertex& v1 = vertices_[t.i1];
       Vertex& v2 = vertices_[t.i2];

       double w0;
       double w1;
       double w2;

       // Compute the weights of this triangle for each vertex
       angleWeights(v0.position, v1.position, v2.position, w0, w1, w2);

       // Add the weighted triangle's normal to the vertex normal
       v0.normal += w0 * t.normal;
       v1.normal += w1 * t.normal;
       v2.normal += w2 * t.normal;
     }

     // Normalize the normals of the vertices
     for (Vertex& v: vertices_)
     {
       v.normal = normalize(v.normal);
     }
}


//-----------------------------------------------------------------------------


void Mesh::compute_bounding_box()
{
    bb_min_ = vec3(std::numeric_limits<double>::max());
    bb_max_ = vec3(std::numeric_limits<double>::lowest());

    for (Vertex v: vertices_)
    {
        bb_min_ = min(bb_min_, v.position);
        bb_max_ = max(bb_max_, v.position);
    }
}


//-----------------------------------------------------------------------------


bool Mesh::intersect_bounding_box(const Ray& _ray) const
{

    /** \todo
    * Intersect the ray `_ray` with the axis-aligned bounding box of the mesh.
    * Note that the minimum and maximum point of the bounding box are stored
    * in the member variables `bb_min_` and `bb_max_`. Return whether the ray
    * intersects the bounding box.
    * This function is ued in `Mesh::intersect()` to avoid the intersection test
    * with all triangles of every mesh in the scene. The bounding boxes are computed
    * in `Mesh::compute_bounding_box()`.
    */

    const double min_x = bb_min_[0];
    const double min_y = bb_min_[1];
    const double min_z = bb_min_[2];

    const double max_x = bb_max_[0];
    const double max_y = bb_max_[1];
    const double max_z = bb_max_[2];

    const vec3 o = _ray.origin;
    const vec3 d = _ray.direction;

    // o + td = bb_min or bb_max => t = (bb_min - o) / d
    float txmin = (min_x - o[0]) / d[0];
    float txmax = (max_x - o[0]) / d[0];

    // If the ray comes from the "wrong" direction, swap min and max
    if (txmin > txmax) {
      float temp = txmax;
      txmax = txmin;
      txmin = temp;
    }

    // Same for y coordinates
    float tymin = (min_y - o[1]) / d[1];
    float tymax = (max_y - o[1]) / d[1];

    if (tymin > tymax) {
      float temp = tymax;
      tymax = tymin;
      tymin = temp;
    }

    // The ray doesn't go through the box
    if ((txmin > tymax) || (tymin > txmax)) {
        return false;
    }

    if (tymin > txmin)
      txmin = tymin;

    if (tymax < txmax)
      txmax = tymax;

    // Same for z coordinates
    float tzmin = (min_z - o[2]) / d[2];
    float tzmax = (max_z - o[2]) / d[2];

    if (tzmin > tzmax) {
      float temp = tzmax;
      tzmax = tzmin;
      tzmin = temp;
    }

    if ((txmin > tzmax) || (tzmin > txmax)) {
      return false;
    }

    return true;
}


//-----------------------------------------------------------------------------


bool Mesh::intersect(const Ray& _ray,
                     vec3&      _intersection_point,
                     vec3&      _intersection_normal,
                     double&    _intersection_t ) const
{
    // check bounding box intersection
    if (!intersect_bounding_box(_ray))
    {
        return false;
    }

    vec3   p, n;
    double t;

    _intersection_t = NO_INTERSECTION;

    // for each triangle
    for (const Triangle& triangle : triangles_)
    {
        // does ray intersect triangle?
        if (intersect_triangle(triangle, _ray, p, n, t))
        {
            // is intersection closer than previous intersections?
            if (t < _intersection_t)
            {
                // store data of this intersection
                _intersection_t      = t;
                _intersection_point  = p;
                _intersection_normal = n;
            }
        }
    }

    return (_intersection_t != NO_INTERSECTION);
}


//-----------------------------------------------------------------------------

double matrix_det(vec3 col_1, vec3 col_2, vec3 col_3)
{
  return    col_1[0] * (col_2[1] * col_3[2] - col_3[1] * col_2[2])
          - col_2[0] * (col_1[1] * col_3[2] - col_3[1] * col_1[2])
          + col_3[0] * (col_1[1] * col_2[2] - col_2[1] * col_1[2]);
}

double solve_cramer_variable(vec3 col_1, vec3 col_2, vec3 col_3, double denominator)
{
  return matrix_det(col_1, col_2, col_3) / denominator;
}

bool solve_cramer(vec3 a, vec3 b, vec3 c, vec3 d, vec3& sol)
{
  double denominator = matrix_det(a, b, c);

  if (denominator == 0)
    return false;

  // See https://en.wikipedia.org/wiki/Cramer%27s_rule#Applications for detailed implementation
  sol = vec3(
    solve_cramer_variable(d, b, c, denominator),
    solve_cramer_variable(a, d, c, denominator),
    solve_cramer_variable(a, b, d, denominator)
  );

  return true;
}


bool
Mesh::
intersect_triangle(const Triangle&  _triangle,
                   const Ray&       _ray,
                   vec3&            _intersection_point,
                   vec3&            _intersection_normal,
                   double&          _intersection_t) const
{
    const vec3& p0 = vertices_[_triangle.i0].position;
    const vec3& p1 = vertices_[_triangle.i1].position;
    const vec3& p2 = vertices_[_triangle.i2].position;

     // Solving equation, done in readme to compute t, alpha, gamma and beta
     const vec3 a = _ray.direction;
     const vec3 b = p0 - p1;
     const vec3 c = p0 - p2;
     const vec3 d = p0 - _ray.origin;

     // sol = (t, beta, gamma), see readme for detailed implementation
     vec3 sol;

     _intersection_t = NO_INTERSECTION;

     if(!solve_cramer(a, b, c, d, sol))
      return false;

      //Extract solutions
     const double t = sol[0];
     const double beta = sol[1];
     const double gamma = sol[2];
     const double alpha = 1 - beta - gamma;

     if (alpha < 0 || beta < 0 || gamma < 0 || beta > 1 || gamma > 1 || t <= 0)
      return false;

    // Return t and intersection point
    _intersection_t = t;
    _intersection_point = _ray(t);

    // Return normal
    // Check if flat or Phong shading
    if(draw_mode_ == PHONG) {
      const vec3 n0 = vertices_[_triangle.i0].normal;
      const vec3 n1 = vertices_[_triangle.i1].normal;
      const vec3 n2 = vertices_[_triangle.i2].normal;

      vec3 normal = alpha * n0 + beta * n1 + gamma * n2;

      _intersection_normal = normalize(normal);
    } else {
      _intersection_normal = _triangle.normal;
    }

    return true;
}

//=============================================================================

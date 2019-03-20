<!-- See readme.pdf to have the intended look of the readme (Latex) -->

# Assignment 3

### Vertex Normals
This exercise was pretty straight-forward. As indicated in the PDF file of the assignement, we loop through each triangle, and multiply each vertex normal by the weights (computed with ``angleWeights``). Then, we loop again through each Vertex to normalize the normals.

### Ray-Triangle intersection + normal calculations

To compute the intersection between our ray and each triangle efficiently, we will use Cramer's rule. For that, we need to arrange the triangle equation so that we get the form $\bold{A}\bold{\vec{x}} = \bold{\vec{b}}$, where **A** is a *3 x 3* matrix, **x** and **b** are vectors of dimension *3*. In other words, we want to find an equation of the form :
$$
x_1 \cdot \bold{\vec{a_1}} + x_2 \cdot \bold{\vec{a_2}} + x_3 \cdot \bold{\vec{a_3}} = \bold{\vec{b}}
$$

where $ \bold{\vec{a_1}}, \bold{\vec{a_2}}, \bold{\vec{a_3}}$ are respectively the first, second and third columns of $\bold{A}$ and $x_1, x_2, x_3$ the components of the vector **x**.

We then need the 3 vertices of the triangle, $\bold{\vec{A}}, \bold{\vec{B}}, \bold{\vec{C}}$, the origin of the ray $\bold{\vec{o}}$ and its direction $\bold{\vec{d}}$ :

$$
\bold{\vec{o}} + t \cdot \bold{\vec{d}} = \alpha \cdot \bold{\vec{A}} + \beta \cdot \bold{\vec{B}} + \gamma \cdot \bold{\vec{C}}\\
\bold{\vec{o}} + t \cdot \bold{\vec{d}} = (1 - \beta - \gamma) \cdot \bold{\vec{A}} + \beta \cdot \bold{\vec{B}} + \gamma \cdot \bold{\vec{C}}\\
\bold{\vec{o}} + t \cdot \bold{\vec{d}} = \bold{\vec{A}} - \beta \cdot \bold{\vec{A}} - \gamma \cdot \bold{\vec{A}} + \beta \cdot \bold{\vec{B}} + \gamma \cdot \bold{\vec{C}}\\
\bold{\vec{o}} + t \cdot \bold{\vec{d}} - \bold{\vec{A}} + \beta \cdot \bold{\vec{A}} + \gamma \cdot \bold{\vec{A}} - \beta \cdot \bold{\vec{B}} - \gamma \cdot \bold{\vec{C}} = 0\\
\bold{\vec{o}} + t \cdot \bold{\vec{d}} + \beta \cdot \bold{\vec{A}} + \gamma \cdot \bold{\vec{A}} - \beta \cdot \bold{\vec{B}} - \gamma \cdot \bold{\vec{C}} = \bold{\vec{A}}\\
\implies\\
\left(\begin{array}{cc}
t \cdot \bold{d}_{1} + \beta \cdot (\bold{A}_{1} - \bold{B}_{1}) + \gamma \cdot (\bold{A}_{1} - \bold{C}_{1}) = \bold{A}_{1} - \bold{o}_{1}\\
t \cdot \bold{d}_{2} + \beta \cdot (\bold{A}_{2} - \bold{B}_{2}) + \gamma \cdot (\bold{A}_{2} - \bold{C}_{2}) = \bold{A}_{2} - \bold{o}_{2}\\
t \cdot \bold{d}_{3} + \beta \cdot (\bold{A}_{3} - \bold{B}_{3}) + \gamma \cdot (\bold{A}_{3} - \bold{C}_{3}) = \bold{A}_{3} - \bold{o}_{3}
\end{array}\right)\\
\implies\\
\left(\begin{array}{cc}
\bold{d}_{1} & \bold{A}_{1} - \bold{B}_{1} & \bold{A}_{1} - \bold{C}_{1}\\
\bold{d}_{2} & \bold{A}_{2} - \bold{B}_{2} & \bold{A}_{2} - \bold{C}_{2}\\
\bold{d}_{3} & \bold{A}_{3} - \bold{B}_{3} & \bold{A}_{3} - \bold{C}_{3}
\end{array}\right)
\left(\begin{array}{cc}
t\\
\beta\\
\gamma
\end{array}\right)=
\left(\begin{array}{cc}
\bold{A}_{1} - \bold{o}_{1}\\
\bold{A}_{2} - \bold{o}_{2}\\
\bold{A}_{3} - \bold{o}_{3}
\end{array}\right)
$$

Then we implemented Cramer's algorithm to solve this equation following [this Wikipedia page](https://en.wikipedia.org/wiki/Cramer%27s_rule#Applications).

To compute the solution using Cramer's algorithm we modularized our code with three utility functions that:
1. Computes the determinant of a matrix
2. Solves one equation
3. Solves the whole system

### Bounding box intersection
The code for this part was inspired by the algorithm found on [this website](https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-box-intersection). We mainly changed some variable names for clarity but the algorithm is the same. </br>
Because we are looking to solve $ bb_{min} \leq o + t \cdot \vec{d} \leq bb_{max} $ we manually solve this for $x$, $y$ and $z$ in the bounding case (i.e. $ bb_{min} = o + t \cdot \vec{d}$ and $ bb_{max} = o + t \cdot \vec{d}$). That means we check for each component that we are intersecting with the box, swapping the variables when needed to ensure the minimum is always less than the maximum. </br>
This algorithm seems to work fine, as you can see on the degub_aabb images in the folder.

### Workload
- Lucien Michaël Iseli, 274999: **33.33%**
- Lucas Strauss, 272432: **33.33%**
- Joachim Dunant, 262314: **33.33%**

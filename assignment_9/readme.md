# Assignment 9

## 1. Perlin Noise in 1D
Compute the noise was fairly easy, we just followed the instructions on the handout.
1. Compute corners c0 and c1
2. Get gradients g0 and g1 using hash function
3. Compute $\phi_0(x - c0)$ and $\phi_1(x - c1)$
4. $t = x - c0$
5. Mix $\phi_0(x - c0)$ and $\phi_1(x - c1)$ with the weight function computed at t.

## 2. Fractional Brownian Motion
Simply wrote the given sum in C++ code. For loop that adds the ith component at each iteration.

## 3. Perlin Noise 2D
### Noise
Same as 1D but slightly more involved, followed what the pdf said.
1. Compute corners c00, c10, c01 and c11
2. Get gradients g00, g10, g01, g11 with hash function
3. Compute vectors from corners to point: a, b, c and d (as in pdf)
4. Compute the dot products of gradient and (a, b, c, d). Results are called s, t, u, v as in pdf
5. Compute x distance from point to c00, same for y
6. Compute st and uv as said in pdf by mixing s & t and u & v respectively, with distance x and weight function.
7. Noise is mix of st and uv with distance y. Using weight function again.

### FBM
Again, simply rewriting the sum in C++, with a dot product

### Turbulence
Same as FBM but with absolute value

## 4. Textures
### World
1. Compute $s = fbm(p)$
2. If s <= water level, return water color else step 3
3. $\alpha = (s - s_{water})$
4. Mix between grass color and mountain color with alpha

### Wood
1. $\alpha = \frac{1}{2} \times (1 + sin(100 \times (\left\lVert p\right\rVert + 0.15 \times turbulence(p))))$
2. Mix between dark brown and light brown with alpha

### Marble
1. $q = (fbm(p), fbm(p + (1.7, 4.6)))$
2. $\alpha = \frac{1}{2} \times (1 + fbm(p + 4 \times q))$
3. Mix between light brown and dark brown with alpha

## 5. Terrain

### Workload
- Lucien Michaël Iseli, 274999: **33.33%**
- Lucas Strauss, 272432: **33.33%**
- Joachim Dunant, 262314: **33.33%**

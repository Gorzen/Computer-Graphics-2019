How we solved each exercise:
	1. Ray-plane intersection:
		We simply followed the same pattern as in Sphere.cpp but we changed the quadratic equation of the sphere to the equation of the plane we were given. Which has only 1 solution so it is even easier. We also simply added a check on the divisor, so that if it's close to zero we return false and stop.
	2. Ray-cylinder intersection + normal derivations:
		We found the implicit equation of the cylinder online and checked that it made sense, then we solved it (see the pdf file).
	3. Ray-cylinder intersection implementation:	
		We then again first followed the same pattern, considering an infinite cylinder. But then of course the issue we had is that the cylinder is infinite which isn't what we want. So we have to only consider points that are actually on the cylinder.
		To do that we added a check when we iterate through the t's we found that satisfy the equation. When we find a t, we calculate the point then we calculate the projection of that point on the cylinder's axis and then compute the distance between the projection and the center of the cylinder. If the distance is too big (i.e. > height/2.0) we discard that point. We compute the projection with the formula we added in the pdf.
		However one issue we had is that we have to make that check when considering the t's and not only on the closest one we found. Because since we consider an infinite cylinder, when we should see a point that is on the inside of the cylinder this means that on the infinite cylinder we won't see it and see a point that is on the outside, you can't see inside an infinite cylinder unless you're in it. So we fixed that by considering all solutions of t's and only accepting it if we actually see it.
	4. Cylinder normal implementation:
		Since we had the projection of the intersection point on the cylinder's axis, it wasn't difficult to compute the normal, simply subtract the projection from the intersection and divide by radius to normalize it and there you go. However we then had a color issue on our images and color is determined by the normal. So we looked into it and the problem was the sign of the normal, also thanks to the moodle post we knew the normal had to face the observer. So we check the direction of the normal and change it accordingly.


Workload:
- Lucien Michaël Iseli, 274999: 33.33%
- Lucas Strauss, 272432: 33.33%
- Joachim Dunant, 262314: 33.33%

# Math 340 Notes

## Convexity

### Convex Set (Affine Transformation)

A convex set $s$ in $\mathbb{R}^n$ is a set for which any two point $x,y$ from
the set:

$$(1 - t)x + ty \in S$$

### Convex Combination

TODO

### Properties:

- Convexity is preserved by Minkowski Sum
- Convexity is preserved by Intersection

## Simplex Method

### Dictionary

TODO

### Basic and Non-Basic variables

Non-Basic variables are on the RHS, and Basic Variables are on the LHS Reason:
For a dictionary, basic variables and their values represent a basic feasible
solution, hence the LHS variables are called basic. Entering & Leaving variables

Entering & Leaving refers to entering & leaving the basic feasible solution
Hence entering variable is non-basic to basic, and leaving variable is basic to non-basic.

### Minimal Ratio Test

TODO

### Geometric meaning

Simplex method takes advantage that the feasible region is convex
(no local maximum), and greedily chooses the direction of steepest
ascent (largest coefficient as entering variable), while using minimum
ratio test to ensure that it doesn't go out of feasible region.

Entering variable represents the direction of ascent, leaving variable 
represents the hyperplane to stop at. (with minimum ratio test makes sure it stops as next vertex (instead of out of bound). The minimum ratio is the step size (of ascent).

A dictionary represents a vertex. But more specifically, a dictionary 
for an $\mathbb{R}^n$ Linear Program represents $n$ active hyperplanes
(such that the intersection of hyperplanes form a vertex). This
is the cause of degeneracy (for $n + k$ hyperplanes, we can choose any n
hyperplanes to represent the vertex, resulting in $\binom{n + k}{n}$).

For each pivot operation, we remove an active hyperplane and replace it with another with gaussian elimination.

### Tie in leaving variable

A tie in leaving variable indicates that there are more than 1 hyperplanes to stop at (during a pivot operation.) 

Therefore, the next dictionary will be degenerate. (as more than $n$
hyperplanes will intersect at next point.

### Infeasible dictionary

An infeasible dictionary is a dictionary for which the current basic solution is
partly (or all) negative).

### Anstee’s rule:

Choose entering variable with largest positive coefficient in objective function
Choose leaving variable with smallest positive ratio for entering variable
Basically we want to maximize that variable without potentially making other
basic variables negative When tie, choose the leaving variable with lowest
subscript This avoids cycling Note: the first 2 are standard simplex rule, the
3rd rule is added to deal with degenerative dictionary (simplex run in a cycle).

### Non-unique optimal solutions:

Sometimes, there can be a set of optimal solutions (that maximizes the objective
function). It is indicated by having no entering variable yet having leaving
variables.

In that case, the set can be characterized by: find a non-basic variable that
does not present in objective function (coefficient 0) Let that be entering, use
standard procedure to choose the leaving variable. The new basic solution is a
vertex of the optimal solution set.

The above procedure can be used to find all the vertices… (intuitively as
product of convexity, there should never be the case of two vertices only
connected by 1 vertex in between that is non optimal.

### Dictionary as combination

- A dictionary is a combination of $n$ intersecting hyperplanes
- A dictionary has $n$ nonbasic variables and $m$ basic variables, and their combination uniquely maps to a dictionary (aka cannot have two dict with same combination of nonbasic and basic variables yet different coefficients)

## Half Spaces & Hyperplanes

### Half Spaces:

A half space is quite literally one side of a hyperplane that cuts
$\mathbb{R}^n$ in half. It is characterized by:

$$\{x \in \mathbb{R}^n: A^T x \leq B, A,B \in \mathbb{R}^n\}$$

Or it can be a open set, for which:

$$\{x \in \mathbb{R}^n: A^T x < B, A,B \in \mathbb{R}^n\}$$

Note: a half space is convex.

### Hyperplanes:

$$\{x \in \mathbb{R}^n: A^T x = B, A,B \in \mathbb{R}^n\}$$

Note: a hyperplane is also convex.

### Connection to LP

- Each LP constraint is a half space.
- LP feasible region are intersection of half spaces (which is a polytope).
- By convex set property, LP feasible region is convex
  - Implies that there will not be local minimum
  - Enables simplex method's greedy strategy (of moving to next vertex with
    higher objective function value)

## Duality

Primal:

Maximize $c^{T}x$, when:

$$
Ax \leq B \\
x \geq 0
$$

Dual:

Minimize $b^{T}y$, when:

$$
A^T{y} \geq c \\
y \geq 0
$$

Similarity:

- If one of primal & dual is unbounded, the other is infeasible.
  - The converse is not true (both can be infeasible)
- If one of primal & dual has optimal solution, the other
share the same optimum.

### Noteworthy facts

- Dual of dual is primal

Quick proof:

Dual:

Minimize $b^{T}y$, when:

$$
A^T{y} \geq c \\
y \geq 0
$$

We then take the SD of it:

Maximize $-b^{T}y$, when:

$$
-A^T{y} \leq -c \\
y \geq 0
$$

Then we take the dual of it:

Minimize $-c^Tx$
$$
-(A^{T})^{T} {x} \geq -c \\
x \geq 0
$$

- If dual is feasible, primal cannot be unbounded.
  - Reason: by weak duality, if primal is unbounded,
  then primal would be step out of duality gap.

### Weak Duality Theorem

The objective function of a primal is less than or equal to the objective function of the dual (for any feasible solutions of the two).

Aka max of primal <= min of dual

In fact the prof claims that it is always true for any 
duality in optimization (beyond LP).


Proof (Summation):

Note $A^Ty \geq c$ (dual constraint), and $Ax \leq B$, then:

Then
$$
\sum_{j = 1}^{n} c_{j} x_{j} \leq \sum_{j = 1}^{n} (\sum_{i = 1}^{m} a_{ij} y_{i}) x_{j} = \sum_{i = 1}^{m} (\sum_{j = 1}^{n} a_{ij} x_{j}) y_{i} \leq  \sum_{i = 1}^{n} b_{i} y_{i}
$$

Proof (Linear algebra)

$$
c^Tx \leq (A^Ty)^T = y^T Ax \leq y^Tb = b^Ty
$$

### Strong Duality theorem

 max of primal == min of dual (no duality gap)

## Degeneracy

A dictionary is *degenerate* if one of the row's constant term is 0.

For Example:

$$
\zeta = 5 + x_{3} - x_{1} \\
x_{2} = 5 + 2x_{3} - 3x_{1} \\
x_{4} = 7 - 4x_{1} \\
x_{5} = x_{1}
$$

Such dictionary may *produce difficulty* for simplex algorithm, or it might not. The difficulty can be:

- Slowing down the algorithm
- In worst case causes cycle (not for Anstee's rule, 
but for many other pivoting rule)

An other interp. for degenerative dictionary is that, in the feasible
region of an LP with dimension n, there are more than n hyperplanes 
intersecting at a single vertex (Redundant constraints).

### Lemma

If simplex method never terminates, it must cycles.

Proof:

Say we have $n, m$ basic & nonbasic variables, then
the total number of dictionaries are:

$$
\binom{n + m}{n}
$$

Which is a finite number. And, a non-terminating procedure
will eventually encounter one of the dictionaries that it already travelled, causing cycle.

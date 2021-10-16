# Math 340 Notes

## Convexity

### Convex Set (Affine Transformation)

A convex set $s$ in $\mathbb{R}^n$ is a set for which any two point $x,y$ from
the set:

$$(1 - t)x + ty \in S$$

### Convex Combination (TODO)

### Properties:

- Convexity is preserved by Minkowski Sum
- Convexity is preserved by Intersection

## Simplex Method

### Basic and Non-Basic variables

Non-Basic variables are on the RHS, and Basic Variables are on the LHS Reason:
For a dictionary, basic variables and their values represent a basic feasible
solution, hence the LHS variables are called basic. Entering & Leaving variables

Entering & Leaving refers to entering & leaving the basic feasible solution!
Hence entering variable is non-basic to basic, and leaving variable is basic to
non-basic.

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

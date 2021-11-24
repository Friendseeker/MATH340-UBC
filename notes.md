# Convexity

## Convex Set (Affine Transformation)

A convex set $s$ in $\mathbb{R}^n$ is a set for which any two point $x,y$ from
the set:

$$(1 - t)x + ty \in S$$

## Convex Combination

TODO

## Properties:

- Convexity is preserved by Minkowski Sum
- Convexity is preserved by Intersection

# Simplex Method

## Dictionary

TODO

## Basic and Non-Basic variables

Non-Basic variables are on the RHS, and Basic Variables are on the LHS Reason:
For a dictionary, basic variables and their values represent a basic feasible
solution, hence the LHS variables are called basic. Entering & Leaving variables

Entering & Leaving refers to entering & leaving the basic feasible solution
Hence entering variable is non-basic to basic, and leaving variable is basic to
non-basic.

## Minimal Ratio Test

TODO

## Geometric meaning

Simplex method takes advantage that the feasible region is convex (no local
maximum), and greedily chooses the direction of steepest ascent (largest
coefficient as entering variable), while using minimum ratio test to ensure that
it doesn't go out of feasible region.

Entering variable represents the direction of ascent, leaving variable
represents the hyperplane to stop at. (with minimum ratio test makes sure it
stops as next vertex (instead of out of bound). The minimum ratio is the step
size (of ascent).

A dictionary represents a vertex. But more specifically, a dictionary for an
$\mathbb{R}^n$ Linear Program represents $n$ active hyperplanes (such that the
intersection of hyperplanes form a vertex). This is the cause of degeneracy (for
$n + k$ hyperplanes, we can choose any n hyperplanes to represent the vertex,
resulting in $\binom{n + k}{n}$).

For each pivot operation, we remove an active hyperplane and replace it with
another with gaussian elimination.

## Tie in leaving variable

A tie in leaving variable indicates that there are more than 1 hyperplanes to
stop at (during a pivot operation.)

Therefore, the next dictionary will be degenerate. (as more than $n$ hyperplanes
will intersect at next point.

## Infeasible dictionary

An infeasible dictionary is a dictionary for which the current basic solution is
partly (or all) negative).

## Anstee’s rule:

Choose entering variable with largest positive coefficient in objective function
Choose leaving variable with smallest positive ratio for entering variable
Basically we want to maximize that variable without potentially making other
basic variables negative When tie, choose the leaving variable with lowest
subscript This avoids cycling Note: the first 2 are standard simplex rule, the
3rd rule is added to deal with degenerative dictionary (simplex run in a cycle).

## Non-unique optimal solutions:

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

## Dictionary as combination

- A dictionary is a combination of $n$ intersecting hyperplanes
- A dictionary has $n$ nonbasic variables and $m$ basic variables, and their
  combination uniquely maps to a dictionary (aka cannot have two dict with same
  combination of nonbasic and basic variables yet different coefficients)

## Revised Simplex Method

### Motivation

Modern computer are both time efficient and space efficient at doing
matrix operations. Therefore, what if simplex algorithm can be represented with matrix and iterated with matrix operations. This
leads to the revised simplex algorithm.

Also, sometimes, say if we have entering variable, we only need the coefficients of entering variable and current basic solution to choose
the leaving variable via ratio test. In fact, a matrix approach allows
selective computation of coefficients, which is another motivation.

The writing will break Revised Simplex Algorithm as
different subproblems, then assemble them together.

### Subproblem 1: Represent pivoting with augmented matrix & matrix multiplication

Say we have the following LP problem:

$$
\zeta = 9x_1 + 7x_2 \\
10x_1 + 5x_2 \leq 50 \\
6x_1 + 6x_2 \leq 36 \\
4.5x_1 + 18x_2 \leq 81 \\
x_{1...2} \geq 0
$$

The following LP problem can be rewritten as:

$$
\zeta = 9x_1 + 7x_2 \\
10x_1 + 5x_2 + x_3 = 50 \\
6x_1 + 6x_2 + x_4 = 36 \\
4.5x_1 + 18x_2 + x_5 = 81 \\
x_{1...5} \geq 0
$$

If one wants to solve it with pivoting, one can examine its coefficient 
and immediately say that $x_{1}$ enters and $x_{3}$ leaves, and do it by
hand via Gaussian Elimination. However, as one may also know, Gaussian 
Elimination can be represented with row operations & augmented matrix.

> The details of augmented matrix and Gaussian Elimination will be omitted in the note (other than 1 example), however there's lots of written & video materials on it online.

For example, we can rewrite the constraints into:

$$
M = \begin{bmatrix}
x_1 & x_2 & x_3 & x_4 & x_5 & \vec{x_b'} \\ \hline
10 & 5 & 1 & 0 & 0 & 50 \\
6 & 6 & 0 & 1 & 0 & 36 \\
4.5 & 18 & 0 & 0 & 1 & 81
\end{bmatrix}
$$

$\vec{x_b'}$ is simply a shorthand notation for the vector containing basic feasible solution of the current dictionary. The objective row is missing, but we will get back to that later.

To compute the new dictionary, note if we do it by hand, we need to:

- First Row: Divide first row by 10
- Second Row: Add $-6/10$ of original first row and original second row
- Third row: Add $-4.5/10$ of original first row and original third row

To construct new 3 rows for constraints.

If one is familiar with Augmented Matrix, one may recall that the above
row operations can be represented with a matrix, namely:

$$
E =
\begin{bmatrix}
1/10 & 0 & 0 \\
-6/10 & 1 & 0 \\
-4.5/10 & 0 & 1
\end{bmatrix}
$$

Then, the new constraints after pivoting can be represented as:

$$
EM = \begin{bmatrix}
x_1 & x_2 & x_3 & x_4 & x_5 & \vec{x_b'} \\ \hline
1 & 0.5   & 0.1   & 0 & 0 & 5 \\
0 & 3     & -0.6  & 1 & 0 & 6 \\
0 & 15.75 & -0.45 & 0 & 1 & 58.5
\end{bmatrix}
$$

Writing it in dictionary form yields:

$$
\begin{align*}
x_1 + 0.5x_2 + 0.1x_3 &= 5 \\
3x_2 - 0.6x_3 + x_4 &= 6 \\
15.75x_2 - 0.45x_3 + x_5 &= 58.5
\end{align*}
$$

The above is exactly the same that one would get if one performs
pivoting by hand, with $x_1$ entering and $x_3$ leaving. You can always perform pivoting by hand to confirm, if you have doubt.

> Summary: Dictionary can be represented with augmented matrix & pivoting can be represented by multiplying the augmented matrix with
a matrix that resembles row operations (also called [elementary matrix](https://en.wikipedia.org/wiki/Elementary_matrix))

### Subproblem 2: Going from one dictionary to any other dictionary, given the partition of basic & nonbasic variables

Say we have exact same problem from before:

$$
\zeta = 9x_1 + 7x_2 \\
10x_1 + 5x_2 + x_3 = 50 \\
6x_1 + 6x_2 + x_4 = 36 \\
4.5x_1 + 18x_2 + x_5 = 81 \\
x_{1...5} \geq 0
$$

And you are asked: given the above starting dictionary, give the constraints of a new dictionary with $\vec{x_B} = (x_1,x_4,x_5)^T, \vec{x_N} = (x_2,x_3)^T$. (The above is just a fancy way of saying that the new dictionary has basic variable $x_1,x_4,x_5$, nonbasic $x_2,x_3$)

There are multiple ways to solve this. But as part of Revised Simplex Algorithm, we do it the matrix way.

> One may recall that $x_1$ entering and $x_3$ exit works, but as we will show later, there exists a way that can be generalized (such that it applies for dictionaries that are not neighbor of starting dictionary)

Call the augmented matrix denoting the new dictionary as $M_{new}$, with
the info given, one can deduce that:

$$
M_{new} = \begin{bmatrix}
x_1 & x_2 & x_3 & x_4 & x_5 & \vec{x_b'} \\ \hline
1 &    &    & 0 & 0 &  \\
0 &      &   & 1 & 0 &  \\
0 &  &  & 0 & 1 & 
\end{bmatrix}
$$

We also know that, we can pivot from $M$ to reach $M_{new}$, therefore we examine the same 3 columns from $M$

$$
M = \begin{bmatrix}
x_1 & x_2 & x_3 & x_4 & x_5 & \vec{x_b'} \\ \hline
10 &  &  & 0 & 0 &  \\
6 &  &  & 1 & 0 &  \\
4.5 &  &  & 0 & 1 &
\end{bmatrix}
$$

We can extract the relevant parts. The 3 columns in $M_new$ forms an identity matrix, and the 3 columns in $M$ forms a square matrix. Let's call the first $I$ matrix and the second matrix $B$.

Hence, a unknown matrix $E$ exists (that represents row operations to move from initial dictionary to the new dictionary), such that:

$$
M_{new} = EM
$$

And, by only looking at the 3 columns:

$$
I = EB \\
E = B^{-1} =
\begin{bmatrix}
10 & 0 & 0 \\
6 & 1 & 0 \\
4.5 & 0 & 1
\end{bmatrix}^{-1} \\
M_{new} = EM = \begin{bmatrix}
x_1 & x_2 & x_3 & x_4 & x_5 & \vec{x_b'} \\ \hline
1 & 0.5   & 0.1   & 0 & 0 & 5 \\
0 & 3     & -0.6  & 1 & 0 & 6 \\
0 & 15.75 & -0.45 & 0 & 1 & 58.5
\end{bmatrix}
$$

Therefore, we can go from initial to another dictionary, given the partition of basic & nonbasic variables of the new dictionary. We simply need to:

- Construct $B$ with column vectors of basic variables of new dictionary
- Denote initial dictionary augmented matrix as $M$, compute $B^{-1}M$

> One may question that whether $B$ is always invertible. Short answer is yes. As row operations, and correspondingly, elementary matrices representing row operations are invertible. We know what we can always get from one dictionary to any other dictionary via pivoting, hence $E$ resembling these row operations exist and is invertible. Therefore $B = E^{-1}$ exists and is invertible. 

And, the technique applies even if we are not moving to neighbors of starting dictionary, but rather can be used to move to any vertices, which is a generalization of approach mentioned in Subproblem 1.

### Subproblem 3: going from one dictionary to any other dictionary, and gets new objective function

Again, we have same LP problem from before:

$$
\zeta = 9x_1 + 7x_2 \\
10x_1 + 5x_2 + x_3 = 50 \\
6x_1 + 6x_2 + x_4 = 36 \\
4.5x_1 + 18x_2 + x_5 = 81 \\
x_{1...5} \geq 0
$$

And you are asked: given the above starting dictionary, give the constraints & *objective function* of a new dictionary with $\vec{x_B} = (x_1,x_4,x_5)^T, \vec{x_N} = (x_2,x_3)^T$.

It may seem like an intimidating problem, but we merely need to generalize result from Subproblem 1 & 2 for a bit, to get the new objective function.

Back in Subproblem 1 & 2, the matrix $M_{new}$ corresponding to the
new dictionary is:

$$
M_{new} = \begin{bmatrix}
x_1 & x_2 & x_3 & x_4 & x_5 & \vec{x_b'} \\ \hline
1 & 0.5   & 0.1   & 0 & 0 & 5 \\
0 & 3     & -0.6  & 1 & 0 & 6 \\
0 & 15.75 & -0.45 & 0 & 1 & 58.5
\end{bmatrix}
$$

If we partition $M$ into two parts $B_{new}$ and $N_{new}$ (a matrix consist of column vectors of non-basic variables), the above dictionary can be represented as:

$$
\begin{align*}
B^{-1}\vec{b} &= B_{new}\vec{x_{B}} + N_{new}\vec{x_{N}} \\
&= \vec{x_B} + B^{-1}N\vec{x_{N}} \\
\vec{x_B} &= B^{-1}\vec{b} - B^{-1}N\vec{x_{N}} 
\end{align*}
$$

The above property will turned out to be a useful substitution. And we are ready to derive an expression for the new objective function.

If we partition $c$ such that initial objective function coefficient for current basic variables $\vec{x_{B}}$ is denoted as $c_{B}$, and objective function coefficients for current non-basic variables $\vec{x_{N}}$ is denotes as $c_{N}$, then the objective function $\zeta$ for new
dictionary can be written as:

$$
\begin{align*}
  \zeta &= c^T \vec{x} \quad \text{x is new dictionary's full solution} \\
  &= c_{B}^T\vec{x_{B}} + c_{N}^T \vec{x_{n}} \\
  &= c_{B}^T(B^{-1}\vec{b} - B^{-1}N\vec{x_{N}}) + c_{N}^T \vec{x_{n}} \\
  &= c_{B}^TB^{-1}\vec{b} - (c_{B}^TB^{-1}N\vec{x_{N}} - c_{N}^T) \vec{x_{n}} 
\end{align*}
$$

The above derivations may look intimidation & doesn't make sense. But it is, basically we know $\zeta$ would contain $\vec{x_{N}}$ only, but $\zeta = c^T \vec{x}$ expands into both $\vec{x_{B}}$ and $\vec{x_{N}}$, hence we construct & use a substitution to get rid of $\vec{x_{B}}$.

### What is Revised Simplex Algorithm

For revised simplex algorithm, we basically:

- Start at initial dictionary
  - Sets $B$, $N$, $\vec{x_{B}}$, $\vec{x_{N}}$
- While not at optimal point (when $-(c_{B}^TB^{-1}N\vec{x_{N}} - c_{N}^T)$ contains positive term)
  - Determines entering variable $x_{i}$ by computing parts of current dictionary $(c_{B}^TB^{-1}N\vec{x_{N}} - c_{N}^T)$
  - Determine leaving variable by:
    - Compute parts of leaving variable coefficients $\vec{P_{i}'} = B^{-1}P_{i}$, for which $P_{i}'$ is the entering variable coefficients in constraints of new dictionary, and $\vec{P_{i}}$ is the entering variable coefficients in constraints of initial dictionary.

    - Compute the slack value of current dictionary as $B^{-1}b$
    - Given $B^{-1}b$ and $\vec{P_{i}'}$, use minimum ratio test to determine leaving variable.

  - Sets $B$, $N$, $\vec{x_{B}}$, $\vec{x_{N}}$ with new choice of entering & leaving variable.

- Record basic optimal solution as $B^{-1}b$

The above may look confusing at first, but it is basically, instead of tracking the entire dictionary, when we need values from new dictionary during simplex iterations, we use techniques mentioned in the 3 subproblems to compute these values from the initial dictionary.

# Half Spaces & Hyperplanes

## Half Spaces:

A half space is quite literally one side of a hyperplane that cuts
$\mathbb{R}^n$ in half. It is characterized by:

$$\{x \in \mathbb{R}^n: A^T x \leq B, A,B \in \mathbb{R}^n\}$$

Or it can be a open set, for which:

$$\{x \in \mathbb{R}^n: A^T x < B, A,B \in \mathbb{R}^n\}$$

Note: a half space is convex.

## Hyperplanes:

$$\{x \in \mathbb{R}^n: A^T x = B, A,B \in \mathbb{R}^n\}$$

Note: a hyperplane is also convex.

## Connection to LP

- Each LP constraint is a half space.
- LP feasible region are intersection of half spaces (which is a polytope).
- By convex set property, LP feasible region is convex
  - Implies that there will not be local minimum
  - Enables simplex method's greedy strategy (of moving to next vertex with
    higher objective function value)

# Duality

Primal:

Maximize $c^{T}x$, when:

$$
Ax \leq b \\
x \geq 0
$$

Dual:

Minimize $b^{T}y$, when:

$$
A^T{y} \geq c \\
y \geq 0
$$

## Noteworthy facts

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
  - Reason: by weak duality, if primal is unbounded, then primal would be step
    out of duality gap.
  - Note: However, if one is infeasible, the other does not necessarily have to
    be unbounded (it can be infeasible too)
- If $x_{0}$ is primal feasible, and $y_{0}$ is dual feasible, and
  $c^{T}x = b^{T}y$, then:
  - $x$ is primal optimal
  - $y$ is dual optimal

### Proof:

Denote $a,b$ as max of primal & min of dual respectively, then:

$$
c^{T}x \leq a \leq b \leq b^{T}y
$$

The above is true by weak duality. By squeeze theorem, we let
$x,y = x_{0}, y_{0}$, then:

$$
c^{T}x_{0} = a = b = b^{T}y_{0}
$$

As desired.

## Weak Duality Theorem

The objective function of a primal is less than or equal to the objective
function of the dual (for any feasible solutions of the two).

Aka max of primal <= min of dual

In fact the prof claims that it is always true for any duality in optimization
(beyond LP).

### Proof (Summation):

Note $A^Ty \geq c$ (dual constraint), and $Ax \leq b$, then:

Then

$$
\sum_{j = 1}^{n} c_{j} x_{j} \leq \sum_{j = 1}^{n} (\sum_{i = 1}^{m} a_{ij} y_{i}) x_{j} = \sum_{i = 1}^{m} (\sum_{j = 1}^{n} a_{ij} x_{j}) y_{i} \leq  \sum_{i = 1}^{n} b_{i} y_{i}
$$

### Proof (Linear algebra)

$$
c^Tx \leq (A^Ty)^T = y^T Ax \leq y^Tb = b^Ty
$$

## Strong Duality theorem

If primal, dual has optimal solution $x^{*}, y^*$ respectively, then:

$$
c^Tx^* = b^Ty^*
$$

### Follow-up:

We can read a solution of the dual problem, directly from final dictionary of
primal problem. We can write objective function of a final primal dictionary as:

$$
\zeta = \zeta^* + \sum_{i = 1}^{m + n}c^*_k x_{k}
$$

For which:

- $\zeta^*$ is the optimal value of primal objective function.
- $c^*$ are objective function coefficients for primal final dictionary.
- $m, n$ are number of nonbasic and basic variables.

We can then read a dual optimal solution from the primal objective function as
follows:

$$y_i^* = -c_{m + i}^*$$

(Which in other words, is the coefficient of all slack variables, with sign
flipped).

### Remainder

An optimal dictionary is not necessary final (an optimal dictionary can be
degenerate with positive coefficients in objective function). And, the above
fact applies to final dictionary only.

### Application

\# of iterations for simplex algorithm is proportional to \# of rows in
dictionary and relatively insensitive to the \# of variables.

Hence, when there's more constraints (rows) than decision variables, solving
dual problem is faster.

### Table of states

| Primal/Dual | Optimal   | Unbounded | Infeasible |
| ----------- | --------- | --------- | ---------- |
| Optimal     | P (by SD) | NP        | NP         |
| Unbounded   | NP        | NP        | P (by WD)  |
| Infeasible  | NP        | P         | P          |

- P is possible
- NP is not possible
- SD means by strong duality
- WD means by weak duality

Reason for infeasible/infeasible case:

We can construct the example as two parallel lines in $\mathbb{R}^2$ (2
constraint, 2 decision variables), for which the the constraint half-space of
the two does not intersect. Then the dual problem will have same
non-intersecting constraint.

## Theorem of the alternative

Let $A$ and $\vec{b}$ given:

Then, exactly one of the following is true (not both):

- There exists an $\vec{x}$ such that $x \geq 0$ and $Ax \leq \vec{b}$
- There exists a $\vec{y}$ such that $\vec{y} \geq 0$, $A^{T}\vec{y} \geq 0$,
  and $\vec{b} \cdot \vec{y}\leq 0$

Proof is literally left as exercise...

## Certificate of optimally

Say if one hand-calculated an optimal solution and want to check the solution.
Then:

- Check feasibility of primal solution
  - Going back to original inequality and see if the solution is in range
- Get the supposed dual optimal solution
  - Check feasibility again
  - Check if the objective function value is the same

### Reason for correctness

Assume we have an primal infeasible solution, then the feasibility check will
catch it.

Assume we have a primal feasible solution but dual infeasible solution, the dual
feasibility check will catch it. (It is possible for this to happen with
algebraic mistakes in pivoting operation, as usually the negative transpose
property should be maintained (dual should stay feasible)).

Assume we have an primal feasible, dual feasible but non-optimal solution, then
strong duality will catch it (the objective function will have the same value).

Hence, for all cases, the incorrect solution is caught.

## Complementary Slackness

Let $x^{*}$ be primal feasible solution (vector with size $n$) Let $y^{*}$ be
dual feasible solution (vector with size $m$)

Then, $x^{*}$, $y^{*}$ optimal for primal & dual is equivalent (two sided if)
to:

For all $i$:

$$
y_{i}^{*} (b_{i} - \sum_{j = 1}^{n}a_{ij}x_j^*) = 0
$$

_And_, for all $j$

$$
x_{j}^{*} (\sum_{i = 1}^{m}a_{ij}y_j^* - c_{j}) = 0
$$

Note the two brackets summations are respective slack variables of the two
problems.

Hence it really means the dot product of dual solution and primal slack variable
equals 0 and the dot product of primal solution and dual slack variable equals
0, hence the name "complimentary slackness")

## Application

We can use complimentary slackness to find dual LP optimal solution via given
primal LP itself & primal LP solution.

Note, when the primal is not degenerate, we can construct system of equations in
terms of dual optimal solution terms, to acquire dual optimum from primal
optimum.

The powerful part is that we don't need a dictionary, but rather the optimal
solution itself is sufficient to apply complimentary slackness

### Proof

Recall the inequality used in weak duality proof

$$
c \leq A^T y \\
c^Tx \leq (A^Ty)^Tx = y^TAx \leq y^Tb = b^Ty
$$

When $c = A^Ty$, the first inequality becomes equality , note $A^Ty - c$ is the
vector containing all slack variables in dual problem.

Hence, let $x_{j}$ denotes the $j$ th element in $x$, and $(A^Ty - c)_{j}$
denotes the $j$ th element in $(A^Ty - c)_{j}$, then the first inequality
becomes inequality when either are true:

- $x_{j} = 0$
- $(A^Ty - c)_{j} = 0$

Repeat the same argument to the 2nd inequality derives the remaining part of
complimentary slackness, as desired.

## Theorem on small change of $\vec{b}$

Say we have

$$
\text{max } c \cdot x \\
Ax \leq b \\
x \geq 0
$$

Assume we perturb $b$ (not for too much) by $\vec{t}$, then the new optimal
objective $\zeta^{**}$ vs before is $\zeta^*$ is:

$$
\zeta^{**} - \zeta^* = \vec{t} \cdot \vec{y^*}
$$

Which looks like... directional derivative, with $y^*$ being gradient of
objective function.

### Theorem

For

$$
\text{max } c \cdot x \\
Ax \leq b \\
x \geq 0
$$

Assume:

- $x^*$ is primal optimal
- $y^*$ is dual optimal solution.
- $y^*$ is unique (aka) $x^*$ is non degenerate)

Then, there exists a $\epsilon > 0$, such that for all $|\vec{t}| < \epsilon$,
the new LP problem with $Ax \leq b + t$ preserves same optimal solution $x^*$.

### Application

Knowing the dual optimum, we can compute $\zeta^{**}$ given small change to $b$.

## Geometric Interp. of dual problem

For each row of constraint $\vec{a} \cdot \vec{x} \leq b_{i}$, $\vec{a}$ is
actually the normal vector of the constraint hyperplane

The dual problem constraints can be written as:

$$
\vec{c} \leq \sum_{i=1}^{n} y_{i}\vec{a_{i}}
$$

For which:

- $\vec{y}$ is a dual feasible solution.
- $\vec{a_{i}}$ are the normal vectors for primal constraints.

### Equality representation

$$\vec{c} = \sum_{i=1}^{n} y_{i}^*\vec{a_{i}} + \sum_{j = 1}^{m}v_{j}(-e_{j})$$

For which:

- $e_{j}$ are canonical basis vectors.
- $\vec{y^*}$ the dual optimal solution.
- $\vec{v}$ are dual slack variables

### Algebraic Point of view (for above formula)

Refer to Vanderbei p53-54.

We basically want to establish a upper bound of the primal problem, and we want
to ensure:

- The upper bound objective's coefficient is strictly equal or greater than the
  primal objective
  - This forms the constraints of the dual problem
- The upper bound is as small as possible
  - This forms the objective function of the dual problem.

### Physics Point of view (current & boat)

$\vec{c}$ represents direction of current. $a_{i}, -e_{k}$ represent direction
of normal force of walls. A boat getting carried by the current will eventually
end at the primal optimal point, and at that point:

$F_{net} = 0 \rightarrow F_{c} + F_{n} = 0$

For the sake of simplicity, say $m = 1$, then at the same point:

$F_{c} = c \\
F_{n} = \sum y_{i} (-a_{i}) + \sum v_{j} (e_{j})$

For which is equivalent to:

$$\vec{c} = \sum_{i=1}^{n} y_{i}^*\vec{a_{i}} + \sum_{j = 1}^{m}v_{j}(-e_{j})$$

The significance being that, since $\vec{a_{i}}, -e_{j}$ are all normal vectors
for the primal constraints boundaries, solving a dual problem is finding _linear
combination_ coefficients such that these normal vectors sums up to $c$.

### Significance

Since $\vec{a_{i}}, -e_{j}$ are all normal vectors for the primal constraints
boundaries, solving a dual problem is finding _linear combination_ coefficients
such that these normal vectors sums up to $c$.

Such linear combination coefficients exists at every vertex in the primal
feasible region, and the role of dual objective function is ensuring we are
finding coefficients for the right vertex (the primal optimal vertex).


### Interp. Complementary Slackness as linear combination

$$\vec{c} = \sum_{i=1}^{n} y_{i}^*\vec{a_{i}} + \sum_{j = 1}^{m}v_{j}(-e_{j})$$

Complementary Slackness for $\vec{x^*}$ shows which hyperplanes 
are binding at final primal dictionary. Therefore, non-binding hyperplanes should have weight $0$, which means $y_{i} = 0$.

## Economical view of dual problem

For a resource allocation problem, the primal is maximizing the profit
given the resource constraints. The dual objective would be the total "shadow/fair price" of primal resource usage.

Say if company A is producing goods under limited resource, the primal would be how company A plans what goods to produce, and dual would be how a different company B would buy resources from company A such that
company A agrees & company B pay as little as possible.

### Interp. of complementary slackness

If a resource $x_{m+i}$ is not fully utilized by company $A$, then company $A$ is willing to given them away for arbitrary low price
(aka 0). Since $y_{i}$ resembles shadow price of $x_{m+i}$, it becomes
$0$. 

### Interp. of small change of b

basically it talks about the profit change of company A with extra resources.

# Degeneracy

A dictionary is _degenerate_ if one of the row's constant term is 0.

### Example:

$$
\zeta = 5 + x_{3} - x_{1} \\
x_{2} = 5 + 2x_{3} - 3x_{1} \\
x_{4} = 7 - 4x_{1} \\
x_{5} = x_{1}
$$

Such dictionary may _produce difficulty_ for simplex algorithm, or it might not.
The difficulty can be:

- Slowing down the algorithm
- In worst case causes cycle (not for Anstee's rule, but for many other pivoting
  rule)

An other interp. for degenerative dictionary is that, in the feasible region of
an LP with dimension n, there are more than n hyperplanes intersecting at a
single vertex (Redundant constraints).

## Lemma

If simplex method never terminates, it must cycles.

### Proof:

Say we have $n, m$ basic & nonbasic variables, then the total number of
dictionaries are:

$$
\binom{n + m}{n}
$$

Which is a finite number. And, a non-terminating procedure will eventually
encounter one of the dictionaries that it already travelled, causing cycle.

## Degeneracy & uniqueness of dual optimal solution

If primal optimal $x^*$ is:

- Non-degenerate

Then the dual optimal solution $\vec{y^*}$ is unique.

### Proof

Non-degenerate indicates exactly $n$ linearly independent hyperplanes intersect
at $x^*$. Therefore, they have linearly independent normal vectors. Denote these
vectors as $N_{1...n}$.

Hence $c = [N_{1}, N_{2},...N_{n}] \vec{y^*}$, for which $y$ is dual optimal
solution (containing both basic & nonbasic). The equality is due to the fact
that $c$ is linear combination of primal constraints normal vectors.

Since $N_{1...n}$ independent, $[N_{1}, N_{2},...N_{n}]$ is therefore
invertible, therefore $\vec{y^*} = [N_{1}, N_{2},...N_{n}]^{-1} c$ is unique.

# Misc

## Penalty Method

Say if we want to max $f(x)$ given $x \in C$ for some set $C$. Then
to make sure the $x$ found is feasible, we can maximize $f(x) - p(x)$ instead, with $p(x) = 0$ when $x$ is feasible, and $p(x) = -\infty$
when $x$ is not feasible.

In practice, $p(x)$ is softened to be continuous, and the above piecewise
$p(x)$ is never used. (As most optimization algorithms require
the objective function to be "nice").

Some necessary (but not sufficient) conditions for $p(x)$:

$p(x) \geq 0, x \in C$ and $p(x) \leq 0, x \notin C$.

And $p(x)$ becomes more negative the farther away $x$ is from $c$.

### Theorem

Say for a $p(x)$ satisfying the above 3 conditions. Then we can always
find $\lambda$ such that $\max f(x) = \max f(x) + \lambda p(x)$.
(Note $x$ is not necessarily the same). In fact $\max_{x} f(x) = \min_{\lambda} (\max_{x} f(x) + \lambda p(x))$.

Above $\lambda$ is called lagrange multiplier (note it is similar but 
different than lagrange multiplier for equality constraint (aka the version taught in calculus classes), $C$ resembles
an inequality. e.g. in $\mathbb{R}^2$ $c$ would resemble an area, instead
of a curve.).

### Lagrange multiplier & Linear Programming 

Say we have:

$$\pi(x,y) = c^Tx + y^T(b - Ax)$$

The above is the same formula for weak duality proof.

$$\pi(x,y) = c^Tx + y^Tb - (A^Ty)^Tx \\
= y^Tb + x^T(c - A^Ty)$$

So primal objective value + product of dual decision and dual slack variables
is equivalent to the dual objective function + product of primal and primal slack variables.

Then, note:

$$\min_{y\geq 0} \max_{x \geq 0} \pi(x,y) = \min_{y\geq 0, A^Ty \geq c} b^Ty$$

# Quizzes

## Nov 3 Quiz

Consider the primal LP:

$$
\text{max } c \cdot x \\
Ax \leq b \\
x \geq 0
$$

Which of the following is true:

- If c changes, $x^*$ much also change.
- If b changes, the optimal dual solution $y^*$ must change
- There are examples of changing $b$ changes the feasible region of the dual
  problem

### Answer

None is true, for 1), simply scale c. Or geometrically, we can change direction
of solution level set (hyperplane) as long as we don't change too much (
maintains only one intersection at same vertex )

For 2, it is the dual version of 1), hence should also be false

For 3, changing objective function of dual does not change the feasible region
of the dual.

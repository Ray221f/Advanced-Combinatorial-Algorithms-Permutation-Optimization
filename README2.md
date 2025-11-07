# Combinatorial Algorithms (Spring 2025)
## Assignment 2

**Authors (in arbitrary order):**  
- Hao Guo 
- Zirui Fang 

**Date:** June 2025  
**Course:** Combinatorial Algorithms  
**Instructor:** Prof. Pablo Ezequiel Terlisky  
---

## 📘 Overview

This repository contains our solutions for **Assignment 2 (v1.4)** of the *Combinatorial Algorithms* course.  
The assignment includes **two main problems** involving **shortest path algorithms** and **vertex cover problems**.  
Each problem has **two parts**, leading to four Python implementations in total.

| Exercise | File | Description |
|-----------|------|-------------|
| 1(a) | `assignment_1_1.py` | Shortest *walk* from `s` to `t` using **exactly one special edge** |
| 1(b) | `assignment_1_2.py` | Shortest *path* from `s` to `t` using **at most two special edges** |
| 2(a) | `assignment_2_1.py` | **Exact** minimum vertex cover using **backtracking + pruning** |
| 2(b) | `assignment_2_2.py` | **2-approximation** vertex cover using a **greedy linear algorithm** |

All programs read from **standard input**, print to **standard output**, and are fully self-contained in Python 3.

---

## 🧩 Exercise 1 — Shortest Paths with Special Edges

### Problem Description
Given a **directed weighted graph** \( G = (V, E) \) with some edges marked as *special*,  
find the shortest walk or path from a source vertex \( s \) to a target vertex \( t \)  
subject to different constraints on the number of special edges used.

Each edge is defined as: u v w p
where:
- \( u, v \): vertices (0 ≤ u, v < n)
- \( w \): nonnegative integer weight
- \( p = 1 \) if the edge is *special*, otherwise \( p = 0 \)

The first line of input contains: n m s t


---

### 1(a) — Shortest Walk Using **Exactly One Special Edge**
📄 File: `assignment_1_1.py`

#### Algorithm
1. **Ignore all special edges** and run Dijkstra’s algorithm from:
   - \( s \) to every vertex \( u \)
   - \( t \) to every vertex \( v \) (using the reversed graph)
2. For each edge \( (u, v) \) marked as *special*:
   - Compute total distance \( d(s, u) + w(u,v) + d(v, t) \)
   - Track the minimal such distance and reconstruct the corresponding walk.
3. If no feasible combination exists, print `infeasible`.

#### Output
If feasible: (distance, [path])
Otherwise: infeasible

#### Example (from assignment)
Input:
6 7 0 5
0 1 2 0
0 3 6 0
1 2 3 0
2 5 4 0
3 2 5 0
3 4 1 1
4 5 2 1
Output: infeasible

Input:
6 9 0 5
0 1 6 0
0 3 4 0
1 2 4 0
1 3 3 1
1 4 5 0
2 5 3 0
3 4 3 0
4 2 2 1
4 5 6 0
Output:
(12,[0,3,4,2,5])

#### Complexity
\[
O(\min\{|V|^2, |E| \log |V|\})
\]
— achieved by dynamically selecting between **Dijkstra with a vector** (dense graphs) or **priority queue** (sparse graphs).

---

### 1(b) — Shortest Path Using **At Most Two Special Edges**
📄 File: `assignment_1_2.py`

#### Algorithm
Implements a **layered-graph construction**:
- Create 3 layers of the graph (representing 0, 1, and 2 special edges used).
- Normal edges connect vertices **within the same layer**.
- Special edges connect vertices **across adjacent layers**.
- Run Dijkstra’s algorithm once from \( s \) in the layered graph.
- Among targets \( t_0, t_1, t_2 \), select:
  - the one with smallest distance,
  - and if tied, the one with fewer special edges (smaller layer index).

#### Example (from assignment)
Input (Figure 1a):
6 7 0 5
0 1 2 0
0 3 6 0
1 2 3 0
2 5 4 0
3 2 5 0
3 4 1 1
4 5 2 1
Output: (9,[0,1,2,5])

Input (Figure 1b):
6 9 0 5
0 1 6 0
0 3 4 0
1 2 4 0
1 3 3 1
1 4 5 0
2 5 3 0
3 4 3 0
4 2 2 1
4 5 6 0
Output: (12,[0,3,4,2,5])

#### Complexity
Same as Exercise 1(a):  
\[
O(\min\{|V|^2, |E| \log |V|\})
\]

---

## 🔺 Exercise 2 — Vertex Cover Problem

### Problem Description
Given an undirected, unweighted graph \( G = (V, E) \),  
find a **subset of vertices \( VC \subseteq V \)** such that every edge in \( E \)  
is incident to at least one vertex in \( VC \).

The input format:
n m
u1 v1
u2 v2
...
um vm

---

### 2(a) — Exact Minimum Vertex Cover (Backtracking)
📄 File: `assignment_2_1.py`

#### Algorithm
A **recursive backtracking** algorithm that explores inclusion/exclusion of each vertex,  
with **one feasibility prune** and **one optimality prune**:

- **Feasibility Prune:**  
  If excluding vertex `i` leaves an uncovered edge `(i, j)` where `j < i` and `x[j] == 0`,  
  then `i` must be included.

- **Optimality Prune:**  
  If the current number of selected vertices exceeds the best known minimum,  
  stop exploring that branch.

#### Output
(size, [selection_vector])

Example (Figure 2a):
4 4
0 1
0 3
1 2
1 3
Output: (2,[0,1,0,1])

Example (Figure 2b):
7 8
0 1
1 2
2 3
2 4
3 4
3 5
3 6
4 5
Output: (3,[0,1,0,1,1,0,0])

#### Complexity
Exponential in worst case, but significantly pruned by the two strategies.

---

### 2(b) — 2-Approximation Vertex Cover
📄 File: `assignment_2_2.py`

#### Algorithm
A simple greedy algorithm (Algorithm 1 from the assignment):
1. While edges remain:
   - Pick an arbitrary edge `(u, v)`.
   - Add both `u` and `v` to the vertex cover.
   - Remove all edges incident to `u` or `v`.
2. Return the resulting set.

#### Approximation Factor
\[
\text{Factor} = 2
\]
Every optimal edge cover must cover all edges; since at least one endpoint of each chosen edge must be in the optimal cover, we choose at most twice as many vertices.

#### Example
Input (Figure 2a):
4 4
0 1
0 3
1 2
1 3
Output: (2,[1,1,0,0])

Input (Figure 2b):
7 8
0 1
1 2
2 3
2 4
3 4
3 5
3 6
4 5
Output: (6,[1,1,1,1,1,1,0])

#### Complexity
\[
O(|V| + |E|)
\]
Efficient for large sparse graphs.

---

## ⚙️ Usage

### Run Exercise
```bash
python3 assignment_1_1.py
python3 assignment_1_2.py
python3 assignment_2_1.py
python3 assignment_2_2.py

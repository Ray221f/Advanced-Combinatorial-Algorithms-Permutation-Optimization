# Combinatorial Algorithms & Graph Theory Project

A comprehensive project implementing combinatorial algorithms and graph theory solutions, developed as part of computer science coursework.

## 📋 Project Overview

This repository contains sophisticated implementations of combinatorial algorithms spanning two major assignments, demonstrating mastery in:

- **Graph Theory Algorithms**
- **Combinatorial Optimization**
- **Permutation Ranking Systems**
- **Approximation Algorithms**
- **Backtracking with Pruning Techniques**

## 🎯 Assignment 1: Combinatorial Pattern Detection & Constrained Permutations

### Exercise 1: Induced Paw Subgraph Detection
**Problem**: Identify all induced paw subgraphs in undirected graphs
- **Input**: Graph with n vertices and m edges
- **Output**: All sets of 4 vertices forming induced paw subgraphs in lexicographic order
- **Algorithm**: Optimized subgraph enumeration with pruning strategies
- **Complexity**: Efficient detection with comprehensive edge case handling

### Exercise 2: Constrained Permutation Ranking
**Problem**: Find valid permutations satisfying precedence constraints using Trotter-Johnson ordering
- **Input**: Size n and m precedence constraints
- **Output**: Rank of valid permutation or infeasibility message
- **Algorithm**: Trotter-Johnson unranking with constraint satisfaction
- **Applications**: Scheduling, topological ordering, constraint satisfaction

## 🎯 Assignment 2: Graph Algorithms & Approximation Methods

### Exercise 1: Special Edge Path Finding
**Part A**: Shortest walk using exactly one special edge
- **Algorithm**: Modified Dijkstra with special edge tracking
- **Complexity**: O(min{|V|², |E| lg |V|})
- **Features**: Handles walks (repeated vertices) when necessary

**Part B**: Shortest path using at most two special edges
- **Algorithm**: Multi-layer Dijkstra with edge type counting
- **Optimization**: Preference for fewer special edges when path lengths are equal

### Exercise 2: Vertex Cover Algorithms
**Part A**: Exact Minimum Vertex Cover
- **Algorithm**: Backtracking with feasibility and optimality pruning
- **Pruning Strategies**: 
  - Feasibility: Early termination when uncovered edges exist
  - Optimality: Branch-and-bound with current best solution

**Part B**: Approximation Algorithm Implementation
- **Algorithm**: Greedy edge selection approach
- **Approximation Factor**: 2-approximation guarantee
- **Complexity**: O(|V| + |E|) optimal implementation
- **Analysis**: Comprehensive behavior analysis across graph types

## 🚀 Technical Features

### Algorithmic Innovations
- **Custom Graph Processing**: Pure Python implementation without external graph libraries
- **Optimized Pruning**: Intelligent backtracking with multiple pruning strategies
- **Theoretical Guarantees**: Proven correctness and complexity bounds
- **Comprehensive Testing**: Extensive test suites covering edge cases and performance boundaries

### Performance Characteristics
- Handles graphs up to 50+ vertices efficiently
- Processes complex constraint sets in polynomial time
- Memory-efficient data structures for large combinatorial spaces
- Validated against known mathematical results and edge cases

## 🛠 Implementation Details

### Technology Stack
- **Language**: Python 3.x
- **Key Packages**: math, heapq, sys (minimal dependencies)
- **Platform**: Unix-compatible systems
- **Testing**: Comprehensive custom test suites

### Key Algorithms Implemented
1. **Subgraph Isomorphism Detection**
2. **Trotter-Johnson Permutation Ordering**
3. **Modified Dijkstra with Edge Constraints**
4. **Backtracking with Pruning**
5. **Vertex Cover Approximation**
6. **Lexicographic Generation**

## 📊 Academic Context

This work demonstrates advanced understanding of:

### Theoretical Foundations
- Graph isomorphism and subgraph detection
- Permutation group theory and ranking
- Shortest path algorithms with constraints
- Approximation algorithm analysis
- NP-hard problem solving strategies

### Research Applications
- **Bioinformatics**: Network motif detection
- **Operations Research**: Scheduling with precedence constraints
- **Network Design**: Vertex cover in communication networks
- **Combinatorial Optimization**: Constraint satisfaction problems

## 👥 Research Team

**Primary Researchers (in arbitrary order)**:
- Zirui Fang
- Hao Guo

**Academic Supervision**: Combinatorial Algorithms Course, Spring 2025

## 📚 Theoretical Foundations

Based on established research in:
- Kreher & Stinson, "Combinatorial Algorithms: Generation, Enumeration, and Search"
- Cormen et al., "Introduction to Algorithms"

## 🎓 Learning Outcomes

This project demonstrates mastery in:
- Designing and analyzing algorithms
- Implementing theoretical computer science concepts
- Optimizing for both time and space complexity
- rigorous testing and validation methodologies
- Academic writing and technical documentation

## 📁 Repository Structure
├── induced_paw_detection.py # Induced paw detection
├── constrained_permutation_ranking.py # Constrained permutation ranking
├── constrained_shortest_path.py # Special edge path finding
├── layered_graph_shortest_path.py # Vertex cover exact algorithm
├── vertex_cover_backtracking.py # Additional implementations
├── vertex_cover_approximation.py # Vertex cover approximation
├── README1.md # Detailed documentation
├── README2.md # Usage instructions
└── test_cases/ # Comprehensive test suites


## 🔬 Research Significance

This work bridges theoretical computer science with practical implementation, providing:
- Efficient solutions to computationally challenging problems
- Insights into algorithm behavior across problem variants
- Educational resources for combinatorial algorithm study
- Foundation for further research in graph algorithms and optimization

---

*Developed as part of undergraduate studies in Computer Science, demonstrating excellence in algorithmic problem-solving.*

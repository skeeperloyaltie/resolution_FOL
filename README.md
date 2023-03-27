## Resolution FOL - using CNF
- In this assignment you will gain insight into resoluion by implementing a theroem power for a subset of first order logic (FOL)
- You are given a single file encoding a knowledge base (KB) in conjunctive normal form (CNF), for example the file will first list the predicates, variables, constants and functions used in the knowledge base. 
- - It will then list the clauses on each line with  whitespaces separating each literal. Negation will be indeicated by "!". For example, the classes may read: 
```!dog(X0) animal(x0)``` <br>
```dog(Kim1)```<br>
- which represents two clauses:
```[- dog(x0), animal(x0)]``` <br>
```[dog(Kim1)]``` <br>

- Which can be expressed in FOL as:
```(inverted A x - dog(X) V animal(x)) Inverted V dog(Kim1)```
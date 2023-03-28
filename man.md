1. !dog(x0) animal(x0)
2. !person(x6) animal(x6)
3. !partOf(x7,Kim)
4. person(SKF0(x1)) !dog(x1) !friendly(x1)
5. loves(SKF0(x2),x2) !dog(x2) !friendly(x2)
6. man(Mike)
7. !dog(x3) partOf(x3,SKF1(x3))
8. !dog(x4) tail(SKF1(x4))
9. !man(x5) person(x5)
10. dog(Kim)
11. friendly(Kim)
12. man(SK0)
13. angry(SK0)

Apply resolution to clauses 1 and 10, using the unification {x0/Kim}:
  animal(Kim)

Apply resolution to clauses 2 and 10, using the unification {x6/Kim}:
  animal(Kim)

Apply resolution to clauses 3 and 10:
  !partOf(Kim,Kim)

Apply resolution to clauses 4 and 10, using the unification {x1/Kim}:
  person(SKF0(Kim)) !dog(Kim) !friendly(Kim)

Apply resolution to clauses 5 and 10, using the unification {x2/Kim}:
  loves(SKF0(Kim),Kim) !dog(Kim) !friendly(Kim)

Apply resolution to clauses 6 and 12:
  man(Mike)

Apply resolution to clauses 7 and 10, using the unification {x3/Kim}:
  !dog(Kim) partOf(Kim,SKF1(Kim))

Apply resolution to clauses 8 and 10, using the unification {x4/Kim}:
  !tail(SKF1(Kim))

Apply resolution to clauses 9 and 2, using the unification {x5/Kim, x6/Kim}:
  !man(Kim) person(Kim)

Apply resolution to clauses 4 and 5:
  person(SKF0(x2)) !dog(x2) !friendly(x2)   loves(SKF0(x2),x2) !dog(x2) !friendly(x2)  -> empty clause

Therefore, the set is unsatisfiable.

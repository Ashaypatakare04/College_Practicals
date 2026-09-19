A = frozenset([1, 2, 3, 4, 5])
B = frozenset([4, 5, 6, 7, 8])

print("A =", A)
print("B =", B)

print("Length of A:", len(A))

print("3 in A:", 3 in A)
print("10 in A:", 10 in A)

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))

C = frozenset([1, 2, 3])
print("Subset:", C.issubset(A))
print("Superset:", A.issuperset(C))

D = frozenset([10, 20, 30])
print("Disjoint:", A.isdisjoint(D))

E = A.copy()
print("Copy:", E)

print("Maximum:", max(A))
print("Minimum:", min(A))
print("Sum:", sum(A))

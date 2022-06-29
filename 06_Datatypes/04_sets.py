# Sets: unordered, metablel, no dublicates

from typing import Set


emptyset = set()

myset = {1,2,3}
print(f"myset : {myset}")

myset2 = {1,2,3,3,3,3}
print(f"myset2 : {myset2}")

myset3 = set("Hallo")
print(f"myset3: {myset3}")

myset3.add("d")
print(f"myset3: {myset3}")

myset3.discard("k")
print(f"\nsafe removal of elements, nothing happen, if not in myset3: {myset3}")

myset3.discard("o")
print(f"remove o in myset3: {myset3}")

odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)
print(f"\nunion: {union}")

intersection = odds.intersection(primes)
print(f"intersections: {intersection}")

diff = odds.difference(primes)
print(f"diff: {diff}")

symmetric_difference = odds.symmetric_difference(primes)
print(f"symmetric_difference: {symmetric_difference}")


setA = {1,2,3}
setB = {2,3,4,5,6}

setA.update(setB)
print(f"\nsetA.update(setB): {setA}")


setA = {1,2,3}
setB = {2,3,4,5,6}

setA.intersection_update(setB)
print(f"setA.intersection_update(setB): {setA}")


setA = {1,2,3}
setB = {2,3,4,5,6}

setA.difference_update(setB)
print(f"setA.difference_update(setB): {setA}")


setA = {1,2,3}
setB = {2,3,4,5,6}

setA.symmetric_difference_update(setB)
print(f"setA.symmetric_difference_update(setB): {setA}")


subset_B = {4,5}

print(f"\nsubset_B.issubset(setB): {subset_B.issubset(setB)}")
print(f"subset_B.issuperset(setB) / child set: {subset_B.issuperset(setB)}")
print(f"setB.issuperset(subset_B) / parent set: {setB.issuperset(subset_B)}")

print(f"setB.isdisjoint(subset_B) / has no intersection: {setB.isdisjoint(subset_B)}")

fset = frozenset([1,2,3,4])
print(f"frozenset is immutable: {fset}")

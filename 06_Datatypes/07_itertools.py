#itertools: product, permutation, combination, accumulation, groupby, and infinitive iterators

from itertools import product, permutations, combinations, combinations_with_replacement

from pandas import value_counts


a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(f"The product of {a} and {b} is {list(prod)}")

c = [1, 2, 3]
perm_len = 3
perm = permutations(c, perm_len)

print(f"The permutations of {c} with len {perm_len} is {list(perm)}")


d = [1, 2, 3, 4]
comb_len = 2
comb = combinations(d, comb_len)

print(f"\nThe combinations of {d} with len {comb_len} is {list(comb)}")

comb = combinations_with_replacement(d, comb_len)

print(f"The combinations_with_replacement of {d} with len {comb_len} is {list(comb)}")


from itertools import accumulate
import operator

e = [1, 2, 3, 4]
acc = accumulate(e)
print(f"\nThe accumulate of {e} is {list(acc)}")


acc = accumulate(e, func=operator.mul)
print(f"The accumulate of {e}, func=operator.mul is {list(acc)}")

e = [1, 2, 5, 3, 4]
acc = accumulate(e, func=max)
print(f"The accumulate of {e}, func=max is {list(acc)}")


from itertools import groupby

def smaller_than_3(x):
    return x < 3

f = [1, 2, 3, 4]
group_obj=groupby(f, key=smaller_than_3)
print(f"\nThe groupby of {f},  key=smaller_than_3:")

for key, value in group_obj:
    print(key, list(value))


#---------------------------------------------
persons = [{"name": "Tim", "age": 25},
           {"name": "Anna", "age": 25},
           {"name": "Max", "age": 33},
           {"name": "Inna", "age": 33},
           {"name": "Ola", "age": 12}]

group_obj=groupby(persons, key=lambda x: x["age"])
print(f"\nThe groupby of {persons},  key=lambda x: x['age']")
for key, value in group_obj:
    print(key, list(value))

#--------------------------------------------
from itertools import count

print("\ncount starts at 10 and continues")
for i in count(10):
    print(i)
    if i == 12:
        break

#--------------------------------------------
from itertools import cycle

a = [1,2,3]
stop = 10
print(f"\ncycle throug {a}")
for i in cycle(a):
    if stop == 0:
        break
    stop = stop - 1
    print(i)
#--------------------------------------------

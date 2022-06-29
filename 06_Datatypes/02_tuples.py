# Cannot be changed after createion ->immutable
# ordered
# allows to dublicate elements

mytuple = ("Max","18")
print(f"tuple_item0: {mytuple[0]}, tuple_item1: {mytuple[1]}\n")

apple_tuple = ("a", "p", "p", "l", "e")
print(f"len: {len(apple_tuple)}\n")

print(f"count p: {apple_tuple.count('p')}")
print(f"count l: {apple_tuple.count('l')}")
print(f"count o: {apple_tuple.count('o')}")

print(f"index first p: {apple_tuple.index('p')}\n")

mylist = list(mytuple)
print(f"list conversion: {mylist}")

name, age = mytuple
print(f"Unpacking. name: {name}, age: {age}\n")

mytuple2 = tuple(i for i in range(0, 10))
print(f"mytuple2: {mytuple2}")

first, *mid, last = mytuple2
print(f"Unpacking mytuple2. first: {first}, last: {last}, mid: {mid}\n")


## Compare List vs Tuple

import sys

list3 = [0, 1, 2, "hello", True]
tuple3 = (0, 1, 2, "hello", True)

sys.getsizeof(list3)
print("Compare List vs Tuple\n")
print("Size:\n")
print(f"sys.getsizeof(list3) {sys.getsizeof(list3)} bytes")
print(f"sys.getsizeof(tuple3) {sys.getsizeof(tuple3)} bytes")

print("Iterating time:\n")
import timeit
tuple4 = tuple(i for i in range(1,7))
list4 = list(tuple4)

print(f"Tuple creation 1000000 times: timeit.timeit(stmt={str(tuple4)}, number=1000000) : {timeit.timeit(stmt=str(tuple4), number=1000000)}")
print(f"List creation 1000000 times: timeit.timeit(stmt={str(list4)}, number=1000000) : {timeit.timeit(stmt=str(list4), number=1000000)}")
# collections: Counter namedtuple, defaultdict, deque
from collections import Counter

a = "aaaabbbbbbccccccc"
my_counter = Counter(a)
print("\nCounter")
print(f"my_counter: {my_counter}")
print(f"my_counter.keys(): {my_counter.keys()}")
print(f"my_counter.values(): {my_counter.values()}")
print(f"my_counter.most_common(1): {my_counter.most_common(1)}")
print(f"my_counter.most_common(2): {my_counter.most_common(2)}")
print(f"list(my_counter.elements()): {list(my_counter.elements())}")


from collections import namedtuple

Point = namedtuple("Point", "x,y")
pt = Point(1, 4)
print("\nnamedtuple")
print(f"pt: {pt}")
print(f"pt.x: {pt.x}")
print(f"pt.y: {pt.y}")


from collections import defaultdict

def def_value():
    return 0

defdict = defaultdict(def_value) # defaultdict(int)
defdict["a"] = 2
defdict["b"] = 1
defdict["c"] = 6
print(f"\ndefdict: {defdict}")
print(f"no exception if value not exist defdict['t']: {defdict['t']}")


from collections import deque

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)

print("\ndeque")
print(f"deque d: {d}")

d.appendleft(9)
print(f"d.appendleft(9): {d}")

d.pop()
print(f"d.pop(): {d}")

d.popleft()
print(f"d.popleft(): {d}")

d.extend([7,8,9])
print(f"d.extend([7,8,9]): {d}")

d.extendleft([7,8,9])
print(f"d.extendleft([7,8,9]): {d}")

d.rotate(2)
print(f"d.rotate(2): {d}")

d.rotate(-2)
print(f"d.rotate(-2): {d}")
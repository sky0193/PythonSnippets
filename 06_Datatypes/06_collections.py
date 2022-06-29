# collections: Counter namedtuple, OrderedDict, defaultdict, deque
from collections import Counter 

a = "aaaabbbbbbccccccc"
my_counter = Counter(a)
print(f"\nmy_counter: {my_counter}")
print(f"my_counter.keys(): {my_counter.keys()}")
print(f"my_counter.values(): {my_counter.values()}")
print(f"my_counter.most_common(1): {my_counter.most_common(1)}")
print(f"my_counter.most_common(2): {my_counter.most_common(2)}")

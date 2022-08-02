# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(f"\nmap {list(b)}")

list_comp = [x*2 for x in a]
print(f"\nsame in list comprehension {list_comp}")


#filter(func, seq)

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(f"\nfilter {list(b)}")

list_comp = [x for x in a if x % 2 == 0]
print(f"\nsame in list comprehension {list_comp}")

#reduce(func, seq)
a = [1, 2, 3, 4, 5, 6]
product_a = reduce()
# Key-Value pairs, Unordered, Mutable

from collections import defaultdict


mydict = {"name": "Max", "age": 28}
print(f"mydict: {mydict}")

mydict2 = dict(name="Max", age=28)
print(f"mydict2 another creation method: {mydict2}")

print(f"\nname: {mydict['name']}")
print(f"age: {mydict['age']}")

mydict["lastname"] = "Müller"
print(f"\nadd lastname: {mydict}")

mydict.pop("age")
print(f"pop age: {mydict}")


print("\nCopy by mydict_copy_by_ref = mydict")
mydict_copy_by_ref = mydict

print(f"memory adress of mydict_copy_by_ref:{hex(id(mydict_copy_by_ref))}")
print(f"memory adress of mydict:{hex(id(mydict))}")


print("\nCopy by mydict_copy_by_value = mydict.copy()")
mydict_copy_by_value = mydict.copy() # or dict(mydict)

print(f"memory adress of mydict_copy_by_value:{hex(id(mydict_copy_by_value))}")
print(f"memory adress of mydict:{hex(id(mydict))}")

from collections import defaultdict

def def_value():
    return 0

defdict = defaultdict(def_value)
defdict["a"] = 2
defdict["b"] = 1
defdict["c"] = 6
print(f"\ndefdict: {defdict}")
print(f"no exception if value not exist defdict['t']: {defdict['t']}")


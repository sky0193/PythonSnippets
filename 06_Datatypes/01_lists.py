empty_list = list()
print(f"empty_list: {empty_list}")

another_empty_list = []
print(f"another_empty_list: {another_empty_list}")

mylist = [i for i in range(1, 10)]
print(f"mylist generation range(1,10): {mylist}")

length = len(mylist)
print(f"mylist len: {length}")

mylist.append(99)
print(f"mylist append 99: {mylist}")

mylist.insert(2, 66)
print(f"mylist.insert(2, 66): {mylist}")

mylist.pop()
print(f"mylist.pop(): {mylist}")

mylist.remove(3)
print(f"mylist.remove(3): {mylist}")

print(f"mylist slicing: {mylist[4:]}")

print(f"mylist step 2: {mylist[::2]}")

print(f"mylist revert: {mylist[::-1]}")

copy_list_by_ref = mylist
copy_list_by_ref.append(42)
print(f"copy_list_by_ref after apending 42: {copy_list_by_ref} and mylist {mylist}")

copy_list_by_value = mylist.copy() 
copy_list_by_value.append(23)
print(f"copy_list_by_value after apending 23: {copy_list_by_value} and mylist {mylist}")


list_comprehention_squerroot = [i * i for i in mylist] 
print(f"list_comprehention_squerroot: {list_comprehention_squerroot}")
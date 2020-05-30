
#! SET #
'''
unordered 
unindexed
Once a set is created you cannot change its items, but you can add new items
unchangable / IMMUTABLE
written in {}
'''

thisset = {"apple", "banana", "cherry"}
print(thisset)

#? add & update

thisset.add("orange")
print(thisset)

thisset.update(["orange", "mango", "grapes"])
print(thisset)

#? len
print(len(thisset))

#? remove & discard

thisset.remove("banana")
print(thisset)
# NOTE If the item to remove does not exist, remove() will raise an error

thisset.discard("banana")
print(thisset)
# NOTE If the item to remove does not exist, discard() will NOT raise an error

''' 
clear , pop , len same as List 
'''

#? JOIN SETS
'''
union() & update()
'''
# NOTE The union() method returns a new set with all items from both sets
# NOTE The update() method inserts the items in set2 into set1

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

#! LIST #
'''
ordered 
changeable / mutable
Allows duplicate members
written in []
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
#access the list items by referring to the index
print(thislist[1])
#reverse
print(thislist[-1]) 
#Range 
print(thislist[2:5])
#NOTE: The search will start at index 2 (included) and end at index 5 (not included)
print(thislist[:4]) #print 0 to 4
print(thislist[2:]) #print 2 to end
print(thislist[-4:-1]) # print from -4(include) to -1(not include)

#? CHANGE VALUE
thislist[1] = "blackcurrant"
print(thislist)

#? LIST LENGTH

print(len(thislist))

#? ADD ITEM FROM LIST

#? append
#NOTE The append() method append the specified item
thislist.append("orange")
print(thislist)
print(len(thislist))

#? insert
# NOTE The insert() method insert in specified index
thislist.insert(1, "orange")
print(thislist)

#? REMOVE ITEM FROM LIST

#? remove
# NOTE The remove() method removes the specified item
thislist.remove("orange")
print(thislist)

#? pop 
# NOTE The pop() method removes the specified index, (or the last item if index is not specified)
thislist2 = ["apple", "banana", "cherry"]
thislist2.pop()
print(thislist2)

#? del
del thislist2[0]
print(thislist2)

#? clear
#NOTE The clear() method empties the list
thislist2.clear()
print(thislist2)

#? COPY ITEM FROM LIST

#? copy
mylist = thislist.copy()
print(mylist)

#? list
mylist2 = list(thislist)
print(mylist2)

#? JOIN LISTS

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#? extend
# NOTE Use the extend() method to add list2 at the end of list1
list1.extend(list2)
print(list1)
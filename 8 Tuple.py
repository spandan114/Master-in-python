
#! TUPLE #
'''
ordered 
unchangeable / IMMUTABLE
written in ()
'''
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error becouse tuple is unchangeable
print(thistuple)
'''
You cannot remove items in a tuple
But you can delete
'''
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#? Create Tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

'''
Accessing , Indexing , Range , Length & Join  same as List 
'''
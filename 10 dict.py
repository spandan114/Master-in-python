
#! DICTIONARY #
'''
 unordered
 changeable / MUTABLE
 indexed
 have keys and values
 writen in {}
 '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#? Accessing Items
x = thisdict["model"]
x = thisdict.get("model")
print(x)

#? Change Values
thisdict["year"] = 2018
print(thisdict)

#? Length
print(len(thisdict))

#? Adding Items
thisdict["color"] = "red"
print(thisdict)

#? Removing Items

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict) #  removes the last inserted item

del thisdict["model"]
print(thisdict) # you can also delete complete dict

thisdict.clear()
print(thisdict) # empty the dictionary

'''
copy also same as list 
'''
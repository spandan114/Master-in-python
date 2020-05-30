"""
!DATATYPES

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

?what is mutable
 a mutable object can be changed after it is created
 NOTE Objects of built-in types like (list, set, dict) are mutable

?what is immutable
 a immutable object can't be changed after it is created
NOTE Objects of built-in types like (int, float, bool, str, tuple, unicode) are immutable

!PYTHON COLLECTIONS (ARRAY)

List       :- is a collection which is ordered and changeable. Allows duplicate members. #! MUTABLE
Tuple      :- is a collection which is ordered and unchangeable. Allows duplicate members. #! IMMUTABLE
Set        :- is a collection which is unordered and unindexed. No duplicate members. #! IMMUTABLE
Dictionary :- is a collection which is unordered, changeable and indexed. No duplicate members. #! MUTABLE

"""
#EXAMPLE OF IMMUTABLE
x = 10
y = x

x = x+1
"""
The object in which x was tagged is changed. 
object 10 was never modified. 
Immutable objects doesn’t allow modification after creation
"""
id(x) == id(y)
id(x) == id(10)


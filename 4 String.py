
# !STRING #
#?Strings are Arrays 

a = "Hello, World!"
print(a[0]) #remember that the first character has the position 0

#?Slicing

b = "Hello, World!"
print(b[2:5]) #Get the characters from position 2 to position 5 

#? Negative Indexing

b = "Hello, World!"
print(b[-5:-2]) #Get the characters from position 5 to position 1, starting the count from the end of the string

#?String Length

print(len(a))

#? strip()
#The strip() method removes any whitespace from the beginning or the end
print(a.strip())

#? lower() & upper()
print(a.lower())
print(a.upper())

#? replace()
x="spandan hoshi"
print(x)
print(a.replace('h','J'))
print(x)

#? split()
m = "Hello, World!"
print(m.split(",")) # returns ['Hello', ' World!']

#? Check String
#To check if a certain phrase or character is present in a string, we can use the keywords in or not in

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

x = "ain" not in txt
print(x) 

#? String Concartinate

a = "Hello"
b = "World"
c = a + b
print(c)
d = a + " " + b
print(d)

#? String Format

age = 36
tx = "My name is John, I am " 
tx = "My name is John, I am " + age
print(tx) #its not working thats why we use string formating
tx = "My name is John, I am {}"
print(tx.format(age))
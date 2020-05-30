
#! LOOP #
'''
TODO
while loops
for loops
'''

#? while loops

i = 1
while i < 6:
  print(i)
  i += 1

#! Brake 
# NOTE break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#! Continue
# NOTE continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#! While .. else

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#? For loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#! looping rgrough string
for x in "banana":
  print(x)

#! range in for loop

for x in range(6):
  print(x)
# for x in range(2,6):
#   print(x)
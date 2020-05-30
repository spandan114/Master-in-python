
#! if..else #

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#! if..elif..else #

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#? Short Hand If..else #

a = 2
b = 330
print("A") if a > b else print("B")

#? Nested If

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# NOTE if statements cannot be empty but someresion if you have empty if then you can use pass
a = 33
b = 200

if b > a:
  pass
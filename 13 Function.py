
#! FUNCTION #

def displayName(name):
  print("hello " + name)

displayName("spandan")

#? *args (arguements)
# NOTE If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "facebook", "wechat")
# arg with key = value
def my_function2(child3, child2, child1):
  print("The youngest child is " + child3)
my_function2(child1 = "facebook", child2 = "whatsapp", child3 = "wechat")

#? **kwargs (keywords)
#NOTE If the number of keyword arguments is unknown, add a double ** before the parameter name

def my_function3(**kid):
  print("His last name is " + kid["lname"])

my_function3(fname = "spandan", lname = "joshi")

#? Return Values

def my_function5(x):
  return 5 * x

print(my_function5(3))

#? Pass

def myfunction():
  pass

#! LAMBDA #
'''
A lambda function is a small anonymous function
A lambda function can take any number of arguments, but can only have one expression

syntex : lambda arguments : expression
'''

x = lambda a : a + 10
print(x(5))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2) # argument for n
print(mydoubler(11)) # argument for a
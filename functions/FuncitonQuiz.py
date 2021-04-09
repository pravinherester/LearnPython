#Without running the code below, what do you think will be printed in the console?

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
print(add(2, multiply(5, divide(8, 4))))
#10,12.0,0.21,14


#What would you predict to be the result of running the following code?

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

# a = 5, which means c = 5. b = 10, which means d = 10. The output of inner_function becomes the output of outer_function.


# Question 3:
# What will be printed in the console after running the following code?

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

#NameError,SyntaxError, None, "Pass", "Great"

# The return keyword will exit the function and prevent the rest of the code from being executed.



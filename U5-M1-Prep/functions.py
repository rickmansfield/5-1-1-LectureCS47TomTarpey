# To define a function in Python, we follow this syntax:

# def function_name(argument_1, argument_2, etc):
# function line 1
# function line 2
# etc.

# Let's define a greeting function that allows us to specify a name and a specific greeting.


def greet(name, greeting):
    print("Hello, %s, %s" % (name, greeting))


greet("Austen", "I hope you are having an excellent day!")
# Hello, Austen, I hope you are having an excellent day!
greet("Rick", "You are an awesome coder!")

# If we want to define a function that returns a value to the caller, we use the return keyword.


def double(x):
    return x * 2


eight = double(4)
print(eight)  # 8

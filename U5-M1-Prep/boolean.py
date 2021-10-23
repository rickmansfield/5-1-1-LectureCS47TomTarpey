# use comparison Operators

x = 10
print(x == 10)  # true
print(x == 5)  # false
print(x > 5)  # true
print(x >= 5)  # true
print(x <= 5)  # false
print(x <= 10)  # true

# use and + or
name = "Elon"
age = 49
if name == "Elon" and age == 49:
    print("Yay! we found Elon!")
if name == "Elon" or age == 49:
    print("Yay! we found Elon!")

# USE in 
years = [2018, 2019, 2020, 2021]
year = 2020

if year in years:
    print("%s is in the years collection" % year)

# USE elif
first_statement = False
second_statement = True

if first_statement:
    print("The first statement is true")
elif second_statement:
    print("The second statement is true")
else:
    print("Neither the first statement nor the second statement are true")

# USE == vs is
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True because a and b have the same value
print(a is b)  # False because a and b reference two different list objects

x = [1, 2, 3]
y = x

print(x == y)  # True because x and y have the same value
print(x is y)  # True because x and y reference the same list object


# USE not
print(not False)    # True
print(not (1 == 1))  # False because 1 == 1 is True and then is inverted by not
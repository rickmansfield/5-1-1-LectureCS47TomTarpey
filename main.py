print("Hello from the colab!")  # Hello from the colab!

# Let's print some things to the screen!
print("Hello to CS47!")  # Hello to CS47!
print("some other stuff")  # some other stuff


# lets look at some types

print(type(123))  # <class 'int'>
print(type(12.9))  # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type({"a": 12, "b": 22}))  # <class 'dict'>

# ------------basic operators---------------
"""
= # assignment
+= 1 # increment
-= 1 # decrement
*
*=
/=
/
%
"""

a = 12
b = 10
print(a)  # 12
a += b
print(a)  # 22

a *= b
print(a)  # 220

# --------f-strings-----------------
z = 1234567
s1 = str(3) + "   hello some text   " + str(z) + "   " + str(z + 3)
s = f" {1 + 2}   {'hello'} some text   {z}   {z + 3}"

print(type(s))  # <class 'str'>

# --------string operations----------
st = "The brown fox is in the hen house! and i want to fix some things here."
# The brown fox is in the hen house! and i want to fix some things here.
print(st)
st2 = st.lower()
# the brown fox is in the hen house! and i want to fix some things here.
print(st2)

# ---------conditionals----------
a = 90
if a > 50:
    print("a is bigggggggg")
    if a == 100:
        print("you are 100!!!!!")
elif a <= 40:
    print("AAAAAAAAAAAA?!")
else:
    print("I am a fish!")  # since a = 90 the terminal prints "a is bigggggggg"

# -------indentation----- is key to help python know where we are in our code
a = 90
if a > 50:
    print("a is bigggggggg")
    if a == 100:
        print("you are 100!!!!!")
elif a <= 40:
    print("broken stuff")
    print("AAAAAAAAAAAA?!")
else:
    print("I am a fish!")

# ----------looping--------------

letters = ["a", "b", "c", "d"]

for letter in letters:
    print(letter.upper())

for i in range(len(letters)):
    if i == 1:
        continue
    print(letters[i].upper())

i = 0
while i < len(letters):
    print(letters[i].upper())
    i += 1

"""
A
B
C
D
A
C
D
A
B
C
D
"""

# lets define some functions and use them


def add(a, b):
    for i in range(0, 10):
        print(i)
        if i == 5:
            break
    return a + b


add(1, 2)
"""
0
1
2
3
4
5
6
7
8
9
3
"""
# range as the iterable for a for loop.

# Prints 0, 1, 2, 3, 4
for x in range(5):
    print(x)

# Prints 2, 3, 4, 5, 6
for x in range(2, 7):
    print(x)

# Prints 1, 3, 5, 7 the number two means every other number or every two values
for x in range(1, 8, 2):
    print(x)
    
# ----- while loop to print the same values as the for loops above.-----

# Prints 0, 1, 2, 3, 4
count = 0
while count < 5:
    print(count)
    count += 1

# Prints 2, 3, 4, 5, 6
count = 2
while count < 7:
    print(count)
    count += 1

# Prints 1, 3, 5, 7
count = 1
while count < 8:
    print(count)
    count += 2

# -----break statement ---- to exit a for loop or a while loop.

# Prints 0, 1, 2, 3, 4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# ------Continue statement -------to skip the current block but not exit the loop entirely.

# Prints 1, 3, 5, 7
for x in range(8):
    # if x is even, skip this block and do not print
    if x % 2 == 0:
        continue
    print(x)

x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

a = 111
b = 222
c = 333
d = 9119
# Loop over each digit(integer) converted to a string class
# square each digit and store them in a vaiable
# convert each individual digit back to string class & 
# append the string with each iteration to form a final string
# return and convet the string back to an integer
def csSquareAllDigits(n):
    s = ""
    for i in str(n):
        y = int(i) * int(i)
        s += str(y)
    return int(s)

print(csSquareAllDigits(a))
print(csSquareAllDigits(b))
print(csSquareAllDigits(c))
print(csSquareAllDigits(d))
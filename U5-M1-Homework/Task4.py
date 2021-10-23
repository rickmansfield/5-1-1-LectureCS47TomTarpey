str1 = "12345"
str2 = "RICK"
str3 = "R I C K"
str4 = "1dd3$%"
str5 = "BOLD"
str6 = "Hello World"

def csOppositeReverse(txt):
# revers order can be done with slicing, join(), reversed() for or while loops
## slicing uses string[start:stop:step]
    flippedOrder = txt[::-1]
# change casing to opposite curret casing
    return flippedOrder.swapcase()
# return result
print(csOppositeReverse(str6))
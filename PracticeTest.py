def addTwoDigits(n):

    # understand return sum of a two digit numbers individual digits from 10< n <99
    # Plan convert to a string
    # split the string into indivdual chracters
    # convert the characters back to numbers in a list
    # add the numbers in the list.
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n//10
        sum += n
        return sum

print(addTwoDigits(66))

# Alternative
# Function to get sum of digits


def getSum(n):

    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = 66
print(getSum(n))

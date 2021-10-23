# product_name = "bananas"
# price = 1.23
# product_id = 123456
# format_string = "The price of these %s id: %d are %.2f " % (product_name, product_id, price)
# print(format_string)

my_string = "Hello, World"

# print string length
print(len(my_string))  # 12 print string length

# print index (desired at rld in this case)
print(my_string.index("rld"))  # 9 print index starting at r of rld

# count occurrences
print(my_string.count('l'))  # 3 how often l appreas in the string
print(my_string.count('He'))  # 1 how often He appreas in the string

#  SLICE STRINGS
#  Slice our ell
print(my_string[1:4])  # ell is the slice starting at 1 and ending at 3 (before 4)
#  slice out every other letter starting at World
print(my_string[7:12:2])  # Wrd

#  REVERSE THE STRING
print(my_string[::-1])  # reverses the string

# CHANGE CASE  
print(my_string.upper())
print(my_string.lower())

#  STARTS or ENDS WITH
print(my_string.startswith("H"))  # H returns true
print(my_string.endswith("H"))  # H returns false

#  SPLIT STRING
print(my_string.split(" "))  # splits the string by a space
print(my_string.split(", "))  # splits the string by a comman and a space

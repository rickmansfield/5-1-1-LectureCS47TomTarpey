str1 = "12345"
str2 = "RICK"
str3 = "R I C K"
str4 = "1dd3$%"
str5 = "BLOD"

def csAlphanumericRestriction(input_str):
    if input_str.isalpha():
        return True
    elif input_str.isnumeric():
        return True
    else:
        return False

print(csAlphanumericRestriction(str1))
csAlphanumericRestriction(str2)
csAlphanumericRestriction(str3)
csAlphanumericRestriction(str4)
csAlphanumericRestriction(str5)

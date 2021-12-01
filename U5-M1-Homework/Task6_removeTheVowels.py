str1 = "Lambda School is awesome!"
str2 = "BOLD"
str3 = "Hello World"


def csRemoveTheVowels(input_str):
    newString = ""
    # input_str = input_str.lower()
    for i in input_str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            pass
        else:
            newString = newString + i
    return newString

# csRemoveTheVowels(str1)
print(csRemoveTheVowels(str2))
print(csRemoveTheVowels(str3))
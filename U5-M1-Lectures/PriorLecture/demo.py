"""
U, P, E, R
Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.
Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
Notes:
- All of the letters in the input list will always be lowercase.

- input?  a list of characters all lower case
- output? dictionary of lower case keys and upper case values

-------
create an empty dictionary / hashmap
iterate over the input array extracting each letter
  - set the hashmap at the key of letter equal to the uppercased version of the letter

return the hashmap to the caller
-------

"""


def mapping(letters): # O(n) linear time complexity
  d = {} # O(1)

  for letter in letters: # O(n)
    d[letter] = letter.upper() # O(1)

  return d # O(1)

print(mapping(["p", "s"])) #  ➞ { "p": "P", "s": "S" }
print(mapping(["a", "b", "c"])) # ➞ { "a": "A", "b": "B", "c": "C" }
print(mapping(["a", "v", "y", "z"])) #  ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
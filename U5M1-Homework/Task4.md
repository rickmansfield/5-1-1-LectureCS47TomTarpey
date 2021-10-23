# Codewriting

- Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

## Examples:

- csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
- csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
- csOppositeReverse("Radar") ➞ "RADAr"

## Notes:

- The input string will only contain alpha characters.
- [execution time limit] 4 seconds (py3)

- [input] string txt

- [output] string

## [Python 3] Syntax Tips

```python
# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
```

--------------ricks notes for solving-------------

- There is NO reverse() function in the string class.
- Some of th ways to reverse a string include:
    - Slicing
    - join() function
    - reversed() function
    - for and while loops
  - slicing is the "recommended" way to reverse a sting. It's supposed to be simpler and faster. 
    - [ReverseOrder](https://www.journaldev.com/23647/python-reverse-string)
    - [InvertCasing](https://www.tutorialspoint.com/How-to-invert-case-for-all-letters-in-a-string-in-Python)
    - [GeneralReference](https://www.youtube.com/watch?v=VchuKL44s6E)
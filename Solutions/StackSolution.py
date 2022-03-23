"""
CSE212
Final Project - Solution
- Michael Hampton
"""


def Stack_Solution(text):
    # a list and a string variable
    text_stack = []
    reversed_text = ""

    # add all letters to list
    for letter in text:
        text_stack.append(letter)

    # remove all letters from stack and add to string in reverse order
    while len(text_stack) > 0:
        reversed_text += text_stack.pop()

    return reversed_text



# Test 1
print(Stack_Solution("live"))

# Test 2
print(Stack_Solution("flow"))

# Test 3
print(Stack_Solution("pots"))

# Test 4
print(Stack_Solution("warts"))

# Test 5
print(Stack_Solution("rail"))
from data_structures.stack import Stack


def multi_bracket_validation(str):
    balanced = True
    opened = Stack()
    brackets = {'{': 'open',
                '(': 'open',
                '[': 'open',
                '}': 'close',
                ')': 'close',
                ']': 'close'
                }

    match = {'{': '}', '(': ')', '[': ']'}

    for char in str:
        if char in brackets.keys():
            if brackets[char] == 'open':
                opened.push(char)
            else:
                if opened.is_empty():
                    balanced = False
                    return balanced
                if char == match[opened.peek()]:
                    opened.pop()
                else:
                    balanced = False
                    return balanced

    if not opened.is_empty():
        balanced = False

    return balanced



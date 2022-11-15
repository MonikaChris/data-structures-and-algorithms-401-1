from data_structures.stack import Stack


def multi_bracket_validation(str):
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
                    return False
                if char == match[opened.peek()]:
                    opened.pop()
                else:
                    return False

    if not opened.is_empty():
        return False

    return True



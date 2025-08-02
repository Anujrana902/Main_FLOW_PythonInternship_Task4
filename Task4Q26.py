def is_balanced_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

def main():
    s1 = "{[()]}"
    s2 = "{[(])}"
    print(f"{s1} is balanced:", is_balanced_parentheses(s1))
    print(f"{s2} is balanced:", is_balanced_parentheses(s2))

if __name__ == "__main__":

    main()

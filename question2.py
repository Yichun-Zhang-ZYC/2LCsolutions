def check_parentheses(strings):
    outputs = []
    for string in strings:
        stack = []
        marks = [' ' for _ in range(len(string))]

        for i, ch in enumerate(string):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    marks[i] = '?'

        for i in stack:
            marks[i] = 'x'

        outputs.append((string, ''.join(marks)))

    return outputs


sample_inputs = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu )))",
    "UUUU((()"
]


results = check_parentheses(sample_inputs)


for result in results:
    print(result[0])
    print(result[1])


additional_sample_inputs = [
    "))))",
    "((((((((",
    "()()()",
    ")(())(",
    "((())",
    "(()))",
    "((x)(y))",
    "",
    "((())())",
    "(((())())"
]


additional_results = check_parentheses(additional_sample_inputs)


for result in additional_results:
    print(result[0])
    print(result[1])

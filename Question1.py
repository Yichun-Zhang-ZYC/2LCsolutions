def shortest_way(source: str, target: str) -> int:
    m, n = len(source), len(target)
    count = 0
    i = 0

    while i < n:
        subseq_found = False  # find target?
        for j in range(m):  # all in source
            if i < n and source[j] == target[i]:
                i += 1
                subseq_found = True
        if not subseq_found:
            return -1
        count += 1 

    return count

# 测试用例
print(shortest_way("abc", "abcbc"))  #2
print(shortest_way("abc", "acdbc")) #-1
print(shortest_way("xyz", "xzyxz"))  #3

# 测试用例
test_cases = [
    ("abc", "abcbc", 2),
    ("abc", "acdbc", -1),
    ("xyz", "xzyxz", 3),
    ("a", "aaaa", 4),
    ("abc", "abc", 1),
    ("", "abc", -1),
    ("abc", "", 0),
    ("ab", "ababab", 3),
    ("abc", "cba", 3),
    ("abcdef", "fedcba", 6),
    ("z", "zzzzz", 5),
]

# 运行测试用例
for i, (source, target, expected) in enumerate(test_cases, 1):
    result = shortest_way(source, target)
    assert result == expected, f"Test case {i} failed: source={source}, target={target}, expected={expected}, got={result}"
    print(f"Test case {i} passed.")

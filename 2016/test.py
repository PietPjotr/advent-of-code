import re

pattern = re.compile(r'(^|\])[a-z]+($|\[)')

# Test
test_strings = [
    "[abc]",
    "]def[",
    "ghi[jkl]",
    "[mno[pqr]stu",
    "]vwx[yz]",
    "foo[bar]baz",
    "[qux",
    "r]ab",
    "s[tuv]w",
]

for test_string in test_strings:
    match = pattern.search(test_string)
    if match:
        print(f"Match found in '{test_string}': {match.group()}")
    else:
        print(f"No match found in '{test_string}'")
# You are given a string S.
# Your task is to find out whether S is a valid regex or not.

import re
test_cases = int(input())
for i in range(test_cases):
    s = input()
    try:
        re.compile(s)
        print('True')
    except re.error:
        print('False')
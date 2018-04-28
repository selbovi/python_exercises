import sys

res = ''
for line in sys.stdin:
    res += line

print(len(set(res.split())))

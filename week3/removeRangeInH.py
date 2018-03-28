s = input()
last = 0
first = s.find('h')
pos = 0
while pos != -1:
    pos = s.find('h', pos + 1)
    if (pos > last):
        last = pos

res = s[0:first] + s[last + 1:(len(s))]
print(res)

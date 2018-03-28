s = input()
last = 0
pos = 0
while pos != -1:
    pos = s.find('f', pos + 1)
    if (pos > last):
        last = pos

if last == s.find('f'):
    print(last)
elif s.find('f') > -1:
    print(s.find('f'), last)

s = input()
sec = s.find('f', s.find('f') + 1)

if s.find('f') == -1:
    print(-2)
elif sec == -1:
    print(-1)
else:
    print(sec)

c1 = int(input())

if c1 % 10 == 1:
    print(str(c1), ' ', 'korova')
elif c1 < 5:
    print(str(c1), ' ', 'korovy')
else:
    print(str(c1), ' ', 'korov')

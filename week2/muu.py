c1 = int(input())

c_ = c1 < 5 or c1 % 10 == 2 or c1 % 10 == 3 or c1 % 10 == 4
if (c1 == 1 or c1 % 10 == 1) and not c1 == 11:
    print(str(c1), ' ', 'korova')
elif c1 == 0 or c1 % 10 == 0:
    print(str(c1), ' ', 'korov')
elif (c_) and (c1 != 12 and c1 != 13 and c1 != 14):
    print(str(c1), ' ', 'korovy')
else:
    print(str(c1), ' ', 'korov')

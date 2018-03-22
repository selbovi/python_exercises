total = int(input())
noDays = total % (24 * 60)
print((noDays // 60) % 24, noDays % 60)

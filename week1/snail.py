h = int(input())
mPerDay = int(input())
slipMeters = int(input())

print((h // (mPerDay - slipMeters)) % h)

def seqSum(m):
    x = int(input())
    if x == 0:
        return m
    else:
        return seqSum(m + x)


seq_sum = seqSum(0)

print(seq_sum)

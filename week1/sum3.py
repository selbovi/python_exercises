numStr = input()
num = int(numStr)
ten = ((num % 100) // 10)
last = int(numStr[len(numStr)-1])
fst = num // 100
print(fst + ten + last)

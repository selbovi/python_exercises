import functools

print(functools.reduce(
    min,
    filter(
        lambda x: x % 2 != 0,
        map(int, input().split())
    )
))

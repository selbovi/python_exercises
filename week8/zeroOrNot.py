import sys

print(any(
    map(lambda x: x == 0, map(
        int,
        set(sys.stdin.read().split()).split())
        )
)
)

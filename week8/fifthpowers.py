import functools

print(functools.reduce(
    lambda x, y: x * y,
    list(
        map(
            lambda x: x ** 5,
            filter(
                lambda x: x > 1,
                list(
                    map(
                        int,
                        input().split()
                    )
                )
            )
        )
    )
))

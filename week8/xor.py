print(*map(
    lambda tup: tup[0] ^ tup[1],
    zip(
        list(
            map(
                int,
                input().split()
            )
        ),
        list(
            map(
                int,
                input().split()
            )
        )
    )
)
      )

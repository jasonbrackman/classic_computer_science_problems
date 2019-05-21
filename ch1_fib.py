# Useful example as it is my first case of seeing type declarations in this way.

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}  # our base cases


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization

    return memo[n]


def fib5(n: int) -> int:
    if n == 0:
        return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next

    return next


from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0:
        yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step


if __name__ == "__main__":
    print(fib3(50))
    print(fib5(50))
    print([i for i in fib6(50)][-1])

def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_euclidean(b, a % b)
        return (gcd, y, x - (a // b) * y)


def diophantine(a: int, b: int, c: int) -> None | tuple[int, int]:
    gcd, x, y = extended_euclidean(a, b)
    if c % gcd != 0:
        return None
    else:
        return (x * (c // gcd), y * (c // gcd))


if __name__ == '__main__':
    # Example usage:
    print(diophantine(5, 7, 1))  # Output: (3, -2)

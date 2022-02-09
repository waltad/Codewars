# reverse_seq = lambda n: [_ for _ in range(n, 0, -1)]
reverse_seq = lambda n: list(range(n, 0, -1))


def reverseseq(n):
    return list(range(n, 0, -1))


if __name__ == '__main__':
    n = 5
    print(reverseseq(n))

    print(reverse_seq(n))
#!/usr/bin/env python3
import sys


def solve(B: int, G: int):
    print("Bat" if B > G else "Glove")
    return


# Generated by 2.13.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    B = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    solve(B, G)

if __name__ == '__main__':
    main()

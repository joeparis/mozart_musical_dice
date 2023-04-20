#!/usr/bin/env python3
from minuet import Minuet


def main():
    # select instrument
    minuet = Minuet("piano")
    minuet.compose()
    minuet.play()
    # save minuet
    # minuet.save(filename)


if __name__ == "__main__":
    main()

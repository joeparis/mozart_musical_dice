#!/usr/bin/env python3
from minuet import Minuet


def main():
    # TODO: select minuet or trio
    # TODO: select instrument
    minuet = Minuet("piano")
    minuet.compose()
    minuet.play()
    # TODO: save minuet


if __name__ == "__main__":
    main()

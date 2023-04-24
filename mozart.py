#!/usr/bin/env python3
from enum import Enum
from os import name, system

from minuet import Minuet


class Instrument(Enum):
    CLARINET = 1
    FLUTE = 2
    MBIRA = 3
    PIANO = 4


class Style(Enum):
    MINUET = 1
    TRIO = 2


def get_style() -> str:
    prompt = """What style of composition would you like?

    1. minuet
    2. trio"""

    print(prompt)
    print()

    style = int(input("Please enter the number of your selection: "))

    match style:
        case Style.MINUET.value:
            return "minuet"
        case Style.TRIO.value:
            return "trio"
        case _:
            return "unknown"


def get_instrument() -> str:
    prompt = """What instrument would you like to use? You may choose:

    1. clarinet
    2. flute
    3. mbira
    4. piano """

    print(prompt)
    print()
    instrument = int(input("Please enter the number of your selection: "))

    match instrument:
        case Instrument.CLARINET.value:
            return "clarinet"
        case Instrument.FLUTE.value:
            return "flute-harp"
        case Instrument.MBIRA.value:
            return "mbira"
        case Instrument.PIANO.value:
            return "piano"
        case _:
            return "unknown"


def clear():
    """Clear the screen."""
    _ = system("cls") if name == "nt" else system("clear")


def main():
    clear()
    style = get_style()
    clear()
    instrument = get_instrument()
    # composition = Minuet(instrument) if style == "minuet" else Trio(instrument)
    composition = Minuet(instrument)
    composition.compose()
    composition.play()

    # TODO: save minuet


if __name__ == "__main__":
    main()

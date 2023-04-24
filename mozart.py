#!/usr/bin/env python3
from os import name, system

from minuet import Minuet


def get_selection(prompt: str, options: tuple, clear_screen=True) -> str:
    if clear_screen:
        clear()

    print(prompt)
    for idx, option in enumerate(options):
        print(f"  {idx + 1}. {option.lower()}")

    print()
    selection = int(input("Please enter the number of your selection: ")) - 1

    return options[selection].replace(" & ", "-")  # HACK


def clear():
    """Clear the screen."""
    _ = system("cls") if name == "nt" else system("clear")


def main():
    styles = ("minuet", "trio")
    instruments = ("clarinet", "flute & harp", "mbira", "piano")

    style = get_selection("What style of composition would you like to create? ", styles)
    instrument = get_selection("What instrument would you like to use? ", instruments)

    # composition = Minuet(instrument) if style == "minuet" else Trio(instrument)
    composition = Minuet(instrument)
    composition.compose()
    composition.play()

    # TODO: save minuet


if __name__ == "__main__":
    main()

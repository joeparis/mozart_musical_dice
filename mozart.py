#!/usr/bin/env python3
from collections import namedtuple
from os import name, system
from pathlib import Path

from waltz import Waltz

Instrument = namedtuple("Instrument", "name,path")


def get_instruments() -> dict[int, Instrument]:
    """Get all available instruments."""
    instruments = sorted(
        [
            instrument
            for instrument in Path(Path.cwd() / "instruments").iterdir()
            if instrument.is_dir()
        ],
        key=lambda path: path.name,
    )

    return {
        index + 1: Instrument(name=str(path.name).lower().replace("-", " & "), path=path)
        for index, path in enumerate(instruments)
    }


def get_instrument_wav_path() -> Path:
    """Get the path for the desired instrument's WAV files."""
    available_instruments = get_instruments()

    while True:
        for index, instrument in available_instruments.items():
            print(f"  {index}. {instrument.name}")

        selection = int(input("\nPlease enter the number of your selection: "))
        try:
            return available_instruments[selection].path
        except KeyError:
            print(f"\nSorry, {selection} is not a valid option. Please try again.\n")


def clear():
    """Clear the screen."""
    _ = system("cls") if name == "nt" else system("clear")


def main():
    clear()
    instrument_path = get_instrument_wav_path()
    composition = Waltz(instrument_path)
    composition.compose()
    composition.play()

    # TODO: save minuet


if __name__ == "__main__":
    main()

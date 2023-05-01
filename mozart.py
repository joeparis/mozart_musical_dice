#!/usr/bin/env python3
from collections import namedtuple
from os import name, system
from pathlib import Path

from consolemenu import SelectionMenu

from waltz import Waltz

Instrument = namedtuple("Instrument", "name,path")


def get_instruments() -> list[Instrument]:
    """Get all available instruments."""
    instruments = sorted(
        [
            instrument
            for instrument in Path(Path.cwd() / "instruments").iterdir()
            if instrument.is_dir()
        ],
        key=lambda path: path.name,
    )

    return [
        Instrument(name=str(path.name).lower().replace("-", " & "), path=path)
        for path in instruments
    ]


def get_instrument_wav_path() -> Path:
    """Get the path for the desired instrument's WAV files."""
    available_instruments = get_instruments()

    selection = SelectionMenu.get_selection(
        strings=[instrument.name for instrument in available_instruments],
        title="Let's make a Musikalisches Würfelspiel...",
        subtitle="Please select your instrument:",
    )

    return available_instruments[selection].path


def clear():
    """Clear the screen."""
    _ = system("cls") if name == "nt" else system("clear")


def save_waltz() -> bool:
    # selection = SelectionMenu.get_selection(strings=["Yes", "No"], title="Save your waltz?",)
    menu = SelectionMenu(strings=["Yes", "No"], title="Save your waltz?", show_exit_option=False)
    menu.show()
    menu.join()
    selection = menu.selected_option

    if selection == 0:
        return True

    return False


def main():
    instrument_path = get_instrument_wav_path()

    composition = Waltz(instrument_path)
    composition.compose()
    print("Playing...")
    composition.play()
    clear()

    if save_waltz():
        filename = input("Please enter a name for your waltz: ")
        composition.save(filename)


if __name__ == "__main__":
    main()

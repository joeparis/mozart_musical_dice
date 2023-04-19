##!/usr/bin/env python3
import pathlib
import random
import wave

import simpleaudio as sa


class Die:
    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)


def make_minuet(instrument: pathlib.Path):
    PHRASE_COUNT = 16

    die1 = Die()
    die2 = Die()

    for i in range(PHRASE_COUNT):
        s = die1.roll() + die2.roll()
        phrase = f"{instrument}/minuet{i}-{s}.wav"
        print(phrase)
        wave_obj = sa.WaveObject.from_wave_file(phrase)
        play_obj = wave_obj.play()
        play_obj.wait_done()


def main():
    CWD = pathlib.Path(__file__).parent
    PIANO_PATH = CWD / "phrases" / "piano"

    make_minuet(PIANO_PATH)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import pathlib
import tempfile
import wave

import simpleaudio as sa

from die import Die


class Minuet:
    def __init__(self, instrument: str = "piano") -> None:
        self.instrument_path = pathlib.Path(f"./phrases/{instrument}")

        if not self.instrument_path.exists():
            raise ValueError(f"{instrument} is not a valid instrument")

        self.phrase_count = 16
        self.composition = None

    def compose(self):
        die1 = Die()
        die2 = Die()

        phrases = [
            self.instrument_path / f"minuet{phrase}-{die1.roll() + die2.roll()}.wav"
            for phrase in range(self.phrase_count)
        ]

        data = []
        for phrase in phrases:
            wav = wave.open(str(phrase), "rb")
            data.append([wav.getparams(), wav.readframes(wav.getnframes())])
            wav.close()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
            output = wave.open(temp, "wb")
            output.setparams(data[0][0])

            for idx, _ in enumerate(data):
                output.writeframes(data[idx][1])  # pylint: disable=unnecessary-list-index-lookup

            output.close()

            self.composition = temp.name

    def save(self, filename: str) -> None:
        pass

    def play(self) -> None:
        wave_obj = sa.WaveObject.from_wave_file(self.composition)
        play_obj = wave_obj.play()
        play_obj.wait_done()

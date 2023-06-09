#!/usr/bin/env python3
import shutil
import tempfile
import wave
from pathlib import Path

import simpleaudio as sa

from die import Die


class Waltz:
    """A randomly generated musical composition.

    A Musikalisches Würfelspiel is a process for generating music by concatenating a
    random sequence of precomposed musical fragments. This class represents a
    Musikalisches Würfelspiel-style Viennese waltz in the style of Mozart by
    combining a sequence of WAV files that are chosen at random (from a set of 272)
    according to the results of throwing dice."""

    def __init__(self, instrument_path: Path) -> None:
        self.instrument_path = instrument_path

        if not self.instrument_path.exists():
            raise ValueError(f"{instrument_path} not found")

        self.phrase_count = 16
        self.composition: Path | None = None

    def compose(self):
        """Compose the waltz."""
        die = Die()

        phrases = [
            self.instrument_path / f"minuet{phrase}-{die.roll() + die.roll()}.wav"
            for phrase in range(self.phrase_count)
        ]

        phrases.extend(
            [
                self.instrument_path / f"trio{phrase}-{die.roll()}.wav"
                for phrase in range(self.phrase_count)
            ]
        )

        data = []
        for phrase in phrases:
            wav = wave.open(f"{phrase}", "rb")
            data.append([wav.getparams(), wav.readframes(wav.getnframes())])
            wav.close()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
            output = wave.open(temp, "wb")
            output.setparams(data[0][0])

            for idx, _ in enumerate(data):
                output.writeframes(data[idx][1])  # pylint: disable=unnecessary-list-index-lookup

            output.close()

            self.composition = Path(temp.name)

    def save(self, filename: str) -> None:
        """Save the composition."""
        shutil.copyfile(str(self.composition), (Path.cwd() / filename).with_suffix(".wav"))

    def play(self) -> None:
        """Play the waltz."""
        wave_obj = sa.WaveObject.from_wave_file(self.composition)
        play_obj = wave_obj.play()
        play_obj.wait_done()

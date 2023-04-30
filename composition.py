#!/usr/bin/env python3
"""A randomly generated musical composition.

A Musikalisches Würfelspiel is a process for generating music by concatenating a
random sequence of precomposed musical fragments. This class represents a
Musikalisches Würfelspiel-style Viennese waltz in the style of Mozart by
combining a sequence of WAV files that are chosen at random (from a set of 272)
according to the results of throwing dice."""
import tempfile
import wave
from abc import ABC, abstractmethod
from pathlib import Path

import simpleaudio as sa

from die import Die


class Composition(ABC):
    @abstractmethod
    def compose(self) -> None:
        """Generate a random waltz in the style of Mozart."""

    @abstractmethod
    def play(self) -> None:
        """Play the generated waltz."""

    @abstractmethod
    def save(self, filename: Path) -> None:
        """Save the generated waltz."""

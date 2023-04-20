#!/usr/bin/env python3
import random
from dataclasses import dataclass


@dataclass(eq=False, order=False, frozen=True)
class Die:
    """A fair n-sided die."""

    sides: int = 6

    def roll(self) -> int:
        """Roll the die.

        Returns:
            int: The result of rolling the die, a number between 1 and sides (inclusive).
        """
        return random.randint(1, self.sides)

"""
Classes and Object-Oriented Programming in Python
===================================================
Demonstrates class definition, instance attributes,
__init__ constructors, and instance methods, using a
Player (Jugador) class with unit-conversion helpers.
"""

import numpy as np


class Player:
    """Represents a sports player with weight and height attributes.

    Attributes:
        name   (str):   Player's name.
        height (float): Height in metres.
        weight (float): Weight in kilograms.
    """

    def __init__(self, name: str = "", weight: float = 0.0, height: float = 0.0):
        """Initialise the player.  Weight must be in kg, height in metres."""
        self.name   = name
        self.height = height
        self.weight = weight

    def set_weight_and_height(self, weight: float, height: float):
        """Assign weight (kg) and height (m) to the player."""
        self.weight = weight
        self.height = height

    def get_weight(self, unit: str = "kg") -> float:
        """Return weight in the requested unit ('kg' or 'lbs')."""
        if unit == "kg":
            return self.weight
        elif unit == "lbs":
            return self.weight * 2.2
        else:
            raise ValueError("unit must be 'kg' or 'lbs'")

    def get_height(self) -> float:
        """Return height in metres."""
        return self.height

    def bmi(self) -> float:
        """Calculate Body Mass Index (kg/m²)."""
        return self.weight / self.height ** 2

    def describe(self):
        """Print a summary of the player's stats."""
        print(
            f"Player: {self.name} | "
            f"Weight: {self.weight:.1f} kg ({self.get_weight('lbs'):.1f} lbs) | "
            f"Height: {self.height:.2f} m | "
            f"BMI: {self.bmi():.1f}"
        )


# ── Example usage ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    player = Player()
    player.name = "LeBron James"
    player.set_weight_and_height(113.4, 2.06)

    print("Weight in kg :", player.get_weight("kg"))
    print("Weight in lbs:", player.get_weight("lbs"))
    print("Height (m)   :", player.get_height())
    player.describe()

    # Create a second player using the constructor directly
    player2 = Player(name="Stephen Curry", weight=84.0, height=1.88)
    player2.describe()

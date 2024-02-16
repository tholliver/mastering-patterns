from dataclasses import dataclass
from food import Food


@dataclass
class Cat:
    energy: str

    def eat(s: Food):
        pass

from abc import ABC, abstractmethod


class Food(ABC):

    @abstractmethod
    def getNutrition(self):
        print('from Food interface')

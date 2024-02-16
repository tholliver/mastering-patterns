from food import Food


class Sausage(Food):

    def __init__(self, name: str):
        self.name = name

    def getNutrition(self):
        print('on Sausage', self.name)

    def getColor():
        pass

    def getExpiration(self):
        print('on Sausage', self.name)


newSausage = Sausage("Beef")
print(newSausage.name)
newSausage.getNutrition()

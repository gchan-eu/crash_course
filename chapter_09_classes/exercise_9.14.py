from random import randint

class Dice():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(randint(1, self.sides))

dice = Dice(20)
for i in range(10):
    dice.roll_dice()


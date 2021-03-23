from Gestures import Gestures
import random


class Player:
    def __init__(self):
        self.name = ""
        self.gesture = ""
        self.player_number = 1
        self.wins = 0
        self.type = ""


class Human(Player):
    def __init__(self):
        super().__init__()
        self.type = "Human"

    def choose_gesture(self, gestures):
        i = 0
        while i < len(gestures):
            print(f'{i}: {gestures[i]}')
            i += 1
        while True:
            try:
                choice = int(input("Please enter the number of your choice_ "))
                break
            except ValueError:
                print("Invalid input. Press either a number 0 - 4 : _ ")
        while choice != 0 or choice != 1 or choice != 2 or choice != 3 or choice != 4:
            if choice == 0 or choice == 1 or choice == 2 or choice == 3 or choice == 4:
                break
            while True:
                try:
                    choice = int(input("Please enter the number of your choice_ "))
                    break
                except ValueError:
                    print("Invalid input. Press either 0, 1, 2, 3, or 4:  ")

        return gestures[choice]


class AI(Player):
    def __init__(self):
        super().__init__()
        self.type = "AI"

    def choose_gesture(self, gestures):
        i = random.randint(0, 4)
        self.gesture = gestures[i]
        return gestures[i]





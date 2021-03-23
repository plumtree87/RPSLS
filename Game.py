from Player import Player, Human, AI
from Gestures import Gestures


class Game:
    def __init__(self):
        self.round = 0
        self.player1 = ""
        self.player2 = ""
        self.winner = ""
        self.game_end = False

    def game_start(self, game):
        gestures = Gestures().gestures
        player1 = self.create_player1()
        player2 = self.create_player2()
        self.game_rounds(player1, player2, gestures)
        self.replay(game)


    def game_rules(self, vs):
        print(" ")
        print(vs[0].name, "chose", vs[0].gesture)
        print(vs[1].name, "chose", vs[1].gesture)
        i = 0
        j = 1
        while j > -1 and i < 2:
            if vs[i].gesture == vs[j].gesture:
                print("TIE")
                break
            if vs[i].gesture == "Rock" and vs[j].gesture == "Scissors":
                print(" ")
                print("Rock crushes Scissors.", vs[i].name, "WINS!")
                vs[i].wins += 1
                break
            if vs[i].gesture == "Scissors" and vs[j].gesture == "Paper":
                print(" ")
                print("Scissors cuts Paper.", vs[i].name, "WINS!")
                vs[i].wins += 1
                break
            if vs[i].gesture == "Paper" and vs[j].gesture == "Rock":
                print(" ")
                print("Paper covers Rock.", vs[i].name, "WINS!")
                vs[i].wins += 1
                break
            if vs[i].gesture == "Rock" and vs[j].gesture == "Lizard":
                print(" ")
                print("Rock crushes Lizard.", vs[i].name, "WINS!")
                vs[i].wins += 1
                break
            if vs[i].gesture == "Lizard" and vs[j].gesture == "Spock":
                print(" ")
                print("Lizard poisons Spock.", vs[i].name, "WINS!")
                vs[i].wins += 1
                break
            if vs[i].gesture == "Spock" and vs[j].gesture == "Scissors":
                print(" ")
                print("Spock smashes Scissors.", vs[i].name, "WINS!")
                vs[i].wins += 1
                break
            if vs[i].gesture == "Scissors" and vs[j].gesture == "Lizard":
                print(" ")
                print("Scissors decapitates Lizard", vs[i].name, "WINS!")
                vs[i].wins += 1
                break
            if vs[i].gesture == "Lizard" and vs[j].gesture == "Paper":
                print(" ")
                print("Paper covers Rock.", vs[i].name, "WINS!")
                vs[i].wins += 1
                break
            if vs[i].gesture == "Paper" and vs[j].gesture == "Spock":
                print(" ")
                print("Paper disproves Spock.", vs[i].name, "WINS!")
                vs[i].wins += 1
                break
            if vs[i].gesture == "Spock" and vs[j].gesture == "Rock":
                print(" ")
                print("Spock vaporizes Rock.", vs[i].name, "WINS!")
                vs[i].wins += 1
                break

            i += 1
            j -= 1

    def create_player1(self):
        print("Please choose if Player 1 will be Human or AI")
        print("If Human enter 0")
        print("If AI enter 1")
        print(" ")
        while True:
            try:
                choice = int(input("Please enter the number of your choice_ "))
                break
            except ValueError:
                print("Invalid input. Press either 0 for a real player, or 1 for A.I.")
        while choice != 0 or choice != 1:
            if choice == 0:
                break
            if choice == 1:
                break
            else:
                while True:
                    try:
                        choice = int(input("Please press 0 for human or 1 for AI_ "))
                        break
                    except ValueError:
                        print("Invalid input. Press either 0 for a Human, or 1 for AI")
        if choice == 0:
            player1 = Human()
            name = input("What is your name?_ ")
            player1.name = name

        if choice == 1:
            player1 = AI()
            player1.name = "AI_Player1"
        return player1

    def create_player2(self):
        print("OK, now please choose if Player 2 will be Human or AI")
        print("If human enter 0")
        print("If AI enter 1")
        print(" ")
        while True:
            try:
                choice = int(input("Please enter the number of your choice_ "))
                break
            except ValueError:
                print("Invalid input. Press either 0 for a real player, or 1 for A.I.")
        while choice != 0 or choice != 1:
            if choice == 0:
                break
            if choice == 1:
                break
            while True:
                try:
                    choice = int(input("Please press 0 for human or 1 for AI_ "))
                    break
                except ValueError:
                    print("Invalid input. Press either 0 for a Human, or 1 for AI")
        if choice == 0:
            player2 = Human()
            name = input("What is your name?_ ")
            player2.name = name
            player2.player_number += 1

        if choice == 1:
            player2 = AI()
            player2.name = "AI_Player2"
            player2.player_number += 1
        return player2

    def game_rounds(self, player1, player2, gestures):
        print(" ")
        print(player1.name, "VS", player2.name)
        print("READY??")
        vs = [player1, player2]
        while player1.wins < 2 or player2.wins < 2:
            if player1.wins > player2.wins and player1.wins == 2:
                print(player1.name, "WINS THE GAME!")
                return True
            if player2.wins > player1.wins and player2.wins == 2:
                print(player2.name, "WINS THE GAME!")
                return True
            print(player1.name, "it's your turn.")
            player1.gesture = player1.choose_gesture(gestures)
            print(player2.name, "it's your turn.")
            player2.gesture = player2.choose_gesture(gestures)
            self.game_rules(vs)
            print(" ")
            print("Score:", player1.wins, "vs", player2.wins)
            print(" ")


    def replay(self, game):
        while not game.game_end:
            print(" ")
            re_play = input("Would you like to play again? y or n  ")
            if re_play == "y" or re_play == "Y":
                game.game_end = False
                game.round = 0
                game.player2 = ""
                game.player1 = ""
                game.winner = ""
                game.game_start(game)
            if re_play == "n" or re_play == "N":
                break
            else:
                print("Y or N")

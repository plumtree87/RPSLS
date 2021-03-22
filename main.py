from Game import Game

if __name__ == '__main__':
    print(" ")
    print("WELCOME TO ROCK PAPER SCISSORS LIZARD SPOCK")
    print("Best out of three, or first to win two games, wins!")
    print(" ")
    game = Game()
    game.game_start()
    while not game.game_end:
        print(" ")
        re_play = input("Would you like to play again? Y or N")
        if re_play == "y" or re_play == "Y":
            game.game_end = False
            game.game_start()
        if re_play == "n" or re_play == "N":
            break
        else:
            print("Hmm")



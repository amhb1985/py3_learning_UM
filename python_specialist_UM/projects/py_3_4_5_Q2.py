

import random

rand_number = random.randint(1, 10)
print('Random number between 1 and 10: {}'.format(rand_number))

letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
rand_letter = random.choice(letters)
print('Random letter: {}'.format(rand_letter))


import random
import time

# Definition der Player Klasse
class Player:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.prizes = []

    def add_money(self, amount):
        self.money += amount

    def deduct_money(self, amount):
        self.money = max(0, self.money - amount)

    def add_prize(self, prize):
        self.prizes.append(prize)

# Definition der HumanPlayer Klasse
class HumanPlayer(Player):
    def take_turn(self, game):
        while True:
            action = input(f"{self.name}, do you want to (1) guess a letter, (2) guess the phrase, or (3) pass? ")
            if action == '1':
                letter = input("Enter a letter to guess: ").lower()
                if len(letter) == 1 and letter.isalpha():
                    if letter in "aeiou" and self.money < 250:
                        print("You don't have enough money to guess a vowel.")
                        continue
                    return game.guess_letter(self, letter)
                else:
                    print("Invalid input. Please enter a single letter.")
            elif action == '2':
                phrase_guess = input("Enter your guess for the phrase: ").lower()
                return game.guess_phrase(self, phrase_guess)
            elif action == '3':
                print(f"{self.name} passes their turn.")
                return False
            else:
                print("Invalid input. Please enter 1, 2, or 3.")

# Definition der ComputerPlayer Klasse
class ComputerPlayer(Player):
    def take_turn(self, game):
        action = random.choice(['guess_letter', 'guess_phrase', 'pass'])
        if action == 'guess_letter':
            available_letters = [chr(i) for i in range(97, 123) if chr(i) not in game.guessed_letters]
            if not available_letters:
                print(f"{self.name} passes their turn due to no available letters.")
                return False
            letter = random.choice(available_letters)
            print(f"{self.name} guesses the letter: {letter}")
            return game.guess_letter(self, letter)
        elif action == 'guess_phrase':
            # Simplified phrase guessing logic for the bot
            phrase_guess = game.phrase.lower()
            print(f"{self.name} guesses the phrase: {phrase_guess}")
            return game.guess_phrase(self, phrase_guess)
        elif action == 'pass':
            print(f"{self.name} passes their turn.")
            return False

# Definition der Wheel Klasse
class Wheel:
    def __init__(self):
        self.segments = ["$500", "$1000", "$250", "Bankrupt", "Lose a turn"]
    
    def spin(self):
        return random.choice(self.segments)

# Definition der Game Klasse
class Game:
    def __init__(self, category, phrase, players):
        self.category = category
        self.phrase = phrase
        self.obscured_phrase = self._obscure_phrase(phrase)
        self.players = players
        self.current_player_index = 0
        self.guessed_letters = set()

    def _obscure_phrase(self, phrase):
        return ''.join(['_' if char.isalnum() else char for char in phrase])

    def display_game_state(self):
        print("\n" + "="*30)
        print(f"Category: {self.category}")
        print(f"Phrase: {self.obscured_phrase}")
        print(f"Guessed Letters: {', '.join(sorted(self.guessed_letters))}")
        for player in self.players:
            print(f"{player.name}: ${player.money}, Prizes: {', '.join(player.prizes)}")
        print("="*30 + "\n")

    def guess_letter(self, player, letter):
        if letter in self.guessed_letters:
            print("Letter has already been guessed.")
            return False
        self.guessed_letters.add(letter)
        if letter in self.phrase:
            occurrences = self.phrase.lower().count(letter)
            prize_money = 500  # Beispielwert
            player.add_money(occurrences * prize_money)
            self.obscured_phrase = ''.join([char if char.lower() in self.guessed_letters else '_' for char in self.phrase])
            print(f"Correct! The letter {letter} appears {occurrences} times.")
            return True
        else:
            print(f"The letter {letter} is not in the phrase.")
            return False

    def guess_phrase(self, player, guess):
        if guess.lower() == self.phrase.lower():
            self.obscured_phrase = self.phrase
            print(f"{player.name} has guessed the phrase correctly!")
            return True
        else:
            print(f"{player.name}'s guess is incorrect.")
            return False

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self):
        wheel = Wheel()
        while '_' in self.obscured_phrase:
            self.display_game_state()
            current_player = self.players[self.current_player_index]
            print(f"{current_player.name}'s turn:")
            spin_result = wheel.spin()
            print(f"Wheel landed on: {spin_result}")
            if spin_result == "Lose a turn":
                print(f"{current_player.name} loses a turn.")
                self.next_turn()
            elif spin_result == "Bankrupt":
                print(f"{current_player.name} goes bankrupt!")
                current_player.money = 0
                self.next_turn()
            else:
                print(f"{current_player.name} can guess a letter.")
                correct_guess = current_player.take_turn(self)
                if not correct_guess:
                    self.next_turn()
                time.sleep(2)
        print("Game over! The phrase was:", self.phrase)
        self.display_game_state()

# Spiel starten
if __name__ == "__main__":
    players = [HumanPlayer("Alice"), ComputerPlayer("Bot1"), ComputerPlayer("Bot2")]
    game = Game("Artist & Song", "Whitney Houston’s I Will Always Love You", players)
    game.play()


#test again.


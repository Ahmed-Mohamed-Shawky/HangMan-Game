import random
import string

hangman_words = {
        "Animals": ["Lion", "Elephant", "Kangaroo", "Penguin", "Dolphin", "Giraffe", "Alligator", "Cheetah", "Octopus", "Platypus", 
                    "Zebra", "Rhinoceros", "Hippopotamus", "Koala", "Chimpanzee", "Crocodile", "Jaguar", "Leopard", "Meerkat", "Panda"],
        
        "Fruits": ["Apple", "Banana", "Strawberry", "Pineapple", "Watermelon", "Grapes", "Kiwi", "Mango", "Blueberry", "Raspberry",
                   "Peach", "Cherry", "Papaya", "Pomegranate", "Coconut", "Dragonfruit", "Grapefruit", "Lemon", "Lychee", "Fig"],
        
        "Countries": ["Australia", "Brazil", "Canada", "Denmark", "Egypt", "France", "Germany", "Hungary", "India", "Japan",
                      "Italy", "Norway", "Mexico", "Nigeria", "Peru", "Russia", "Singapore", "Turkey", "Vietnam", "Zimbabwe"],
        
        "Sports": ["Football", "Basketball", "Cricket", "Tennis", "Baseball", "Hockey", "Rugby", "Badminton", "Golf", "Volleyball",
                   "Swimming", "Cycling", "Boxing", "Wrestling", "Skating", "Surfing", "Archery", "Judo", "Karate", "Gymnastics"],
        
        "Movies": ["Inception", "Titanic", "Avatar", "Gladiator", "Interstellar", "Matrix", "Jaws", "Casablanca", "Godfather", "Joker",
                   "Frozen", "Avengers", "HarryPotter", "StarWars", "JurassicPark", "ShawshankRedemption", "PulpFiction", "Rocky", "Alien", "ToyStory"],
        
        "Colors": ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Violet", "Indigo", "Cyan", "Magenta",
                   "Turquoise", "Maroon", "Amber", "Aquamarine", "Lavender", "Crimson", "Teal", "Olive", "Beige", "Fuchsia"],
        
        "Vehicles": ["Bicycle", "Airplane", "Helicopter", "Scooter", "Motorcycle", "Yacht", "Submarine", "Tractor", "Convertible", "Limousine",
                     "Truck", "Bus", "Van", "Train", "Ambulance", "Firetruck", "Taxi", "Bulldozer", "CruiseShip", "Spaceship"],
        
        "Jobs": ["Doctor", "Engineer", "Architect", "Teacher", "Lawyer", "Pilot", "Chef", "Scientist", "Firefighter", "Plumber",
                 "Nurse", "Dentist", "Pharmacist", "Carpenter", "Electrician", "Mechanic", "PoliceOfficer", "Artist", "Journalist", "Accountant"],
        
        "Famous Landmarks": ["Eiffel", "Pyramids", "Colosseum", "TajMahal", "BigBen", "StatueofLiberty", "GreatWall", "MountRushmore", "SydneyOpera", "LeaningTower",
                             "GoldenGateBridge", "Stonehenge", "ChristtheRedeemer", "MachuPicchu", "Acropolis", "Petra", "BurjKhalifa", "MountFuji", "NiagaraFalls", "Versailles"],
        
        "Technology": ["Smartphone", "Computer", "Internet", "Robotics", "AI", "Blockchain", "Database", "Algorithm", "Encryption", "Quantum",
                       "VirtualReality", "3DPrinting", "Nanotechnology", "Microchip", "Semiconductor", "Satellite", "Sensor", "Cybersecurity", "Wearable", "Drone"]
    }

class HangMan:

    def __init__(self,word_to_guess):
        self.faild_attempts = 0
        self.word_to_guess = word_to_guess.lower()
        self.game_progress = [ "-" for ch in word_to_guess ]
        self.hangedman = [
                        '________',
                        '|      | ',
                        '|      O ',
                        '|      | ',
                        '|     /|\ ',
                        '|      | ',
                        '|     / \ ',]
    
    def _find_Indexes(self,letter):
        indexes = [ index for index in range(len(self.word_to_guess)) if(self.word_to_guess[index]==letter) ]
        return indexes
    
    def _is_invalid_letter(self,letter):
        if(letter in string.ascii_letters):
            return False
        else:
            return True
    
    def _game_status(self):
        str = ' '.join(self.game_progress)
        print("The word is: "+str)
        if (self.faild_attempts):
            for attempt in range(self.faild_attempts):
                print(self.hangedman[attempt])
    
    def _update_progress(self,letter,indexes):
        for index in indexes:
            self.game_progress[index] = letter
            
    def _user_input(self):
        input_letter = input("what's the letter u think about :> :- ")
        if(self._is_invalid_letter(input_letter)):
            return False
        else:
            return input_letter
            
    def play(self):
        while(self.faild_attempts<7):
            print("==============================================================")
            self._game_status()
            while(True):
                letter = self._user_input()
                if(letter):
                    break
            indexes = self._find_Indexes(letter)
            if(len(indexes)):
                print(random.choice(["Well done","Nice jop","Nice one"]))
                self._update_progress(letter,indexes)
            else:
                print(random.choice(["Bamoooot Ya Fa5ryyy","Oh Noo","Yaaa3aaammm"]))
                self.faild_attempts+=1
            dash_number = 0
            for ch in self.game_progress:
                if(ch=="-"):
                    dash_number+=1
            if(dash_number==0):
                print("OMG u r just right :D the ward is: '"+ self.word_to_guess + "'")
                print("Grrraaaatttzzzzzzzz..... u just won aginst a machine -_-")
                break
        if(self.faild_attempts>=7):
            self._game_status()
            print("LooL... the machine just beated u @_@") 
            print("The Word was: '"+ self.word_to_guess + "'")
            




exit_play = False
while (not exit_play):    
    counter = 0;
    print()
    for category in hangman_words.keys():
        counter = counter+1
        print(f"{counter}-{category}", end =" ")
    print("\n")
    #print(self.__hangman_words.keys())
    while True:
        input_category_ID = int(input(f"Choose Category from 1 to {len(hangman_words)}:- "))
        if (input_category_ID in range(1,len(hangman_words))):
            break
    category = list(hangman_words.keys())[input_category_ID-1]
    print(f"--------------{category}--------------")
    
    
    Hang_Man = HangMan(random.choice(hangman_words[category]))
    Hang_Man.play()
    if((input("Do u want To play again (Y/N): ") in ("N","n"))):
        exit_play = True
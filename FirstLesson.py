



import time, os

class Warrior:
    def __init__(self, nickname):
        self.nickname = nickname
        self.health = 100
        self.gold = 0        
    
    def display_status(self):
        print(f"{self.nickname} - health: {self.health} - gold: {self.gold}")

    def battle_monster(self):
        self.health -= 10
        self.gold += 1 

            

    def store(self):
        print("[1] 1 gold 20 health")
        print("[2] 4 gold 100 health")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Yanlis secim")
        if choice == 1:
            if self.gold > 0: 
                self.gold -= 1
                self.health += 20
                print("Can +20 alındı (-1 gold)")
            else:
                print(f"Yeterince gold yoxdur. Balance: {self.gold}")
        elif choice == 2:
            if self.gold >= 4:
                self.gold -=4
                self.health = 100
                print("Can 100 alındı (-4 gold)") 
        
            
                
                    
            else:
                print(f"Yeterince gold yoxdur. Balance: {self.gold}")
        else:
            print("Yanlis secim")


class InvalidNameException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

isPlay = True
isMenu = True

print("Welcome to Battle Monsters!")
while isPlay:
    time.sleep(1)
    nickname = input("Enter nickname for warrior: ")
    try: 
        if not nickname.isalpha():
            raise InvalidNameException("Invalid nickname. Please at least 1 alphabetic character.")
        isMenu = True
    except InvalidNameException as e:
        print(e)
        isMenu = False
        time.sleep(2)
        os.system('cls')

    warrior = Warrior(nickname)

    while isMenu:
        print("[1] Display status")
        print("[2] Fight with Monsters")
        print("[3] Store")
        print("[4] Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            warrior.display_status()
        elif choice == 2:
            if warrior.health == 0:
                print("Canin 0 dir Store dan Can All!!")
            else:
              warrior.battle_monster()
    
            
        elif choice == 3:
            warrior.store()
        elif choice == 4:
            isPlay = False
            exit()
        else:
            print("Sehv secim")
        time.sleep(3)
        os.system('cls')


class Book:
    pass

class BookNotFoundException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

try:
    raise BookNotFoundException("Book not found!")
except BookNotFoundException as e:
    print(e)


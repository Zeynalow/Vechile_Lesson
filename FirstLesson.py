

# class Student:
#     def __init__(self, name, surname , age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.grade = 77
        
# name = input("Aadinizi Daxil Edin: ")
# surname = input("Soyadinizi Daxil Edin: ")
# age = int(input("Yasinizi daxil edin: "))
        

# student = Student(name,surname,age)
# print(student.name)
# print(student.surname)
# print(student.age)
# print(student.grade)

# class Book:
#     def __init__(self,title,genre,author,page_count):
#         self.title = title
#         self.genre = genre
#         self.author = author
#         self.page_count = page_count
# title = input("Kitabin Adini Daxil Edin:")
# genere = input("Kitabin Janrini Daxil edin:")
# author = input("Kitabin Muelifini Daxil Edin:")
# page_count = input("Kitabin Sehifesini Daxil edin: ")


# book = Book(title,genere, author, page_count)
# print(book.title)
# print(book.genre)
# print(book.author)
# print(book.page_count)



# class Dog:
#     def __init__(self, nickname,age):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         print(f"{self.nickname} - Barkk!!")
# class Cat:
#     def __init__(self , nickname, age):
#         self.nickname = nickname
#         self.age = age
#     def make_sound(self):
#         print(f"{self.nickname} - Meooww!")
# dog = Dog("Dog1",1)
# cat1 = Cat("Cat1",1)
# cat2 = Cat("Cat2" , 1)

# class Zoopark:
#     def __init__(self,title):
#         self.title = title
#         self.animals = []
#     def add_animal(self,animal):
#         self.animals.append(animal)
#         print(f"{animal} - Zooparka elave edildi")
#     def delete_animal(self):
#        self.animals.pop()
#        print("Silindi")


# zoo = Zoopark("Baki Zooparki")
# zoo.add_animal("Aslan")
# zoo.add_animal("AYI")
# zoo.add_animal("Fil")


# zoo.delete_animal()  
# zoo.delete_animal()  
# print(zoo.animals)


# class Book:
#     pass
# class BookNotFoundException(Exception):
#     def __init__(self, *args):
#         super().__init__(*args)
# try:
#     raise BookNotFoundException("Book not found!")
# except BookNotFoundException as e:
#     print(e)


#----------------------------------------------------



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


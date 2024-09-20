# bibliotek övning del 3

from abc import ABC, abstractmethod

class Item(ABC): # item är en abstrakt klass
    def __init__ (self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    @abstractmethod #abstrakt metod som måste implementeras i subklasser
    def display_info(self):
        pass

class Book(Item): #subklass Book som ärver från Item
    def __init__ (self, title, author, year, pages):
        super().__init__(title, author, year) #anropar konstruktorn i Item
        self.pages = pages #ett nytt attribut
        
    def display_info(self): #implementerar den abstrakta metoden display_info
        return f"Book: {self.title}, Author: {self.author}, Year: {self.year}, Pages: {self.pages}"
      
class Magazine(Item): #subklass Magazine som ärver från Item
    def __init__ (self, title, author, year, issue):
        super().__init__(title, author, year)
        self.issue = issue
    
    def display_info(self): #implementerar den abstrakta metoden display_info
        return f"Magazine: {self.title}, Author: {self.author}, Year: {self.year}, Issue: {self.issue}"
    
class LibraryUser: # klass för låntagaren
    def __init__ (self, name):
        self.name = name # namn på låntagaren
        self.borrowed_items = [] #en tom lista för att lagra lånade objekt
    
    def borrow(self, item): #metod för att låna ett objekt
        self.borrowed_items.append(item) #lägg till
    
    def return_item(self, item): #metod för att returnera ett objekt
        if item in self.borrowed_items:
            self.borrowed_items.remove(item) # ta bort
            
    def list_borrowed_items(self): #metod för att visa alla lånade objekt
        if self.borrowed_items:
            print(f"{self.name} has borrowed the following items:")
            for item in self.borrowed_items:
                print(item.display_info())
        else:
            print(f"{self.name} has not borrowed any items.")

class Library: # biblioteksklass
    def __init__ (self):
        self.items = [] # en tom lista för att lagra alla objekten
        self.users = [] # en tom lista för att lagra alla låntagare
        
    def add_item(self, item): # metod för att lägga till ett nytt objekt
        self.items.append(item)
    
    def remove_item(self, item): # metod för att ta bort ett objekt
        if item in self.items:
            self.items.remove(item)
    
    def register_user(self, user): # metod för att registrera en ny låntagare
        self.users.append(user)
    
    def borrow_item(self, user, item): # metod för att låna ett objekt
        if item in self.items and item not in [i for u in self.users for i in u.borrowed_items]:
            user.borrow(item)
        else:
            print(f"The Objekt '{item.title}' is probobly not available or already lent by someone else.")
            
    def return_item(self, user, item): # metod för att returnera ett objekt
        user.return_item(item)
    
    def list_items(self): # metod för att visa alla objekt
        for item in self.items:
            print(item.display_info())
    
    def list_available_items(self): # metod för att visa tillgängliga objekt
        borrowed_items = [i for u in self.users for i in u.borrowed_items] # samlarar alla lånade items i en lista
        available_items = [item for item in self.items if item not in borrowed_items] # filtrerar bort lånade objekt
        for item in available_items:
            print(item.display_info()) # visar tillgängliga items

    def summary_of_borrowed_items(self): # metod för att visa sammanfattning av lånade objekt
        for user in self.users:
            if user.borrowed_items:
                print(f"{user.name} has borrowed:")
                for item in user.borrowed_items:
                    print(f" - {item.display_info()}")
                    

book1 = Book("python in the Library", "Olle johansson", 2023, 311)
book2 = Book("c# a viewpoint", "Eva Skoog", 2010, 253)
book3 = Book("Java eller inte", "Philip Rutger", 2004, 194) 
mag1 = Magazine("Pc for all", "Jane borg", 2024, "January")
mag2 = Magazine("Home cleaners", "Lina Turesson", 2022, "March")

library = Library()

library.add_item(book1)
library.add_item(book2)
library.add_item(book3)
library.add_item(mag1)
library.add_item(mag2)

user1 = LibraryUser("Göran")
user2 = LibraryUser("Bodil")
user3 = LibraryUser("Peter")
    
library.register_user(user1)
library.register_user(user2)
library.register_user(user3)

library.borrow_item(user1, book1)
library.borrow_item(user2, mag1)
library.borrow_item(user3, book2)

print("\nAvailable items in the library:")
library.list_available_items()

print("\nSummary of borrowed items:")
library.summary_of_borrowed_items()

print(f"\nItems borrowed by {user1.name}:")
user1.list_borrowed_items()
    
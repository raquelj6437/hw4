class Person():
    numMade = 0

    def __init__(self, name=None, gender=None, age=None):
        self.name = name
        self.gender = gender
        self.age = age
        self.friends = ''
        # current collection of books owned
        self.books_collections = ''
        self.books_cart = ''
        self.wish_list = ''
        self.currentState = ""
        Person.numMade = Person.numMade + 1

    def getID(self): return self.ID

    def setName(self, name): self.name = name

    def getName(self): return self.name

    def setAge(self, age): self.age = age

    def getAge(self): return self.age

    def getFriends(self): return self.friends

    def getBooks_Collections(self): return self.books_collections

    def getBooks_Cart(self): return self.books_cart

    def getWishList(self): return self.wish_list

    def expressState(self):
        self.currentState = " "  # ensures that the current state is reset before updating
        self.currentState += "Person " + selfname + "_(" + str(self.ID) + "),"
        self.currentState += "is" + self.age + " years old, and has these books"
        self.currentState += " :" + str(self.books_collections)
        self.currentState += "Person " + selfname + \
            "previously had these books: " + str(self.books_history)

    def printState(self):
        self.expressState()
        print(self.currentState)

    def person_kind(self):
        if self.gender[0] == 'm':
            return 'male'
        elif self.gender[0] == 'f':
            return 'female'
        else:
            return 'alien'

    def borrow(self, amount): self.books_collections += amount

    def loan(self, amount): self.books_collections -= amount

    def introduce_person(self): print(str(
        self.name + "(_" + str(self.ID) + ")" + "I am" + str(self.age) + "years old."))

from List import List


class Books():
    numMade = 0

    def __init__(self, data=None, title=None, author=None, subject=None, edition=None, annotations=None, location=None):
        self.data = data
        self.title = title
        self.author = author
        self.subject = subject
        self.edition = edition
        self.annotations = annotations
        self.location = location
        self.ID = Books.numMade
        Books.numMade += 1

        self.available = []
        self.loaned = []
        self.title = []

    def __str__(self):
        return str(self.data)

    def getID(self): return self.ID

    def setData(self, data): self.data = data

    def getData(self): return self.data

    def setTitle(self, title): self.title = title

    def getTitle(self): return self.data

    def setAuthor(self, author): self.author = author

    def getAuthor(self): return self.author

    def setSubject(self, subject): self.subject = subject

    def getSubject(self): return self.subject

    def setEdition(self, edition): self.edition = edition

    def getEdition(self): return self.subject

    def setAnnotations(self, annotations): self.annotations = annotations

    def getAnnotations(self): return self.annotations

    def setLocation(self, annotations): self.location = location

    def getLocation(self): return self.location

    def getAvailable(self): return self.available

    def getLoanedBooks(self): return self.loaned

    def getBooks(self): return self.bookList

    def hasTitle(self): return self.title != None

    def hasAuthor(self): return self.author != None

    def hasSubject(self): return self.subject != None

    def hasEdition(self): return self.edition != None

    def hasAnnotations(self): return self.annotations != None

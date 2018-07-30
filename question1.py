from Person import Person
from Books import Books
from List import List
from Node import node

b = Books()

red = Books('hi')
orange = Books('bye')
purple = Books('purple')
green = Books('green')

b.available.append(red)
b.available.append(orange)
b.available.append(purple)
b.available.append(green)

doug = Person('Douglas')
jerry = Person('Joseph')
ralph = Person('Ralphy')

doug.friends.append(jerry)
doug.friends.append(ralph)

jerry.books_cart.append(red)
b.available.remove('hi')

doug.books_cart.append(red)

jerry.books_cart.print_front()
doug.books_cart.print_front()

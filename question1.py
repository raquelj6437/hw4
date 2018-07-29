from Person import Person
from Books import Books
from List import List
from Node import node

p = Person()
b = Books()

red = Books('hi', 'jonny', 'color', '3', 'yes')
orange = Books('bye')
purple = Books('purple')
green = Books('green')

red_node = node(red)
orange_node = node(orange)
purple_node = node(purple)
green_node = node(green)

b.available.append(red_node)
b.available.append(orange_node)
b.available.append(purple_node)
b.available.append(green_node)

print(str(b.available.showTree()))
print(str(b.loaned.showTree()))
print(red_node.data)
# b.available.print_back()

# print(b.available.startFind('hi'))

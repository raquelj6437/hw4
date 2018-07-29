from Person import Person
from Books import Books
from List import List
from Node import node

p = Person()
b = Books()

red = Books('hi')
orange = Books('bye')
purple = Books('purple')
green = Books('green')

red_node = node(red)
orange_node = node(orange)
purple_node = node(purple)
green_node = node(green)

available = List('available')

available.append(red_node)
available.append(orange_node)
available.append(purple_node)
available.append(green_node)

# available.print_back()
# available.print_front()

# print(purple_node.prev)
# print(available.name)
# print(available.data)
print(available.showTree())
print(node().get_data())
print(b.available)
# print(available.isEmpty())

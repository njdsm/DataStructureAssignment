from sweepstakes import Sweepstakes
from family import Family
from linked_list import LinkedList
from binary_tree import Binary_Tree

months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
# pi is 3.14, so third index is month with pi day
print(months[2])

birthday_locations = {"Arcade", "Park", "Skate West"}
for i in birthday_locations:
    print(i)

sweepstakes = Sweepstakes()
sweepstakes.add_contestant("Nate", "Johnson")
sweepstakes.add_contestant("Paige", "Johnson")
sweepstakes.add_contestant("Mason", "Johnson")

sweepstakes.get_winner()

family = Family()
family.add_member("Nate", "Johnson", "Me")
family.add_member("Paige", "Johnson", "Wife")
print(family.members)

linked_list = LinkedList()
linked_list.append_node(5)
linked_list.append_node(30)
linked_list.append_node(65)
linked_list.add_to_beginning(1)
linked_list.add_to_beginning(3)

print(linked_list.contains_node(linked_list.head, 65))
print(linked_list.contains_node(linked_list.head, 64))

new_tree = Binary_Tree(50)
new_tree.add_node(75, new_tree)
new_tree.add_node(25, new_tree)
new_tree.add_node(80, new_tree)
new_tree.add_node(79, new_tree)
print(new_tree.search_for_node(80, new_tree))
print(new_tree.search_for_node(234, new_tree))
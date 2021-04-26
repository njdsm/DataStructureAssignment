from sweepstakes import Sweepstakes
from family import Family
from linked_list import LinkedList

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
print(family.members)

linked_list = LinkedList()
linked_list.append_node(5)
linked_list.append_node(30)
linked_list.append_node(65)
linked_list.add_to_beginning(1)
linked_list.add_to_beginning(3)

print(linked_list.contains_node(linked_list.head, 65))
print(linked_list.contains_node(linked_list.head, 64))


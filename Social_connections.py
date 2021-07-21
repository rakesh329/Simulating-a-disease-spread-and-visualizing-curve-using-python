"""
Written by : Rakesh Namballa
Started date : 23/05/2020
Last edited: 08/06/2020
Description: " Representing social connections "
In this code we create objects for all the people and add friends to each person depending on the sample txt file.
Sample file consist of all the Person names along with their respective friends.

"""


class Person:
    def __init__(self, first_name, last_name):
        self.friend_list = []  # List for all the friends
        self.first_name = first_name
        self.last_name = last_name

    def add_friend(self, friend_person):
        self.friend_list.append(friend_person)

    def get_name(self):
        return str(self.first_name + " " + self.last_name)  # Concatenating first name and last name

    def get_friends(self):
        return self.friend_list


def load_people():
    all_personObjects = {}  # Each person name and object address stored as a Key:Value pairs.
    all_lines = []
    f = open("sample_set.txt", 'r')  # Open the file and read each line.
    for line in f:
        line = line.rstrip()  # Removes the /n tag from each line
        all_lines.append(line)  # Append each line into a list(all_lines)
        person_name = line.split(": ")  # Separate the Person with friends
        person = Person(person_name[0].split(" ")[0], person_name[0].split(" ")[1])  # Splits the first and last name
        all_personObjects[person_name[0]] = person  # Person is added into the dictionary along with object address

    f.close()

    for line in all_lines:
        person_name = line.split(": ")  # Separate the fiends with person
        friend_name = person_name[1].split(", ")  # Separate all the friends
        for friend in friend_name:
            all_personObjects[person_name[0]].add_friend(all_personObjects[friend])  # Add friend object to person

    return list(all_personObjects.values())  # return list of all Person objects  from the file records


if __name__ == '__main__':
    load_people()

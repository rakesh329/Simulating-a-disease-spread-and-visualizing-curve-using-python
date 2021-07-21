"""
Written by : Rakesh Namballa
Started date : 26/05/2020
Last edited: 08/06/2020
Description: "  Simulate disease spread "
In this code we create objects for all the patients and add friends to each person depending on the sample txt file.
We run a simulation to check the no:of effected people and return a count for each day.
"""
import random

from Social_connections import Person


class Patient(Person):
    def __init__(self, first_name, last_name, health):
        super().__init__(first_name, last_name)
        self.friend_list = []
        self.first_name = first_name
        self.last_name = last_name
        self.health = set_health_boundary(health)  # Initial starting  person’s health point values

    def get_health(self):
        return round(self.health)  # Returns the patient’s current health points

    def set_health(self, new_health):
        self.health = set_health_boundary(round(new_health))  # Changes health points

    def is_contagious(self):
        if self.health < 50:
            return True
        else:
            return False

    def infect(self, viral_load):
        if self.health <= 29:
            self.health = set_health_boundary(round(self.health - (0.1 * viral_load)))
            return
        elif self.health < 50:
            self.health = set_health_boundary(round(self.health - (1.0 * viral_load)))
            return
        elif self.health >= 50:
            self.health = set_health_boundary(round(self.health - (2.0 * viral_load)))
            return

    def sleep(self):
        self.health = set_health_boundary(self.health + 5)  # Add 5 heath points after sleep


def set_health_boundary(value):  # Method to set the min and max health points
    if value <= 0:
        return 0
    elif value >= 100:
        return 100
    else:
        return value


def run_simulation(days, meeting_probability, patient_zero_health):
    all_PatientObjects = load_patients(75)  # Set all the patients with initial health by calling load_patient()
    all_PatientObjects[0].set_health(patient_zero_health)  # Specify the zero patient health

    events = ["meet", "don'tmeet"]  # List for the use in random.choices()
    not_meeting_probability = round(1 - meeting_probability, 2)
    day_count = []
    for i in range(0, days):
        for patient in all_PatientObjects:
            for friend in patient.get_friends():  # Gets all the friend for that patient object
                # random.choices() returns a list with randomly selected from the specified sequence
                toMeet = random.choices(events, weights=[meeting_probability, not_meeting_probability])[0]
                if toMeet == "meet":
                    # Checks if both patient and meeting friend are contagious
                    if friend.is_contagious() and patient.is_contagious():
                        friend_health = friend.get_health()
                        #   from given viral load formula
                        friend_viral_load = (((friend_health - 25) * (friend_health - 25)) / 62) + 5
                        person_health = patient.get_health()
                        person_viral_load = (((person_health - 25) * (person_health - 25)) / 62) + 5
                        friend.infect(person_viral_load)
                        patient.infect(friend_viral_load)
                    # Enter the condition if only friend is contagious
                    elif friend.is_contagious():
                        friend_health = friend.get_health()
                        friend_viral_load = (((friend_health - 25) * (friend_health - 25)) / 62) + 5
                        patient.infect(friend_viral_load)
                    # Enter the condition if only patient is contagious
                    elif patient.is_contagious():
                        person_health = patient.get_health()
                        person_viral_load = (((person_health - 25) * (person_health - 25)) / 62) + 5
                        friend.infect(person_viral_load)

        count = 0
        for patient in all_PatientObjects:
            if patient.is_contagious():
                count = count + 1  # count for no:of infected patients each day
            patient.sleep()
        day_count.append(count)
    return day_count  # return the list of day_count


def load_patients(initial_health):
    all_PatientObjects = {}  # Each patient name and object address stored as a Key:Value pairs.
    all_lines = []
    f = open("a2_sample_set.txt", 'r')  # Open the file and read each line.
    for line in f:
        line = line.rstrip()  # Removes the /n tag from each line
        all_lines.append(line)  # Append each line into a list
        patient_name = line.split(": ")  # Separate the patient with friends
        patient = Patient(patient_name[0].split(" ")[0], patient_name[0].split(" ")[1], initial_health)
        all_PatientObjects[patient_name[0]] = patient  # Patient is added into the dictionary along with object address

    f.close()

    for line in all_lines:
        patient_name = line.split(": ")  # Separate the fiends with patient
        friend_names = patient_name[1].split(", ")  # Separate all the friends
        for friend in friend_names:
            all_PatientObjects[patient_name[0]].add_friend(all_PatientObjects[friend])

    return list(all_PatientObjects.values())  # return list of all Patient objects  from the file records


if __name__ == '__main__':
    run_simulation(40, 1, 1)

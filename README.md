## Simulating-a-disease-spread-and-visualizing-curve-using-python

This project is to create the necessary data structure to simulate social links and disease transmission
between people, simulate infections among the population over a period of time, and plot graphs to determine
whether an outbreak is contained or not.

We surveyed 200 fake people, all with unique names, and asked them to provide the names of their friends in the
group who they are in regular contact with. You may assume that each person has specified at least one friend, and
each of the person’s friends has also named that person as a friend. All the details are present on the sample_set.txt.

The data file consists of 200 records. Each record is recorded on its own line in the file, and consists of a person’s
name, together with all the names of that person’s friends. The real file is 200 lines long, but to illustrate the file
format, just the first two lines of the file are shown here as a sample:
> Gill Bates: Jodee Killam, Natacha Osterhoudt, Jom Tones, Verdie Tong, Ossie Digangi
; Jom Tones: Marry Blakely, Masako Miguel, Gill Bates

**Text file Explaination:**

- The first line in the file is the record for Gill Bates. Gill Bates has named the following people as her social
connections: Jodee Killam, Natacha Osterhoudt, Jom Tones, Verdie Tong, and Ossie Digangi. This means that
if Gill Bates is contagious (able to spread the virus), Gill Bates may infect the people she has named, and if
her friends are contagious, they may infect Gill Bates.

- On the next line, Jom Tones has named his friends in a similar way, and so on.
- Note that Gill Bates has named Jom Tones as one of her friends. This means that Jom Tones must also name
Gill Bates as one of his friends. It’s not unusual that may both visit each other, and the virus may travel from
either person to the other. You can assume that this rule is followed for all records in the file.

## How the virus spreads

**Health of each person**

Each person has a number of health points which changes over time depending on a person’s health.
The number of health points is used to check if a patient is contagious (i.e. able to infect other people) or not:


>| Health Points | |Description |
| -------------- | ----------- |
| 76-100 | |Perfect Health, Not contagious|
| 75 || Average Health, Not contagious |
| 50-74 || Fair Health, Not contagious |
| 30-49 || **contagious** |
| 0-49 || Poor Health, **contagious** |

When sleeping after each day, each person’s immune system will naturally add 5 health points to that person, up to
a maximum of 100 health points.

**Meeting probability**

Each day, a person may or may not visit another person for a meeting. For each person, the probability that they will
travel to visit one of their friends depends on social distancing regulations. A single meeting probability parameter
will be applied to all people in the group to determine the effect of a certain level of social distancing. This
probability is a fraction of 1. 
- For example, running the simulation with a meeting probability of 1.0 means that every
day, every person will leave home to visit all of their friends, and all their friends will also travel to visit them during
the same day. A probability of 0.0 means nobody can leave home to visit anyone else, and a probability of 0.333
means there is a 33.3% random chance of each visit happening.

**Viral load**

The virus spreads when a contagious person2 passes a viral load to a person they are visiting, or a person who has
visited them. The term ‘viral load’ is a measure of the quantity of virus in the air which the other person breathes in
when they are visiting and/or being visited by any contagious person. A person can be affected by a viral load even if
they are already partly sick.

**Effect of infection**

When a contagious person produces a viral load, every person they meet when visiting (or being visited) will be
infected by their viral load. If the viral load is small, or a person is healthy, the person who is infected might not
become sick, and they will quickly recover their health later when they sleep.


## Program Explaination

Complete projects is done in three different python files:
1. Social_connections.py
2. Simulate_disease_spread.py
3. Visualise_curve.py

**1. Social_connections.py**

In this code we create objects for all the people and add friends to each person depending on the sample txt file.
Sample file consist of all the Person names along with their respective friends.

**Person class**
Create a Python program that defines a Person class with the following methods.:
- **__init__(first_name, last_name):**
Constructor method to create a new Person object.
where first_name and last_name are strings containing the person’s name
- **add_friend(friend_person):**
This method should add a new social connection to be stored in this Person object.
friend_person is a reference to another Person object.
- **get_name():**
This method returns a string containing the person’s first and last name concatenated together;
e.g. “Jom Tones”
- **get_friends():**
This method returns a list of Person objects for the social connections that have been added.

The purpose of the Person class is to represent a person who is linked to other people by social connections. The
above description specifies what methods and form the Person class required to have, but not how to code them.
Therefore each Person object must be able to store a set of references to other Person objects. (You will need to
think about a suitable data type for storing a set of objects, and how you would need to initialize the empty set
within the class definition.) In addition to storing the person’s friends, your Person class should also contain
instance variables to keep track of the person’s name.

**2. Simulate_disease_spread.py**

In this code we create objects for all the patients and add friends to each person depending on the sample txt file.
We run a simulation to check the no:of effected people and return a count for each day. This is the most important part in the 
project as this code contins all the calculation that checks wheather the person is contagious or not.

**Patient class (a subclass of Person)**

The Person class you defined in Social_connections.py is fine for mapping social connections, but it does not contain appropriate
methods for simulating disease spread or health of the people in our group.
Before you move to writing the simulation, define a Patient class which inherits the methods of
the Person class through inheritance. Your Patient class should add the following methods:
- **__init__(first_name, last_name, health):**
Constructor method to create a new Patient object by inheriting from the Person class.
where first_name and last_name are strings containing the person’s name and health is the initial starting value of the person’s health points.
- **get_health():**
This method returns the patient’s current health points.
- **set_health(new_health):**
This method changes the patient’s current health points directly.
- **is_contagious():**
This method should return a Boolean result of True if the person’s health points are in the range of
being contagious able to spread disease. It should return False if the
person is not currently contagious.
- **infect(viral_load):**
This method infects the Patient object with a viral load. It causes the patient to receive the viral
load specified in the method’s argument given as a floating point number.
After receiving a viral load, the person may or may not become sick enough to be contagious.
Calling this method should adjust the person’s health points according to the rules defined in section
Note that the person’s health cannot go below 0.
- **sleep():**
Calling this method causes the person to recover some health points one night’s sleep.


**load_patients function ()**

You will also need to write a slightly different version of the function you wrote to load data from the file, since we
really need a list of Patient objects, not a list of Person objects. Write a function named
load_patients(default_health) which does the following: 
1. Reads from the file sample_set.txt.
2. Creates a new Patient object for each record (line) in the file, which contains the name of the person
represented by that record. For each Patient object created, you should assign the health value given by
the default_health argument, since the initial health of each person is not listed in the file.
3. Where a person’s record indicates that they have friends, you should use the inherited add_friend
method to add each friend to that Person object.
4. Finally, return a list of all the Patient objects that have been created from the file records.
In other words, this function should do the same thing as load_people, except that it should create Patient
objects (with a specified default health value) instead of Person objects.


**run_simulation function – implement the simulation logic**

Now implement a run_simulation(days, meeting_probability, patient_zero_health) function
which should implement the following behaviour:
1. Take in the following arguments:
- days: the integer number of days the simulation should run for.
- meeting_probability: the fractional probability that any person may visit a certain friend on
a certain day. 0.0 means 0% chance, 1.0 means 100% chance. (This was explained in section 2.)
- patient_zero_health: the initial health of the first person in the file. (See below.) If the
(rounded) initial health is less than or equal to 49, this person is contagious and there may be
the chance of a disease outbreak.
2. Use your load_patients function to load patient data from the disk. The first patient in the returned
list (who we will call ‘patient zero’) should be given the starting health value specified in the
patient_zero_health argument. The remaining patients should be given an initial health value of
75, which is the average health of the population from section 2.
3. Run through each day of the simulation. For each day, do the following:
- For each patient in the group, look at each of the person’s friends, and randomize whether the
person should meet that friend today. 7 The probability for this to happen is given by the
meeting_probability argument. If the meeting takes place, each person in that pair who is
contagious8 should spread a viral load to the other person, by calling the infect() method on
the other person. You will need to calculate what viral load to infect each friend with according
to the rules in section 2.
- After all meetings have completed for the day, check how many people are now contagious in
the simulation.

- After the end of each day, all people should sleep() to recover some health.
4. Finally, the function should return a list with the daily number of contagious cases through the duration
of the simulation. For example, if your simulation runs for 30 days, the list should
contain 30 integers containing the number of people who were contagious at the end of each day, from
the first day of the simulation (element [0]) to the last day of the simulation.

**3. Visualise_curve.py**

**visual_curve function**

Write a function named visual_curve(days, meeting_probability, patient_zero_health) which runs
the simulation using the specified arguments, and then does the following:
1. Runs the simulation by calling the run_simulation function with the specified arguments for days,
meeting_probability, patient_zero_health.
2. After the simulation is complete, prints the whole daily list of contagious patient counts from the returned
data.
3. Then, using functionality from either the matplotlib or pandas library, plot a curve showing the daily
number of contagious patients over the number of days of the simulation. The days of the simulation should
be on the X axis and the contagious patient count on the Y axis. Your graph should have the X and Y axis
labelled accordingly.

> The output diagrams are provided for different senarious




















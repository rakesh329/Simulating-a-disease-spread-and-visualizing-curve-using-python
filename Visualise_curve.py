"""
Written by : Rakesh Namballa 
Started date : 23/05/2020
Last edited: 08/06/2020
Description: "  Visualise the curve "
In this code we create a count vs days graph and visualise the graph
"""
"""
Test scenario A: An uncontained outbreak 
Number of days: 30
Meeting probability: 0.6  
Patient zero health: 25 health points 
In this case as the patient zero health is less he infect more viral load to the friends he meet and the probability of 
meeting is also more.
Though running through multiple case the spread for the first few days start slowly but as patients meet regularly the 
viral load gets infected to multiple people fast and at the end of 30 days all the patients are completely effected with 
virus.
------------------------------------------------------------------------------------------------------------------------
Test scenario B: an unpredictable situation 
Number of days: 60 
Meeting probability: 0.25 
Patient zero health: 49 health points 
This is an unpredictable case where the patient zero health has a mild symptoms and the meeting probability also less.
* In few cases on first day virus spreads for few people and from second day all patients gets recovers after sleep.
* In few cases it keeps on increasing and many patients gets infected.
------------------------------------------------------------------------------------------------------------------------
Test scenario C: flattening the curve 
Number of days: 90 
Meeting probability: 0.18 
Patient zero health: 40 health points 
In this cse as the meeting probability is less and the patient zero health is less effected, the increase in the virus 
is less
* In few cases the patient recovers after few days
* In few cases patients gets infected but increases slowly 
"""


from matplotlib import pyplot as plt  # import libraries  to plot a graph
from Simulate_disease_spread import run_simulation


def visual_curve(days, meeting_probability, patient_zero_health):
    data_series = run_simulation(days, meeting_probability, patient_zero_health)  # storing the list of day_count
    plt.plot(list(range(1, days + 1)), data_series)
    plt.title("Virus spread simulation")
    plt.xlabel("Days")
    plt.ylabel("Count")
    plt.show()


if __name__ == '__main__':
    # Take inputs from the user
    days = int(input("Enter number of days:"))
    meeting_probability = float(input("Enter meeting probability:"))
    patient_zero_health = int(input("Enter patient zero health:"))
    visual_curve(days, meeting_probability, patient_zero_health)


from typing import ValuesView


print("Hello World") 
counties= ["Aprapahoe", "Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


for i in range(0,len(voting_data)):
    counties=voting_data[i]["county"]
    voter=voting_data[i]["registered_voters"]
    print(f"{counties} county has {voter} registered voters")
    
import datetime as dt
now = dt.datetime.now()
print(f"The time is {now}")

#Method 2
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:


    # Print the file object.
    print(election_data)



 #Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Resources","analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:
    #write some text
    
      
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------------------\nArapahoe\nDenver\nJefferson")

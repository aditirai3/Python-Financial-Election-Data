import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

#define variables and lists
vote_count = 0
candidate_list = []
counter_khan = 0
counter_correy = 0
counter_li = 0
counter_tooley = 0

#Read the csv file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    header = next(csvreader)

#Count the total number of votes
    for row in csvreader:
        vote_count = vote_count + 1

#Returns an array with unique candidate names        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

# print(candidate_list) #Check the unique names in order to form individual counters

#Count the number of votes for each candidate
        if row[2] == "Khan":
            counter_khan = counter_khan + 1
        
        if row[2] == "Correy":
            counter_correy = counter_correy + 1

        if row[2] == "Li":
            counter_li = counter_li + 1
            
        if row[2] == "O'Tooley":
            counter_tooley = counter_tooley + 1

#Calculate individual percentages
percent_khan = round((counter_khan/vote_count)*100, 1)
percent_correy = round((counter_correy/vote_count)*100, 1)
percent_li = round((counter_li/vote_count)*100, 1)
percent_tooley = round((counter_tooley/vote_count)*100, 1)

#calculate highest vote count
highest_vote = max(percent_khan, percent_correy, percent_li, percent_tooley)

#compare vote count to candidate name
if percent_khan == highest_vote:
    winner = "Khan"
elif percent_correy == highest_vote:
    winner = "Correy"
elif percent_Li == highest_vote:
    winner = "Li"
elif percent_tooley == highest_vote:
    winner = "O'Tooley"

#Print output in terminal
output_path = os.path.join("Analysis", "election analysis.txt")

with open(output_path, 'w', newline = '') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {vote_count}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Khan: {percent_khan}% ({counter_khan})\n")
    txtfile.write(f"Correy: {percent_correy}% ({counter_correy})\n")
    txtfile.write(f"Li: {percent_li}% ({counter_li})\n")
    txtfile.write(f"O'Tooley: {percent_tooley}% ({counter_tooley})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------")

        
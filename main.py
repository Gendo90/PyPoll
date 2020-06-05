import os
import csv
import collections

#format filepath to the budget_data.csv file
election_filepath = os.path.join('.', "Resources", "election_data.csv")

#open the budget_data.csv file for reading
with open(election_filepath, 'r') as election_data:
    #convert contents of budget_data.csv file to an array
    election_arr = csv.reader(election_data, delimiter=",")

    #store header for column names and then go to next line
    header = next(election_arr)

    election_list = [(int(row[0]), row[1], row[2]) for row in election_arr]

    candidates = collections.defaultdict(int)

    for row in election_list:
        candidates[row[2]] += 1


    total_votes = sum(candidates.values())
    winner = ["N/A", 0]

    vote_breakdown = {}
    for candidate in candidates.keys():
        count = candidates[candidate]
        percentage = "{:.3%}".format(count/total_votes)
        vote_breakdown[candidate] = [percentage, count]

        #add checks to determine winner upon looping through candidates
        if(winner[1]<count):
            winner = [candidate, count]


    output_strings = []

    analysis_header = "Election Results"
    spacer_row = "-"*50
    output_strings.append(analysis_header)
    output_strings.append(spacer_row)

    vote_count = "Total votes: {}".format(total_votes)
    output_strings.append(vote_count)
    output_strings.append(spacer_row)

    for candidate in vote_breakdown.keys():
        curr_line = "{}: {} ({})".format(candidate, vote_breakdown[candidate][0], vote_breakdown[candidate][1])
        output_strings.append(curr_line)

    output_strings.append(spacer_row)

    winner_line = "Winner: {}".format(winner[0])
    output_strings.append(winner_line)

    for item in output_strings:
        print(item)

#output filepath to "analysis.txt"
output_filepath = os.path.join('.', "Analysis", "output.txt")

#open file as a variable, then write to the variable:
with open(output_filepath, "w", newline='') as output_file:
    output_writer = csv.writer(output_file, delimiter='\n')

    output_writer.writerow(output_strings)

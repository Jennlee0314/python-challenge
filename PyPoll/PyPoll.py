import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#read in csv file
with open(csvpath, newline='') as data:
    poll_data = csv.reader(data)
    print(poll_data)

Poll_header = next(poll_data)
print(f'csv_header: {Poll_header}')

#create lists to be used to store variable values at each row

vote_list1 = []
vote_list2 = []
candidate_list = []

for row in poll_data:
    vote_list1.append(1)

    if row[2] not in candidate_list:
        candidate_list.append(row[2])
        I=candidate_list.index(row[2])
        vote_list2.append(0)
        vote_list2[I] = vote_list2[I]+1

    else:
        I = candidate_list.index(row[2])
        votw_list2[I] = vote_list2[I]+1

#The total number of votes cast
    total_vote = sum(votw_list1)
#A complete list of candidates who received votes
#This code shows that there are 4 candidates

print(lien(candidate_list))

#finding statistics to be printed in election results

winner_plate = vote_list2.index(max(vote_list2))
winner = candidate_list[winner_place]
vote_share0 = round(vote_list2[0]/total_vote*100, 4)
vote_share1 = round(vote_list2[1]/total_vote*100, 4)
vote_share2 = round(vote_list2[2]/total_vote*100,4)
vote_share3 = round(vote_list2[3]/total_vote*100,4)

#Election Result


Print("Election Results")
Print("____________________________")
Print(f'{candidate_list[0]}: {vote_share0}00% ({vote_list2[0]})')
Print(f'{candidate_list[1]}: {vote_share1}00% ({vote_list2[1]})')
Print(f'{candidate_list[2]}: {vote_share2}00% ({vote_list2[2]})')
Print(f'{candidate_list[3]}: {vote_share3}00% ({vote_list2[3]})')
Print("____________________________")
print(f'Winner: {winner}')
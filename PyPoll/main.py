import os
import csv

bad_csvpath = os.path.join("Resources", "election_data.csv")
csvpath = os.path.join("Resources", "election_data.csv")



with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

#set up variables
    votes = []
    county = []
    candidates = []
    votes_Charles = []
    votes_Diana = []
    votes_Raymon = []
    totalCharlesvotes = 0
    totalDianavotes = 0
    totalRaymonvotes = 0

    

    for row in csv_reader:
        votes.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

#calculating total votes
        totalvotes = len(votes)

        
#calculating total votes for every candidates
    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            votes_Charles.append(candidates)
            totalCharlesvotes = len(votes_Charles)
            
        elif candidate == "Diana DeGette":
            votes_Diana.append(candidates)
            totalDianavotes = len(votes_Diana)
            
        else:
            votes_Raymon.append(candidates)
            totalRaymonvotes = len(votes_Raymon)

#transform total votes for each candidates in percentage
    Charlesvotes_percentage = round(((totalCharlesvotes / totalvotes)*100),3)
    Dianavotes_percentage = round(((totalDianavotes / totalvotes)*100),3)
    Raymonvotes_percentage = round(((totalRaymonvotes / totalvotes)*100),3)

#find out the winner
    if Charlesvotes_percentage > Dianavotes_percentage and Raymonvotes_percentage:
        winner = "Charles Casper Stockham"
    elif Dianavotes_percentage > Charlesvotes_percentage and Raymonvotes_percentage:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"





        






print("Election Results")
print("----------------------------")
print('Total Votes:', totalvotes)
print("----------------------------")
print("Charles Casper Stockham: ", Charlesvotes_percentage, "%", "(",totalCharlesvotes,")" )
print("Diana DeGette: ", Dianavotes_percentage, "%", "(", totalDianavotes,")")
print("Raymon Anthony Doane: ", Raymonvotes_percentage, "%", "(",totalRaymonvotes,")")
print("----------------------------")
print("Winner: ", winner )


f = open("Election Results.txt", "w")
f.write("Election Results")
f.write("----------------------------")

f.write(" Total Votes:" + str(totalvotes) )
f.write("----------------------------")
f.write(" Charles Casper Stockham: " + str(Charlesvotes_percentage) + "%" + "(" + str(totalCharlesvotes) +")")
f.write(" Diana DeGette: " + str(Dianavotes_percentage) + "%" + "(" + str(totalDianavotes) + ")")
f.write(" Raymon Anthony Doane: " + str(Raymonvotes_percentage) + "%" + "(" + str(totalRaymonvotes) + ")")
f.write("----------------------------")
f.write(" Winner: " + winner )
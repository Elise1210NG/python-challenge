import os
import csv


bad_csvpath = os.path.join("Resources", "budget_data.csv")
csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)
print(bad_csvpath)

#set up variables
budget_data = []
months = []
ProfitOrLoss = [0]
changes = []
totalmonthly_changes = []
GreatestInc = 0
GreatestDec = 0

with open(csvpath) as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=",")
    
      
    for row in csv_reader:
#find out total months in the spreadsheets
        months.append(row["Date"])
        totalmonths = len(months)

#find out net total profit/losses  
        ProfitOrLoss.append(int(row["Profit/Losses"]))
        total_PL = sum(ProfitOrLoss)

#find out the changes over the entire period      
        changes.append(int(row["Profit/Losses"]))     
       
        for i in range(totalmonths-1):
         monthly_changes = (changes[i+1]) - (changes[i])
         totalmonthly_changes.append(monthly_changes)
         totalChanges = list(dict.fromkeys(totalmonthly_changes))
         from statistics import mean
         def Average(totalChanges):
            return mean(totalChanges) 
         average_changes = Average(totalChanges)
         
#find out the greatest increase and decrease in profits
         GreatestInc = max(totalChanges)
         GreatestDec = min(totalChanges)

               
        
    







print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {totalmonths}')
print(f'Total: $ {total_PL}')
print("Average Change : $", round(average_changes,2))
print("Greatest Increase in Profits: " +  "  ($" + str(GreatestInc) + ")")
print("Greatest Decrease in Profits: " +  "  ($" + str(GreatestDec) + ")")

f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("----------------------------")

f.write(" Total Months: " + str(totalmonths))
f.write(" Total: $" + str(total_PL))
f.write(" Average Change is: $" + str(round(average_changes, 2)))
f.write(" Greatest Increase in Profits: " + "  ($" + str(GreatestInc) + ")")
f.write(" Greatest Decrease in Profits: " + "  ($" + str(GreatestDec) + ")")
















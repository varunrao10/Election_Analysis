#The data we need to retreive.
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total vote counter
total_votes = 0

#create candidate options list to store candidate names
candidate_options = []

#create candidate votes dictionary holding votes for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    #print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        #add to total vote counter
        total_votes += 1
        
        #access the candidate names in the lists
        candidate_name = row[2]
        
        #append the names to the options list and add only unique names
        if(candidate_name not in candidate_options):
            
            #Add unique name to option list
            candidate_options.append(candidate_name)
            
            #Add Unique names as keys to votes and assign a value of 0
            candidate_votes[candidate_name] = 0

        #Incrementing votes for candidates
        candidate_votes[candidate_name] += 1

#Write results to election_analysis.txt
with open(file_to_save, "w") as txt_file:
  # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    """""
    #Print the total votes.
    print("Total Votes: " + str(total_votes))

    #Print the candidate list
    #print(candidate_options)

    #Print dictionary of candidate votes
    print(candidate_votes)
    print("\n")
    """""

    for candidate_name in candidate_votes:
    
        #gets value from candidate name key
        votes = candidate_votes[candidate_name]
        
        #calculate percentage of votes
        vote_percentage = float(votes)/float(total_votes) *100

        #First iteration will assign the first key and value to the winning variables and as it iterates through the other keys will find the winner and assign as needed
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        #print candidate name and percentage of votes and vote count
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


"""
# Using the with statement open the file as a text file.
    # Write three counties to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
"""
#1. The total number of votes cast (DONE)
#2. A complete list of candidates who recieved votes (DONE)
#3. The percentage of votes each candidate won (DONE)
#4. The total number of votes each candidate won (DONE)
#5. The winner of the election based on popular vote (DONE)  
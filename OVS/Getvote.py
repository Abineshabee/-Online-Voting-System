import mysql.connector

# Connect to the MariaDB database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Abinesh1010',
    database='ovs'
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query to select all rows from the 'vote' table
cursor.execute("SELECT * FROM vote")

# Fetch all the rows
data = cursor.fetchall()

# Close the connection
conn.close()

# Initialize a dictionary to store votes for each candidate
candidate_votes = {}

# Iterate through the fetched data and calculate votes for each candidate
for row in data:
    candidate = row[1]  # Candidate name is in the second column (index 1)
    votes = row[2]      # Number of votes is in the third column (index 2)
    
    # Update the candidate's vote count in the dictionary
    if candidate in candidate_votes:
        candidate_votes[candidate] += votes
    else:
        candidate_votes[candidate] = votes
'''
# Print the vote count for each candidate
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes} votes")
'''
# Save the data to a file
with open(r'D:\.vscode\OVS\Data.txt', 'w') as file:
    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {votes} votes\n")

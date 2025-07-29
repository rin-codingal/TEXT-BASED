import requests

# Trivia API endpoint
url = "https://opentdb.com/api.php?amount=5&type=multiple" # Fetch 5 questions

# Send GET request to fetch trivia questions
response = 

# Check if the request was successful
if response.status_code == :
    trivia_data = 
    score = 0

    # Loop through each trivia question
    for i, question_data in enumerate(trivia_data["results"]):
        
        options =  # Add correct answer to options
        options =  # Shuffle options

        for j, option in enumerate(options):
            

        # Collect user's answer
        user_answer = 

        # Check if the answer is correct
        if options[] == question_data[]:
            
        else:
            

        print()
    print(f"Your final score: {score}/{len()}")

else:
    print("Failed to retrieve trivia")
# 1. IMPORT necessary libraries:
#    - google.genai (for interacting with the Gemini API)
#    - config (for managing API key)

# 2. DEFINE function generate_response(prompt, temperature=0.3):
#    - Initialize genai client using the API key from config
#    - Create content structure based on the prompt
#    - Send the prompt to Gemini API and return the generated response

# 3. DEFINE function bias_mitigation_activity():
#    - Print introductory message for bias mitigation activity
#    - Prompt user to input a prompt (e.g., "Describe the ideal doctor")
#    - Generate AI response to the initial prompt
#    - Prompt user to modify the prompt to make it more neutral
#    - Generate AI response to the modified (neutral) prompt
#    - Display both AI responses

# 4. DEFINE function token_limit_activity():
#    - Print introductory message for token limit activity
#    - Prompt user to input a long prompt (more than 300 words)
#    - Generate AI response to the long prompt
#    - Display a truncated portion of the response (limit output for demonstration)
#    - Prompt user to condense the long prompt into a shorter one
#    - Generate AI response to the shortened prompt
#    - Display the AI response to the shortened prompt

# 5. DEFINE function run_activity():
#    - Print introductory message for AI learning activity
#    - Prompt the user to choose between the bias mitigation activity or token limit activity
#    - If the user chooses "1", run bias_mitigation_activity()
#    - If the user chooses "2", run token_limit_activity()
#    - If the user enters an invalid choice, prompt them again

# 6. IF __name__ == "__main__":
#    - Call run_activity() to initiate the activity

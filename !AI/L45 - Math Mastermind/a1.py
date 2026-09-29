# 1. IMPORT required libraries:
#    - streamlit for UI
#    - google.genai for Gemini API client
#    - config for API key
#    - io for export functionality

# 2. INITIALIZE Gemini API client using API key from config

# 3. DEFINE generate_response(prompt, temperature=0.1):
#    - Define a detailed system prompt framing the AI as a math expert
#    - Combine system prompt with user’s math problem and difficulty level
#    - Send the combined prompt to Gemini API and get the response text
#    - Return AI response or error message

# 4. DEFINE setup_ui():
#    - Setup Streamlit page configuration and title
#    - Display introductory text and example math problems in an expander
#    - Initialize session state variables for conversation history and input key
#    - Provide buttons for clearing history and exporting solutions
#    - Create a form with:
#        - Text area for entering math problems
#        - Difficulty level selector
#        - Submit button ("Solve Problem")
#    - On submit:
#        - Validate input
#        - Append difficulty info to the prompt
#        - Call generate_response()
#        - Add question and answer to session history (latest on top)
#        - Increment input key and rerun app to clear input
#    - Display conversation history in a styled scrollable container with:
#        - Problem number and difficulty badge
#        - Detailed AI solution with formatting

# 5. DEFINE main():
#    - Call setup_ui()

# 6. IF __name__ == "__main__":
#    - Run main()

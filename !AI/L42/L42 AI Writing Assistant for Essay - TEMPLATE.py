import os
from google import genai
from google.genai import types
from colorama import init, Fore, Style

# Initialize colorama
init()

# Initialize the Gemini API client
client = genai.Client(api_key="write your API Key here")

# Function to generate AI response
def generate_response(prompt, temperature=0.3):
    """Generate a response from Gemini API."""
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=)])]

        config_params = types.GenerateContentConfig(temperature=)

        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=, config=)
        
        return 
    
    except Exception as e:
        return f"Error: {str(e)}"

# Step 1: Get essay details
def get_essay_details():
    print(Fore.CYAN + "\n=== AI Writing Assistant ===\n")
    print()

    # Gather user information for the essay
    topic = input(Fore.YELLOW + "")
    print()

    print( + "What type of essay are you writing? (e.g., Argumentative, Expository, Descriptive, Persuasive, Analytical) ")
    essay_type = input()
    
    # Modified section for selecting word count
    print(Fore.GREEN + "\nSelect the desired essay word count:")
    print(Fore.GREEN + "1. ")
    print(Fore.GREEN + "2. ")
    print(Fore.GREEN + "3. ")
    print(Fore.GREEN + "4. ")
    print()
    
    word_count_choice = input( + "Please enter the number corresponding to your choice: ")

    word_count_dict = {"1": "", "": "900", "": "1200", "": ""}
    length = (, "300")  # Default to 300 words if invalid input

    print()

    print( + "Who is the target audience for your essay? (e.g., High school students, College professors) ")
    target_audience = input()
    print()

    specific_points = input(Fore.YELLOW + "Do you have any specific points that must be included in the essay? ")
    print()

    # Additional details
    stance = input(Fore.YELLOW + "")
    print()

    references = input(Fore.YELLOW + "Are there any sources, quotes, or references you’d like to include? ")
    print()

    writing_style = input( + "Do you have any preferences for writing style? (e.g., Formal, Conversational, Academic, Creative) ")

    # Ask for outline preference
    outline_needed = input(Fore.YELLOW + "").lower()

    # Return the gathered information
    return {
        "topic": ,
        "essay_type": ,
        "length": length,
        "target_audience": target_audience,
        "specific_points": ,
        "stance": stance,
        "references": references,
        "writing_style": ,
        "outline_needed": 
    }

# Step 2: Generate Essay Content
def generate_essay_content(details):
    # Ask for creative vs structured temperature preference
    temperature = (input(Fore.YELLOW + "Do you prefer a more creative and open-ended response (higher temp, e.g., 0.7) or a structured response (lower temp, e.g., 0.2)? Enter temperature value: "))

    # Start with generating the introduction
    introduction_prompt = f"Write an introduction for an {['essay_type']} essay about {['topic']} on the topic of {['stance']}."

    introduction = generate_response(introduction_prompt, temperature)

    print(Fore.CYAN + "\n=== Generated Introduction ===")
    print()

    # Ask if user wants the full body or a step-by-step body
    body_style = input(Fore.YELLOW + "Would you like the AI to write the body step-by-step or generate a full draft? (Step-by-step/Full draft): ").lower()

    # Generate body content based on style
    if body_style == "full draft":
        body_prompt = f"Write a detailed {['essay_type']} essay about {['topic']} with the stance of {['stance']}."

        body = (body_prompt, )

        print(Fore.CYAN + "\n=== Generated Full Body ===")
        print(Fore.GREEN + body)
    else:
        # Step-by-step body generation
        body_step_prompt = f"Write step-by-step arguments for the essay on {details['topic']} with the stance of {['stance']}. Provide evidence and reasoning for each step."

        body_step = (, temperature)

        print(Fore.CYAN + "\n=== Generated Step-by-Step Body ===")
        print(Fore.GREEN + body_step)

    # Ask for conclusion generation
    conclusion_prompt = f"Write a conclusion for an {['essay_type']} essay about {['topic']} on the topic of {['stance']}."

    conclusion = (, temperature)

    print(Fore.CYAN + "\n=== Generated Conclusion ===")
    print(Fore.GREEN + conclusion)

# Step 3: Feedback and Refinement
def feedback_and_refinement():
    # Get user feedback on the content
    satisfaction = input(Fore.YELLOW + "How satisfied are you with the generated content? (Rate from 1 to 5 stars): ")

    if satisfaction != "5":
        print(Fore.YELLOW + "Please provide feedback on how we can improve the content (tone, structure, etc.): ")

        feedback = input(Fore.YELLOW)

        print(Fore.CYAN + f"\nThank you for your feedback! We will refine the essay based on your input: {}")
        
    else:
        print(Fore.CYAN + "\nThank you! The essay looks good.")

# Main Function
def run_activity():
    print(Fore.CYAN + "\nWelcome to the AI Writing Assistant!")
    
    # Get essay details from user
    details = ()
    
    # Generate the essay content based on the details
    
    
    # Ask for feedback and refine
    

# Run the Activity
if __name__ == "__main__":
    run_activity()

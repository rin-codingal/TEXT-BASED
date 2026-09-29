# 1. IMPORT libraries:
#    - streamlit for UI
#    - google.genai for Gemini API client
#    - PIL.Image for image handling
#    - re for prompt safety filtering
#    - io for in-memory image processing
#    - config for API key

# 2. INITIALIZE Gemini API client with API key

# 3. DEFINE is_prompt_safe(prompt):
#    - Check if prompt contains forbidden keywords (violence, hate, nude, etc.)
#    - Return False if any forbidden word is found; True otherwise

# 4. DEFINE generate_image(prompt):
#    - If prompt is not safe, return error message
#    - Prepare content structure and config for Gemini image generation model
#    - Stream the content from Gemini API
#    - For each chunk:
#        - If image data exists, convert to PIL image and return it
#        - Else continue reading chunks (skip text parts)
#    - If no image found, return error message

# 5. DEFINE main():
#    - Setup Streamlit page title and description
#    - Provide a form to enter image description prompt
#    - On submission:
#        - Validate prompt is non-empty and safe
#        - Call generate_image(prompt)
#        - Display generated image or error message
#        - Save generated image to session state for download
#    - Outside form:
#        - If generated image exists in session, provide a download button

# 6. IF __name__ == "__main__":
#    - Run main()

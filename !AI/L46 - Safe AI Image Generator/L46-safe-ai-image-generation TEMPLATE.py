import streamlit as st
import re
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# Initialize Gemini API client
client = genai.Client(api_key="") 

def is_prompt_safe(prompt: str) -> bool:
    """
    Basic filter to avoid generating harmful or restricted content.
    Extend this list based on your organization's content policy.
    """

    forbidden_keywords = [
        "violence", "weapon", "gun", "blood", "nude", "porn", "drugs", "hate", "racism", "sex",
        "terror", "bomb", "abuse", "kill", "death", "suicide", "self-harm", "hate speech"
    ]

    pattern = 

    return not bool() 

def generate_image(prompt: str):
    """
    Generate an image using Gemini API with the given prompt.
    Returns image data or error message.
    """

    if not is_prompt_safe(prompt):
        return None, "⚠️ "    

    try:
        # Use the correct model name and API structure based on reference

        contents = [
            types.Content(
                
            ),
        ]
 
        generate_content_config = types.GenerateContentConfig(
            
            response_mime_type="text/plain",
        )        

        # Use streaming approach like in the reference
        for chunk in client.models.generate_content_stream(
            
        ):
            if (
                
            ):
                continue                

            # Check for image data
            if (chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data):
                inline_data = 
                
                data_buffer = 
                
                # Convert to PIL Image
                image = 
                return image, None           

            # Handle text response
            elif chunk.text:
                # Continue to next chunk - text might come before image
                continue        

        return None, ""        

    except Exception as e:
        return None, f"Error during image generation: {str(e)}"
    
def main():
    st.set_page_config(page_title="Safe AI Image Generator", layout="centered")

    st.title("???? Safe AI Image Generator")

    st.write(
        "Enter a description to generate a safe and responsible AI image using Gemini 2.0 Flash. "

        "Examples: 'A serene sunset over a mountain lake', 'A futuristic city skyline at night'"
    )    

    # Add info about the model
    st.info("This app uses Gemini 2.0 Flash Preview for image generation with streaming response.")    

    with st.form(key="image_gen_form"):
        prompt = st.text_area(
            
        )

        submit = st.form_submit_button("Generate Image")        

        if submit:
            if not prompt.strip():
                st.warning("⚠️ ")

            else:
                with st.spinner("Generating image... This may take a few moments."):
                    image, error = 
                    
                if error:
                    st.error(error)

                elif image:
                                       

                    # Store image in session state for download outside form
                    

                else:
                    st.error("Failed to generate image. Please try again with a different prompt.")
                    
    # Download button outside the form
    if hasattr(st.session_state, 'generated_image') and st.session_state.generated_image:
        buf = 

        st.session_state.

        byte_im =         

        st.download_button(
            label="???? Download Generated Image",
            data=,
            file_name="ai_generated_image.png",
            mime=,
            help="Click to download the generated image"
        ) 

if __name__ == "__main__":
    main()
    # to run this streamlit web app, write python -m streamlit run filename.py in the terminal
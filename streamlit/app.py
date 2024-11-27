import os
import streamlit as st
import requests
from bs4 import BeautifulSoup
from openai import OpenAI


#client = OpenAI()
api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
# Set up OpenAI API key (you'll need an API key from https://openai.com/)
#openai.api_key = "your_openai_api_key"

# Set up SerpAPI search (you'll need an API key from https://serpapi.com/)
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_animal_info(query):
    """Use SerpAPI to get search results for a given query."""
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Parse the first result for relevant content
    if 'organic_results' in data and data['organic_results']:
        first_result_url = data['organic_results'][0]['link']
        result_response = requests.get(first_result_url)
        soup = BeautifulSoup(result_response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        return "\n".join([para.get_text() for para in paragraphs[:3]])  # Return first few paragraphs
    else:
        return "No information found."

def generate_image_from_prompt(prompt):
    """Generate an image using DALL·E based on a text prompt."""
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    return response.data[0].url

# Streamlit App Interface
try:
    st.title("Native South American Animals Info App")
    st.write("Enter the name of a South American animal to get information and generate an image.")
except Exception as e:
    print (e) 
# Input for animal name
animal_name = st.text_input("Enter animal name (e.g., 'Lama'):")

if animal_name:
    # Search for animal information
    st.write(f"Fetching information about {animal_name}...")
    info = search_animal_info(f"{animal_name} animal native South America")
    
    if info:
        # Display the raw info
        st.write("Information found:")
        st.write(info)

        # Generate an image based on the found information
        st.write("Generating an image based on the information...")
        image_prompt = f"An image of a {animal_name}, native to South America. {info}"
        image_url = generate_image_from_prompt(image_prompt)

        # Display the generated image
        st.image(image_url, caption=f"Generated image of {animal_name}")

    else:
        st.write("No information found for the specified animal.")

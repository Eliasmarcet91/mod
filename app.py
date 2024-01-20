import streamlit as st
from openai import OpenAI
import json
import pandas as pd

# Function to serialize the output
def serialize(obj):
    """Recursively walk object's hierarchy."""
    if isinstance(obj, (bool, int, float, str)):
        return obj
    elif isinstance(obj, dict):
        obj = obj.copy()
        for key in obj:
            obj[key] = serialize(obj[key])
        return obj
    elif isinstance(obj, list):
        return [serialize(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(serialize(item) for item in obj)
    elif hasattr(obj, '__dict__'):
        return serialize(obj.__dict__)
    else:
        return repr(obj)  # Don't know how to handle, convert to string

# Access the OpenAI API key from Streamlit secrets
api_key = st.secrets["openai_secret"]

# Initialize the OpenAI client with the API key from secrets
client = OpenAI(api_key=api_key)

# Streamlit UI components
st.title('''Elias Marcet Moderator application - CAI 2300C Introduction to Natural Language Processing at Miami Dade College - Kendall Campus - Hate Speech Detection''')

user_input = st.text_area("Enter text to moderate")


#create a button
if st.button('Moderate'):
    response = client.moderations.create(input=user_input)
    output = response.results[0]
    serialized_output = serialize(output)
    json_output = json.dumps(serialized_output, indent=2, ensure_ascii=False)
    st.json(json_output)
    


#add tabs to the UI
page1, page2, page3 = st.tabs(['Cloud Adoption', 'CyberSecurity', 'Linux'])
with page1:
    st.write("Steps for a successful Cloud Adoption.")
with page2:
    st.write("What is CyberSecurity?")
with page3:
    st.write("Introduction to Linux.")
    st.write("Visit the link below")
    st.write("https://tech101s.com/2020/07/21/linux/")

#add a map in the page
map_df = pd.DataFrame({'lat': [25.776667], 'lon': [-80.195377]})
st.map(map_df)


#add an image to the UI NEED TO WORK ON IT
#from PIL import Image
#image = Image.open('https://ernesto.net/wp-content/uploads/2021/01/1N1A0005.jpg')
#st.image(image, caption='All bald men have a big forehead')




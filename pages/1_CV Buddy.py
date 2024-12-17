import streamlit as st
from groq import Groq
from pypdf import PdfReader
from pathlib import Path
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()
#Get api key
API_KEY = os.getenv("API_KEY")

#Locate current directory
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()

#Import CV
cv = ""
reader = PdfReader(current_dir/"assets"/"cv.pdf")
for page in range(len(reader.pages)):
    # creating a page object
    page = reader.pages[page]
    # extracting text from page
    cv += page.extract_text()


client = Groq(api_key = API_KEY)

#Header
st.set_page_config(layout= "wide")
st.markdown("<h1 style='text-align: center; font-weight: bold;'>CV Buddy</h1>", unsafe_allow_html=True)

#Chat input
resp = st.container(height = 300, border  = False)
prompt = st.chat_input(placeholder = "Write a message")
user = "😄"
assistant = "🤖"



#Input-Processing-Output block    
def process(prompt):
    ''' 
    This function takes in the text input, processes it and returns a text
    output to be displayed
    '''
    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": f"""You are an AI powered chatbot named CV-Buddy integrated into a digital CV. This is the CV: {cv}. You were created by Chikamso 
                Chidi-Akoma showcasing his skills and abilities in a unique and interactive way. You are to answer general questions. Please try to avoid his
                Mechanical Engineering background."""
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
       
    )
    
    response = chat_completion.choices[0].message.content
    return response
    



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
    
with resp:
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == assistant:
                st.markdown(message["content"])
            elif message["role"] == user:
                st.markdown(message["content"])
    
    
    # React to users (first) input
    if prompt:
        try:
            # Display user message in the chat messsage container
            with st.chat_message(user):
                st.markdown(prompt)
            #Add user message to chat history
            st.session_state.messages.append({"role":user, "content": prompt})
        except:
            #Display error message
            with st.chat_message(assistant):
                response = 'Error! Check your internet connection.'
                st.markdown(f'<span style="color:red;">{response}</span>', unsafe_allow_html=True)
                
        try:
            with st.chat_message(assistant):
                response = process(prompt)
                st.markdown(response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role":assistant, "content":response})
        except:
            #Display error message
            with st.chat_message(assistant):
                response = 'Error! Check your internet connection.'
                st.markdown(f'<span style="color:red;">{response}</span>', unsafe_allow_html=True)
                


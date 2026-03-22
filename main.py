import os
import streamlit as st
import google.genai as genai
from google.genai import types
from dotenv import load_dotenv
from tools import get_city_profile, compare_cities, get_best_cities, get_worst_cities

st.set_page_config(page_title="Global Air Quality Agent", page_icon="🌍", layout="wide")
st.title("🌍 Global Air Quality AI Assistant")

if "chat_session" not in st.session_state:
    load_dotenv()
    
    # Store the client directly in Streamlit's memory so it never closes
    st.session_state.client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    my_tools = [get_city_profile, compare_cities, get_worst_cities, get_best_cities]
    instruction = "You are a helpful Air Quality Data Assistant. Always use your tools to find exact numbers."
    
    agent_config = types.GenerateContentConfig(
        system_instruction=instruction,
        temperature=0.1,
        tools=my_tools,
    )
    
    #Create the chat session using the memorized client
    st.session_state.chat_session = st.session_state.client.chats.create(
        model="gemini-2.5-flash",
        config=agent_config
    )
    st.session_state.messages = []



#Display exisitng chat to the screen
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# The Chat Input Box
user_input = st.chat_input("Ask me about air quality...")
if user_input:
    # Show user message immediately
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Send to Gemini
    with st.chat_message("assistant"):
        with st.spinner("Analyzing data..."):
            response = st.session_state.chat_session.send_message(user_input)
            st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})


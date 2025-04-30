import streamlit as st
from main import get_chatbot_response  # Ollama-based function
from openai import OpenAI


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


#css
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif !important;
        line-height: 1.5 !important;
        color: #F8F8F2 !important;
    }

    h1, h2, h3, h4, h5, h6, p, div, span, input, textarea, button {
        font-family: 'Poppins', sans-serif !important;
        color: #F8F8F2 !important;
    }

    /* Button and Input styling */
    .stButton, .stTextInput, .stTextArea, .stFileUploader, .stCheckbox, .stRadio {
        font-family: 'Poppins', sans-serif !important;
        border-radius: 5px;
        color: #2D2A2E !important;
        border: none !important;
    }

    h1 {
        color: #F92672 !important;  /* Vibrant Pink for main title */
    }

    .model-switch {
        background: none;
        border: none;
        color: #1f77b4;
        text-decoration: underline;
        cursor: pointer;
        font-size: 16px;
        margin: 10px 0;
    }

    .model-switch:hover {
        color: #e63946;
    }

    .chat-role {
        font-weight: 500;
    }

    .stChatInputContainer {
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)





# ----- SIDEBAR -----
with st.sidebar:
    st.title("AI Chatbot")

    current_model = st.session_state.get("selected_model", "ollama")

    if current_model == "ollama":
        st.markdown("""
            **ollama chatbot**

            Ask anything, and the AI will respond with smart, human-like answers.

            ---  
            **model**: `llama3.2`  
            **frontend**: Streamlit  
            **backend**: Ollama (local LLM engine)

            ---
        """)
    else:
        st.markdown("""
            **openai chatbot**

            This version uses the OpenAI API to generate intelligent and high-quality responses.

            ---  
            **model**: `GPT-4 / GPT-3.5`  
            **frontend**: Streamlit  
            **backend**: OpenAI Cloud API

            ---
        """)
    
    # Model toggle switch
    st.markdown(f"### Current Model: `{st.session_state.get('selected_model', 'ollama').upper()}`")
    if st.button("Switch Model"):
        if st.session_state.get("selected_model", "ollama") == "ollama":
            st.session_state.selected_model = "openai"
            st.session_state.previous_conversation_ollama = []  # clear ollama chat


        else:
            st.session_state.selected_model = "ollama"
            st.session_state.previous_conversation_openai = []  # clear openai chat

        st.rerun()


        

# ----- Initialize Chat Memory -----
if "selected_model" not in st.session_state:
    st.session_state.selected_model = "ollama"

if "previous_conversation_ollama" not in st.session_state:
    st.session_state.previous_conversation_ollama = []

if "previous_conversation_openai" not in st.session_state:
    st.session_state.previous_conversation_openai = []

st.sidebar.write("🔁 Memory:")
st.sidebar.json(st.session_state.previous_conversation_openai)

# ----- Display Chat History ----
if st.session_state.selected_model == "ollama":
    for msg in st.session_state.previous_conversation_ollama:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# ----- User Input + Response -----
if prompt := st.chat_input("Type here..."):
    
    if st.session_state.selected_model == "ollama":

        with st.chat_message("user"):
            st.markdown(prompt)


        response = get_chatbot_response(prompt, st.session_state.previous_conversation_ollama)
        with st.chat_message("ai"):
            st.markdown(response)  






    else:
        st.session_state.previous_conversation_openai.append({"role": "user", "content": prompt})

        st.session_state["openai_model"] = "gpt-4"
        for message in st.session_state.previous_conversation_openai:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.previous_conversation_openai
            ],
            stream=True,
        )
            response = st.write_stream(stream)
        st.session_state.previous_conversation_openai.append({"role": "assistant", "content": response})


import google.generativeai as genai
import streamlit as st

# --- Gemini API Key Setup ---
API_KEY = "AIzaSyAocKnnS6xRrR5b78LhsDthcWfimRcTU-s"  
genai.configure(api_key=API_KEY)

# --- Gemini Model Initialization ---
try:
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
except Exception as e:
    st.error(f"Error initializing Gemini model: {e}")
    st.stop()

# --- App UI ---
st.title('AI CHAT ASSISTANT')
st.subheader('Created by Rakesh')
st.markdown("---")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Special Query Handler ---
def handle_special_queries(message):
    lower = message.lower()
    if 'your creator' in lower or 'Rakesh' in lower:
        return "Rakesh, the creator of AI CHAT ASSISTANT, is passionate about tech and AI."
    elif lower in ['AI CHAT ASSISTANT', 'who are you', 'who are you?', 'what is your name', 'what is your name?']:
        return "I am AI CHAT ASSISTANT, created by Rakesh."
    return None

# --- Gemini Chat Completion ---
def get_gemini_response(message):
    try:
        response = model.generate_content(message)
        return response.text.strip()
    except Exception as e:
        st.error(f"Error getting response from Gemini: {e}")
        return "Sorry, something went wrong while processing your message."

# --- Main Function ---
def main():
    user_input = st.text_input("Write your question here:")

    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

    if not user_input:
        return

    if st.button("Submit"):
        special_response = handle_special_queries(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        if special_response:
            st.session_state.chat_history.append({"role": "bot", "content": special_response})
        else:
            response = get_gemini_response(user_input)
            st.session_state.chat_history.append({"role": "bot", "content": response})

    # Display chat history
    for chat in st.session_state.chat_history:
        role = "You" if chat["role"] == "user" else "AI CHAT ASSISTANT"
        st.write(f"{role}:** {chat['content']}")

# --- Run App ---
if __name__ == "__main__":
    main()
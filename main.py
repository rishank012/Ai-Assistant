import streamlit as st  # type:ignore
import image_generator as img
import genai_model as g

# Set up the page layout
st.set_page_config(page_title="AI Chatbot", layout="wide")

st.title("🤖 Friday Ai Assistant")

# Create Tabs for Chatbot and Image Generation
tab1, tab2 = st.tabs(["💬 Chat", "🖼️ Image Generation"])

# Chatbot Environment
with tab1:
    st.subheader("Chat With Ai")

    col1, col2 = st.columns([8, 2])

    with col1:
        user_input = st.text_input("Type your message:", key="user_text")
        if user_input:
            a = g.chat_with_gemini(user_input)
            st.chat_message("user").markdown(a)

    with col2:
        st.write("## Voice Input \n(Click to Speak)")
        if st.button("🎤", key="voice_btn"):
            import Friday

# Image Generation Environment
with tab2:
    st.subheader("Generate AI Images:frame_with_picture:")
    prompt = st.text_input("Enter an image description:")
    if st.button("Generate Image", key="image_btn"):
        st.write("Generating image...")
        try:
            img.image(prompt)
        except Exception as e:
            st.error(f"Error generating image: {e}")

st.success("This is just a starter version. More Updates soon...")

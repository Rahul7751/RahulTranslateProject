import streamlit as st
import google.generativeai as genai

# === Set Streamlit config ===
st.set_page_config(page_title="English to French Translator (Gemini Flash)", layout="centered")

# === Title ===
st.title("🌍 English to French Translator")
st.write("Powered by Gemini 2.0 Flash")

# === Set API Key ===
API_KEY = "AIzaSyCtD7pFRnyEX-0BxEvqI7QLpHl9fz_VWYw"
genai.configure(api_key=API_KEY)

# === Load correct Gemini model ===
try:
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
except Exception as e:
    st.error(f"❌ Failed to load Gemini Flash model: {str(e)}")
    st.stop()

# === Input box ===
user_input = st.text_input("Enter an English sentence:")

# === Button to trigger translation ===
if st.button("Translate"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a sentence.")
    else:
        with st.spinner("🔄 Translating..."):
            try:
                prompt = f"Translate the following English sentence to French:\n\n{user_input}"
                response = model.generate_content(prompt)
                translation = response.text.strip()
                st.success("✅ Translation Complete!")
                st.text_area("French Translation:", value=translation, height=100)
            except Exception as e:
                st.error(f"❌ Error during translation: {str(e)}")

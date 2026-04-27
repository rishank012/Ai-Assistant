import google.generativeai as genai

genai.configure(api_key="") # <-- Paste your api key here

model = genai.GenerativeModel("gemini-3-flash-preview")

def chat_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text


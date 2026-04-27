from google import genai
from google.genai import types  # type:ignore
from PIL import Image
from io import BytesIO
import base64
import streamlit as st  # type:ignore

client = genai.Client(api_key="") # <-- you have to paste your api key here


def image(a):

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=a,
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE']
        )
    )
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            st.write("Generated Text:", part.text)
        elif part.inline_data is not None:
            # Decode and display the image
            i = Image.open(BytesIO(part.inline_data.data))
            i.save('generated_image.jpg')
            st.image(i, caption="Generated Image")
            st.write("Image generated successfully!")

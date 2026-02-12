import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import datetime

# Connect to HuggingFace
client = InferenceClient(token="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")

MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

st.set_page_config(page_title="AI Image Generator", page_icon="🖼️")
st.title("🖼️ AI Image Generator")
st.write("Type a description, choose a style, and let AI create an image")

# User input
prompt = st.text_input("Describe your image")

style = st.selectbox(
    "Choose Art Style",
    ["Realistic", "Anime", "Cartoon"]
)

# Convert style into AI instruction
style_prompt = {
    "Realistic": "realistic, highly detailed, photo quality",
    "Anime": "anime style, japanese animation, vibrant colors",
    "Cartoon": "cartoon style, 2D illustration, bold lines"
}

if st.button("Generate") and prompt:
    final_prompt = f"{prompt}, {style_prompt[style]}"

    with st.spinner("AI is creating your image..."):
        image = client.text_to_image(final_prompt, model=MODEL)
        st.image(image, caption=final_prompt)

        # Save image
        filename = f"ai_image_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        image.save(filename)

        st.success(f"Image saved as {filename}")

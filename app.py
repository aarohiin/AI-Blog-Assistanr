import os
import streamlit as st
from openai import OpenAI
from datetime import datetime
import re
import time
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")

if not api_key:
    st.error("Please set the NVIDIA_API_KEY in a .env file.")
    st.stop()

# Initialize NVIDIA model client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

st.set_page_config(page_title="📝 Blog Assistant", layout="wide")

# App title
st.title("📝 Blog Generator with NVIDIA LLM")
st.caption("Powered by Nemotron-3 70B | API via NVIDIA")

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Settings")
    blog_type = st.selectbox("Blog Type", ["How-to", "Listicle", "Explainer", "Opinion", "Review"])
    tone = st.selectbox("Tone", ["Professional", "Casual", "Witty", "Empathetic"])
    audience = st.selectbox("Target Audience", ["Developers", "Marketers", "General Readers", "Researchers"])
    word_count = st.slider("Word Count", min_value=300, max_value=1500, value=600, step=100)
    st.markdown("---")
    st.markdown("📌 Tip: Add keywords to your prompt for better SEO.")

# Main prompt input
prompt = st.text_area("🧠 What should the blog be about?", placeholder="e.g. How AI is transforming healthcare...")

# Helper to format title
def slugify(text):
    text = text.strip().lower()
    return re.sub(r'[^a-z0-9]+', '-', text)

# Generate blog
if st.button("🚀 Generate Blog"):
    if not prompt:
        st.warning("Please enter a topic.")
        st.stop()

    # Define structured system prompt
    system_prompt = (
        f"You are a blog writing assistant. Write a detailed {blog_type.lower()} blog post "
        f"in a {tone.lower()} tone for {audience.lower()}. Limit it to approximately {word_count} words. "
        f"Ensure proper structure with title, introduction, body, and conclusion. Use markdown formatting."
    )

    with st.spinner("Generating content..."):
        response = client.chat.completions.create(
            model="meta/llama3-70b-instruct",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )

        content = response.choices[0].message.content
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{slugify(prompt[:30])}_{timestamp}.md"

        st.success("✅ Blog generated!")
        st.download_button(
            label="💾 Download as Markdown",
            data=content,
            file_name=filename,
            mime="text/markdown"
        )

        st.markdown("---")
        st.markdown("### 📝 Generated Blog Content")
        st.markdown(content)

import streamlit as st
from prompts import generate_story
from image_generator import generate_image

st.set_page_config(page_title="Whatwat | AI Sci-Fi Generator")
st.title("🚀 Whatwat")

st.markdown("Enter a short bio and watch AI turn it into a dramatic sci-fi story.")

user_bio = st.text_area("Your Bio", placeholder="E.g. 25, designer, loves plants and vaporwave, introvert")

if st.button("Generate My Story") and user_bio:
    with st.spinner("Generating your sci-fi novel..."):
        title, story = generate_story(user_bio)
        image_url = generate_image(user_bio)

    st.subheader(title)
    st.write(story)
    st.image(image_url, caption="AI-generated book cover")
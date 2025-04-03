import streamlit as st
from PIL import Image

# Set Page Title
st.set_page_config(page_title="My Art Portfolio", layout="wide")

# Header Section
st.title("🎨 My Art Portfolio")
st.write("Welcome to my digital space where I showcase my passion for art!")

# About Me
st.header("About Me")
st.write("Hi, I'm Omkar, a fourth-year Fine Arts student specializing in contemporary and digital art. My work explores surrealism, human emotions, and abstract storytelling through various mediums, including oil painting, digital illustration, and mixed media.")

# Display Profile Image (Optional)
profile_image = "i7_Passport_Photo 6.jpeg"  # Replace with actual image path
if profile_image:
    image = Image.open(profile_image)
    st.image(image, width=250, caption="[Your Name]")

# Selected Works
st.header("Selected Works")
artworks = [
    {"title": "Dreamscape", "medium": "Oil on Canvas", "year": "2023", "desc": "A surreal representation of the subconscious mind."},
    {"title": "Digital Metropolis", "medium": "Digital Art", "year": "2024", "desc": "Exploring the fusion of technology and human existence."},
    {"title": "Ethereal Realms", "medium": "Watercolor", "year": "2022", "desc": "A soft yet powerful depiction of dream-like landscapes."},
    {"title": "Fragments of Time", "medium": "Mixed Media", "year": "2023", "desc": "A visual exploration of memories and emotions."}
]

for art in artworks:
    st.subheader(art["title"])
    st.write(f"*{art['medium']}, {art['year']}*")
    st.write(art["desc"])
    # Add an image placeholder (Replace with actual image path if available)
    st.image("https://via.placeholder.com/400", width=400, caption=art["title"])

# Exhibitions & Features
st.header("Exhibitions & Features")
st.write("- **Emerging Artists Showcase**, 2023 - City Art Gallery")
st.write("- **Digital Art Revolution**, 2024 - Online Exhibition")
st.write("- **Best Contemporary Work Award**, 2023 - National Art Competition")

# Contact Information
st.header("8624013521")
st.write("📧 Email: omkarok2510@gamil.com")
st.writest.write("📸 Instagram: [@omkar_karale_25](https://www.instagram.com/omkar_karale_25/)")

st.write("🎭 LinkedIn: [Your Profile]https://www.linkedin.com/in/omkar-karale-21881a281/")



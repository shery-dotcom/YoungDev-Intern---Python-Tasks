import streamlit as st


# Example: Displaying an image
st.image(r"C:\Users\ahmed\OneDrive\Pictures\Skardu Trip\IMG_3199.jpg", width=200)


# Set the title and subtitle
st.title("Talha Asif's Digital Resume")
st.subheader("Python Developer and AI Enthusiast")


# Personal Information
st.write("### Personal Information")
st.write("""
- **Name:** Talha Asif
- **Email:** talhaasif487@gmail.com
- **Location:** Soan Garden Block H, Street 25B, House 11, Islamabad
""")


# Education
st.write("### Education")
st.write("""
- **BS in Artificial Intelligence** from COMSATS University
""")


# Experience
st.write("### Experience")
st.write("""
- **Python Developer Intern at CodeAlpha**
  - Developed Python scripts for various tasks
  - Shared explanations of tasks on LinkedIn
- **Managed C3 Account** for almost 2 years, completed numerous campaigns
- **Social Media Marketing** for C3 Society at COMSATS University
""")


# Projects
st.write("### Projects")
st.write("""
- **Image Recognition Project** using CNN to identify bird species
""")


# Skills
st.write("### Skills")
st.write("""
- Python
- Django
- Machine Learning
- Convolutional Neural Networks (CNN)
- Social Media Marketing
""")


# Footer
st.write("### Connect with Me")
st.write("[LinkedIn](https://www.linkedin.com/in/talha-asif-084985248)")

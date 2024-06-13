from pathlib import Path
import streamlit as st
from PIL import Image

# Path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# General Settings of the website
PAGE_TITLE = "Personal Landing Website | Marvin Baesa"
PAGE_ICON = ":wave:"
NAME = "Marvin Baesa"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision making.
"""
EMAIL = "engr.marvinbaesa01@gmail.com"
SOCIAL_MEDIA = {
    "Github": "https://github.com/EngrEmperorNERO"
}

# Ensure set_page_config is called once and at the start
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS, PDF, and Profile Pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(EMAIL)

# Social Links:
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Experience and Qualifications
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✅ More than 3 years of experience extracting actionable insights from data
    - ✅ Strong hands-on experience and knowledge in Python, SQL, and Excel
    - ✅ Good understanding of statistical principles and their respective applications
    - ✅ Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# Skills
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 👨‍💻 Programming: Python (Pandas, Openpyxl, Numpy, Matplotlib, Selenium, Streamlit, BeautifulSoup)
    - 📊 Data Visualization: Power BI, MS Excel, Google Sheet, and Tableau
    - 🗃️ Data Processing: Data cleaning, Data transformation, Data wrangling, and Data modeling
    - 💻 Database: MySQL and PostgreSQL
    """
)

# Work History
st.write("#")
st.subheader("Work History")
st.write("---")

# Job 1
st.write("**Senior Data Analyst | Ross Industries**")
st.write("2/2020 - Present")
st.write(
    """
    - ▶️ Used Power BI and SQL to redefine and track KPIs surrounding marketing initiatives and supplied recommendations
      to boost landing page conversion rate by 38%
    - ▶️ Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented
      A/B tests to generate 15% more clients
    - ▶️ Redesigned data model through iterations that improved refund and shipping projections by 12%
    """
)

# Ensure there are no additional calls to set_page_config
#if __name__ == "__main__":
#    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "unnu.png"



# --- GENERAL SETTING  
PAGE_TITLE = "Nutthawut Ruengsri"
PAGE_ICON = ":wave:"
NAME = "Nutthawut Ruengsri"
DESCRIPTION = """
Hi My name is Nutthawut Ruengsri.
   \nMy nickname is unun. 
- I was born on Wednesday 19 th of Dec 2001. I am 22 years old.
  
"""
EMAIL = "rnutthawut1919@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "www.linkedin.com/in/nutthawut-ruengsri-02a767261",
    "GitHub"  : "https://github.com/nunu19nunu",
    "Facebook" : "https://www.facebook.com/unun1919",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("My Resume")


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



# --- HERO SECTION --- 
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=270)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧",EMAIL)



# --- SOCIAL LINK ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXP & QUALIFICATIONS ---
st.write("#")
st.subheader("Education")
st.write("---") 
st.write(
    """
- ► Graduated from high school at Watrajabopit school.
- ► Bachelor’s Degree at Rajamangala University of Technology Phra Nakhon.
- ► Faculty of Science Department of Data Science, Bangkok, Thailand (GPA3.64)

"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Soft Skill")
st.write("---")
st.write(
    """
 - ► Communication
 - ► Emotional Intelligence
 - ► Collaboration
 - ► Social Quotient
"""
)

st.write("#")
st.subheader("Hard Skill")
st.write("---")
st.write(
    """
- 💻 Programing: Python (Scikit-learn, Pandas, Streamlit, Seaborn)
- 🖥️ Web programming: HTML, CSS
- 📊 Data Visulization : PowerBi, MS Excel, Tableau
- 📔 Modeling : Logistic regression, Random Forest, Decision trees
- 💾 Database : MySQL
"""
)

# --- Language ---

st.write("#")
st.subheader("Language")
st.write("---")
st.write(
    """
- Thai(Native)
- English (Fair)


"""
)
# --- Project  & Accomplishment
st.write("#")
st.subheader("Project & Accomplishment")
st.write("---")
st.write("""
- ► Python (2023)
- ใช้ Python model(RandomForestClassifier) ในการทำนายน้ำท่วม
- ใช้ Streamlit ในการนำขึ้นเว็บ
""")
st.write("---")
st.write(
    """
- ► Cloud Computing (2022)
- สร้าง Compute Engine
- จัดการ Virtualizatoin Network
- ติดตั้ง Jupyter Notebook ลงบน Compute Engine
- ปรับแต่ง Jupyter Notebook ให้ใช้งานได้กับ SSL
""")
st.write("---")
st.write(
    """
- ► Digital image data analysis (2022)
- สร้างโมเดลการเรียนรู้ เพื่อตรวจจับการใส่หน้ากากอนามัย
- โดยการใช้ Machine Learning


"""
)




# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

st.write("💳", "**Internship | Information Technology Center Department of Disaster Prevention and Mitigation Ministry of Interior.**")
st.write("26/06/2023 - 12/10/2023")
st.write(
    """
- ► Make a Dashboard about Drought in the Tableau program.
- ► Make a Dashboard about Flood in the Tableau program.
- ► Help organize a meeting the project to develop the potential of information and communication technology personnel.
- ► Help organize a meeting the project using radio frequency synthesis equipment.



"""
)

import streamlit as st
from pathlib import Path
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"cv.pdf"
profile_pic = current_dir/"assets"/"profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Chikamso Chidi-Akoma"
PAGE_ICON = ":wave:"
NAME = "Chikamso Chidi-Akoma"

DESCRIPTION =  "Data Analyst, assisting entreprises by supporting data-driven decision-making"
EMAIL = "chikamsochidiakoma@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/chikamso-chidi-akoma-98b81a233",
    "GitHub": "https://github.com/ChikamsoChidi/",
    "Twitter":""
    }

# --- ADD PAGE TITLE ---
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON, layout= "wide")


# --- LOAD CSS FILE PDF AND PROFILE PIC ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- Hero Section ---
col1, col2 = st.columns([2,3], gap = "small")

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button("Download CV", data = PDFbyte, file_name = resume_file.name,
                       mime="application/octet-stream")
    st.write("✉",EMAIL)
    
# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# --- Experience & Qualification ---
st.write("#")
st.subheader("Experience and Qualification")
st.write(
    """
    - 2+ years of experience extracting actionable insights from data
    - Strong hands on experience and knowledge
    - Good Understanding of statistical principles and their respective applications
    - Excellent team-player and displaying stroong sense of initiative on tasks
    """
    )

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - Programming Python (Scikit-Learn, Pandas), SQL, VBA
    - Data Visualization Power-BI, MS-Excel, Matplotlib
    - Modeling: Logistic Regression, Linear Regression, Decision Trees
    - Databases: PostgreSQL, SQLite
    """
    )

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.divider()

# --- JOB 1
job_col1, job_col2 = st.columns([2.5,1])

with job_col1:
    st.write("##### Data Analysis Intern | Accenture North America")
    st.write("January 2024")
    st.write(
        """
        - Completed a simulation focused on advising a hypothetical Social Media client as a Data 
        Analyst at Accenture North America.
        - Cleaned, modelled and analysed several datasets to uncover insights into content trends to 
        inform strategic decisions.
        - Prepared a PowerPoint deck and video presentation to communicate key insights for the client 
        and internal stakeholders.
    
        """
        )
with job_col2:
    st.image(Image.open(current_dir/"Assets"/"Accenture.jpg"))
  

# --- JOB 2
st.write("#")
job_col1, job_col2 = st.columns([2.5,1])

with job_col1:
    st.write("##### Data Analysis Intern | Techrative Technologies LTD")
    st.write("August 2024")
    st.write(
        """
        - Streamlined data collection and reporting procedures, reducing processing time by 20% 
        enhancing efficiency
        - Implemented process improvements and automation solutions, resulting in 15% increase in 
        productivity 
        - Collaborated with 3+ cross-functional teams tgather requirements, define project scopes, and 
        ensure alignment with business objectives, fostering effective teamwork and project success.
        - Produced 15+ comprehensive reports and presentations summarizing findings and 
        recommendations, facilitating clear communication with stakeholders and driving actionable 
        outcomes.
        - Conducted in-depth market research and analysis, resulting in identification of 10+ key trends 
        and insights that informed strategic decision-making processes.
        """
        )
with job_col2:
    st.empty()
    
    

# --- PROJECT AND ACCOMPLISHMENT ---
st.write("#")
st.subheader("Projects and Accomplishments")
st.divider()

# --- PROJECT 1
st.write("#")
proj_col1, proj_col2 = st.columns([2.5,1])
with proj_col1:
    st.write("##### 1st Runner-Up, Innovate with Forvis Mazars Hackathon")
    st.write("November 2024")
    st.write(
        """
        - Developed Smart-Audit, an innovative AI-powered tool designed to streamline the auditing process, 
        making it faster, more efficient, and less tedious.
        - Performed extensive research on the RAG (Retrieval-Augmented Generation) applications 
        to allow Smart-Audit to strictly follow IFRS and GAAP standards.
        - Integrated Azure OpenAI LLM (Large Language Model) into SmartAudit.
        - Rigorously understudied vector databases and integrated them to initial versions of Streamlit.
    
        """
        )
with proj_col2:
    st.image(Image.open(current_dir/"Assets"/"Forvis Mazars Cert.jpg"))

# --- PROJECT 1
st.write("#")
proj_col1, proj_col2 = st.columns([2.5,1])
with proj_col1:
    st.write("##### Housing Price Prediction")
    st.write("June 2024")
    st.write(
        """
        - Achieved an RSME of 44018.76 in forecasting the price of houses by developing and deploying a 
        machine learning model.
        - Managed data Integrity by handling missing values and encoding categorical variables, 
        enhancing quality by 30%.
        - Conducted experiments with regression algorithms to identify the most suitable approach.
        - Performed rigorous feature engineering and hyperparameter tuning processes to increase 
        precision.
    
        """
        )
with proj_col2:
    st.image(Image.open(current_dir/"Assets"/"Housing Pred.png"))


# --- PROJECT 2
st.write("#")
proj_col1, proj_col2 = st.columns([2.5,1])
with proj_col1:
    st.write("##### Social Media Sentiment Analysis")
    st.write("January 2024")
    st.write(
        """
        - Identified key investment opportunities through sentiment analysis, resulting in 30% increase in 
        ROI.
        - Cleaned several datasets with varying content types and categories to achieve high data integrity.
        - Modelled relationships between several datasets to ensure coherence and comprehensiveness.
        - Created PowerPoint presentation slides to communicate insights to key stakeholders. 
        """
        )
with proj_col2:
    st.image(Image.open(current_dir/"Assets"/"Analysis for Social Buzz_page-0008.jpg"))
    
    
# --- Project 3
st.write("#")
proj_col1, proj_col2 = st.columns([2.5,1])
with proj_col1:
    st.write("##### Web Scraping and Data Analytics")
    st.write("September 2024")
    st.write(
        """
        - Scraped over 200 rows and 5 columns of data from multiple webpages using Selenium
        - Collected various geographic datasets for future analysis.
        - Cleaned the data to achieve high data integrity.
        - Designed a performance dashboard with Power BI to comunicate Key Performance Indicators (KPI).
        """
        )
with proj_col2:
    st.image(Image.open(current_dir/"Assets"/"Barber Site analysis.jpg"))


# --- Project 4
st.write("#")
proj_col1, proj_col2 = st.columns([2.5,1])
with proj_col1:
    st.write("##### Sales Analysis Dashboard")
    st.write("October 2024")
    st.write(
        """
        - Cleaned the data to achieve high data integrity.
        - Built interactive sales analysis dashboard to allow users filter and drill down on relevant data.
        - Performed product-wise sales performance and analysis.
        - Reflected real time sales tracking and visualization.
        """
        )
with proj_col2:
    st.image(Image.open(current_dir/"Assets"/"Sales Analysis Dashboard.png")) 
    
    
# --- Project 5
st.write("#")
proj_col1, proj_col2 = st.columns([2.5,1])
with proj_col1:
    st.write("##### Supply Chain and Freight Analytics Dashboard")
    st.write("August 2024")
    st.write(
        """
        - Real-time shipment tracking and visiblity.
        - Freight cost analysis and optimization.
        - Supply chain network mapping and risk assessment.
        - Carrier performance evaluation and benchmarking.
        """
        )
with proj_col2:
    st.image(Image.open(current_dir/"Assets"/"Supply Chain and Freight Analytics Dashboard.png"))

#!/usr/bin/env python 3

import streamlit as st
import pandas as pd


def main():

    st.set_page_config(
        page_title="Joe Howie",
        page_icon="🌈",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.sidebar.title("Navigation")
    
    view = st.sidebar.radio(
        "Go to",
        ["About Me", "Work History", "Educatiion", "Publications"]#, "Projects"]
    )
    st.sidebar.image("profile_pic.jpg")
    st.title("Joe Howie")
    # st.caption("A veiw of my work history, education, publications, and projects.")
  
    if view == "About Me":
        about_me()

    elif view == "Work History":
        work_history()

    elif view == "Educatiion":
        education()

    elif view == "Publications":
        publications()

    # elif view == "Projects":
    #     projects()


# Page functions
def about_me():
    st.write("""Hello, my name is Joe! I am a profession Data Scientist with a background in Physics and Computer Science. For the last 5 years I have worked in health data analytics, building powerful machine learning algorithms and create health indicator dashboards.""")
    with st.expander("Proficient Softwares"):
        data = {"Python": 10, 
                "Java": 8, 
                "SQL": 8, 
                "Bash": 5, 
                "C/C++": 5,
                "Excel": 10,
                "Power BI": 3,
                "LaTex":10,
                "Linux": 8, 
                "Microsoft": 15,
                "Mac OS": 20,
                "Matlab":2,
                "Git": 10,
                "Neo4j":2}
        print_list(data.keys())
        # data = {key: value for key, 
        #        value in sorted(data.items(), 
        #                        key=lambda item: item[1], reverse=True)}
        # df = pd.DataFrame(data.values(), columns=["Years of Experience"], index=data.keys())
        # st.dataframe(df, width="content", height="content")
    with st.expander("Analytical Techniques"):
        list_of_skills = ["Regression", "PCA", "t-SNE", "K-Means clustering", "Machine Learning", "LSTM", "NLP", "Transformers", "Dimentional Analysis", "Integral, Differential, and Vector Calculus", "Linear Algebra"]
        print_list(list_of_skills)
    with st.expander("Hardware Experience"):
        loe = ["3D-Printers", "Oscilloscopes", "DAQ", "Breadboards", "Soldering Circuit Boards", "Raspberry Pi", "Arduino", "Embedded Systems", "Multimeters"]
        print_list(loe)
        

def work_history():
    st.divider()
    write_job(position="Data Consultant", 
              company="Interior Health Autority", 
              time="August 2023 -- Present", 
              location="Kelowna, B.C. (Remote)", 
              description="""Created dashboards, scorecards, and KPI’s for members of the organization that affect the decision making process. Responsible for managing different portfolios and indicators that require monthly or quarterly updates. Built interpersonal relationships with clients from different departments within the organization."""
              )
    st.divider()
    write_job(position="Research Developer", 
              company="Vancouver Island Health Authority", 
              time="November 2021 -- December 2023", 
              location="Victoria, B.C. (Remote)", 
              description="""Designed analytic tools for synthesizing large health data sets into insightful visualizations. Produced statistical models and distributions that advanced the understanding of health service pathway usage. Developed machine learning pipelines and trained deep learning models to predict patient outcomes based on previous encounters. MITAC Accelerate recipient, co-authored four scientific papers that utilized the developed products."""
              )
    st.divider()
    write_job(position="Computer Science Lab Instructor", 
              company="University of Victoria",
              time="January 2020 -- December 2021",
              location="Victoria, B.C.",
              description="""Taught lab sections for many different first and second year computer science classes. Helped students obtain a deeper understanding of the course material. Marked student assignments, midterms, and final exams, while providing helpful feedback. Managed the computer science assistance centre."""
              )
    st.divider()
    write_job(position="Science Instructor", 
              company="Science Venture",
              time="September 2019 -- December 2019",
              location="Victoria, B.C.",
              description="""Collaborated on curriculum development for science and technology clubs. Delivered engaging, high impact, interactive lessons to students on a weekly basis."""
              )
    st.divider()
    write_job(position="Physics Researcher", 
              company="ATLAS Canada",
              time="January 2018 -- September 2018",
              location="Victoria, B.C.",
              description="""Generated histograms from simulated data of proton-proton collisions to analyze and optimize for a specific particle physics model that predicted dark matter production. Presented power points that showed intermediate results regularly at weekly meetings."""
              )
    st.divider()
    write_job(position="Senior Tour Guide & Welcome Desk Receptionist", 
              company="University of Victoria",
              time="April 2016 -- April 2023",
              location="Victoria, B.C.",
              description="""Eﬀectively communicated key facts about the university to groups of parents and prospective students. Provided guests with helpful information, direction, and answered questions about the university."""
              )
    st.divider()
    

def education():
    st.divider()
    write_degree(institution="University of Victoria, Victoria, B.C.", 
                 degree="MSc. Computer Science", 
                 time="September 2020 -- December 2022", 
                 thesis="Scaling Up Structural Clustering to Large Probabilistic Graphs Using Lyapunov Central Limit Theorem", 
                 supervisor="Dr. Alex Thomo and Dr. Venkatesh Srinivasan"
                 )
    st.divider()
    write_degree(institution="University of Victoria, Victoria, B.C.", 
                 degree="BSc. Honours Physics, Computer Science Minor", 
                 time="September 2014 -- April 2020", 
                 thesis= "Dichroic Atomic Vapour Laser Lock for Cavity Quantum Optics", 
                 supervisor="Dr. Andrew MacRae"
                 )
    st.divider()


def publications():
    st.divider()
    write_paper(journal="VLDB 2023 Volume 16", 
                title="Scaling Up Structural Clustering to Large Probabilistic Graphs Using Lyapunov Central Limit Theorem", 
                authors="Joseph Howie, Dr. Venkatesh Srinivasan, Dr. Alex Thomo", 
                doi="10.14778/3611479.3611516",
                link="https://www.vldb.org/pvldb/vol16/p3165-howie.pdf"
                )
    st.divider()
    write_paper(journal="MIE 2024 IOS Press", 
                title="Synthetic Generation of Patient Service Utilization Data: A Scalability Study", 
                authors="Joseph Howie, Sowmya Balasubramanian, Jonas Bambi, Kenneth Moselle, Venkatesh Srinivasan, Alex Thomo", 
                doi="10.3233/SHTI240511",
                link="https://ebooks.iospress.nl/doi/10.3233/SHTI240511"
                )
    st.divider()
    write_paper(journal="MDPI 2024 BioMedInformatics Volume 4 Issue 2", 
                title="A Methodological Approach to Extracting Patterns of Service Utilization from a Cross-Continuum High Dimensional Healthcare Dataset to Support Care Delivery Optimization for Patients with Complex Problems", 
                authors="Jonas Bambi, Yudi Santoso, Hanieh Sadri, Ken Moselle, Abraham Rudnick, Stan Robertson, Ernie Chang, Alex Kuo, Joseph Howie, Gracia Yunruo Dong, Kehinde Olobatuyi, Mahdi Hajiabadi, and Ashlin Richardson", 
                doi="10.3390/biomedinformatics4020053",
                link="https://www.mdpi.com/2673-7426/4/2/53#"
                )
    st.divider()
    write_paper(journal="MDPI 2024 BioMedInformatics Volume 4 Issue 3", 
                title="Approaches to Extracting Patterns of Service Utilization for Patients with Complex Conditions: Graph Community Detection vs. Natural Language Processing Clustering", 
                authors="Jonas Bambi, Hanieh Sadri, Ken Moselle, Ernie Chang, Yudi Santoso, Joseph Howie, Abraham Rudnick, Lloyd T. Elliott, and Alex Kuo", 
                doi="10.3390/biomedinformatics4030103",
                link="https://www.mdpi.com/2673-7426/4/3/103"
                )
    st.divider()


def projects():
    st.write("These projects span three areas: Academic, Profressional, and Personal")
    academic, prof, personal = st.tabs(["Academic", "Profressional", "Personal"])
    with academic:
        with st.expander("Master's Thesis"):
            st.write("""The paper \"Scaling Up Structural Clustering to Large Probabilistic Graphs Using Lyapunov Central Limit Theorem\" 
                     mentioned in the publications page was the main project of my master's program. 
                     It took about one year to complete and was the result of taking a unique idea from conception
                     to a fully functional algorithm that was tested on multiple datasets. The publication of this work afforded me the 
                     opportunity to present the paper at the VLDB conference in 2023. The conference asked me to record the presentation 
                     for their digital archive and can be viewed on YouTube.""")
            redirect_button("https://youtu.be/GGrUU-MBJyk?si=dNkHVsTYrjXaFs8G", "Paper Presentation")
            st.write("\n")
        
        with st.expander("Honours Thesis"):
            st.write("""As part of my honours degree in physics, I had the opportunity to work on a 
                        quantum optics project. For this project, I designed a specialized laser locking system that stablized
                        a lasers frequency within 0.0001\% of the desired value. The specific system was called a 
                        Dichroic Atomic Vapour Laser Lock, or DAVLL. This project required precise alignmen of optical components 
                        (mirrors, lenses, and sensors), as well as careful circuit design and fine tuning.""")
        
    # with prof:
    #     with st.expander(""):

#button
def redirect_button(url: str, text: str= None, color="#FD504D"):
    st.markdown(
    f"""
    <a href="{url}" target="_self">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )

        
# writer functions
def print_list(list_of_skills):
    for i in sorted(list_of_skills):
        st.markdown("- "+i)


def write_job(position, company, time, location, description):
    with st.container(horizontal=True):
        st.subheader(f"**{position}**")
        st.subheader(f"**{company}**", text_alignment="right")
    with st.container(horizontal=True):
        st.caption(f"_{time}_")
        st.caption(f"_{location}_", text_alignment="right")
    st.write(description)


def write_degree(institution, degree, time, thesis='', supervisor=''):
    st.subheader(f"**{degree}**")
        
    with st.container(horizontal=True):
        st.caption(f"**{institution}**")
        st.caption(f"_{time}_", text_alignment="right")
        
    if thesis!="":
        st.write(f'**Thesis:** _"{thesis}"_')
    if supervisor!="":
        st.write(f"Supervisor: {supervisor}")


def write_paper(journal, title, authors, doi, link):
    st.subheader(f"**{title}**")
    with st.container(horizontal=True):
        st.caption(f"**{journal}**")
        st.caption(f"**Authors:** _{authors}_", text_alignment="right")
    st.page_link(link, label=f"DOI: {doi}", icon="📝")


if __name__=="__main__":
    main()
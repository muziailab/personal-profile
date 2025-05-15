import streamlit as st
from datetime import datetime

def create_timeline(date_str, title, description):
    start_date = datetime.strptime(date_str.split(' - ')[0], '%b %Y')
    current_date = datetime.now()
    is_current = 'Present' in date_str
    
    st.markdown(f"""
    <div style="position: relative; padding-left: 30px; margin-bottom: 20px; border-left: 2px solid #ccc;">
        <div style="position: absolute; left: -8px; top: 0; width: 16px; height: 16px; 
                    background-color: {'#1f77b4' if is_current else '#2ca02c'}; 
                    border-radius: 50%;"></div>
        <div style="margin-bottom: 5px; color: #666;">{date_str}</div>
        <div style="font-weight: bold; margin-bottom: 5px;">{title}</div>
        <div style="color: #444;">{description}</div>
    </div>
    """, unsafe_allow_html=True)

def create_skill_bar(skill, level):
    st.markdown(f"""
    <div style="margin-bottom: 10px;">
        <div style="margin-bottom: 5px;">{skill}</div>
        <div style="background-color: #f0f2f6; border-radius: 10px; height: 20px;">
            <div style="width: {level}%; height: 100%; background-color: #1f77b4; 
                        border-radius: 10px; transition: width 0.5s ease;">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def education_page():
    st.title("Education")
    
    st.markdown("### 📚 Educational Timeline")
    
    # CUHK
    create_timeline(
        "Sep 2024 - Present",
        "The Chinese University of Hong Kong",
        "Master of Science in Marketing\n" +
        "• Major Courses: Marketing Strategy, Consumer Behavior Analysis\n" +
        "• Specialized in data-driven marketing strategies"
    )
    
    # Ningbo University
    create_timeline(
        "Sep 2015 - Jun 2019",
        "Ningbo University",
        "Bachelor of Economics in International Trade\n" +
        "• GPA: 88.12/100, Major Ranking: Top 3.37%\n" +
        "• English-taught program with solid professional knowledge"
    )
    
    # Netherlands Exchange
    create_timeline(
        "Feb 2017 - Jun 2017",
        "University of Applied Sciences, Netherlands",
        "Exchange Program\n" +
        "• Cross-cultural Management & International Marketing\n" +
        "• Enhanced international perspective through team projects"
    )
    
    st.markdown("---")
    
    # Skills with Progress Bars
    st.markdown("### 🎯 Key Skills & Proficiency")
    
    col1, col2 = st.columns(2)
    
    with col1:
        create_skill_bar("Marketing Analytics", 90)
        create_skill_bar("Data Analysis", 85)
        create_skill_bar("Research Methods", 88)
    
    with col2:
        create_skill_bar("Digital Marketing", 92)
        create_skill_bar("Business English", 95)
        create_skill_bar("Cross-cultural Communication", 90)
    
    st.markdown("---")
    
    # Detailed Education Information
    st.markdown(
        """
        ### 🎓 The Chinese University of Hong Kong
        **Master of Science in Marketing** (Sep 2024 - Present)
        - Major Courses: Marketing Strategy, Consumer Behavior Analysis, Digital Marketing Analytics, Marketing Research Methods
        - Specialized in data-driven marketing strategies and consumer insights analysis
        - Engaged in research projects focusing on digital consumer behavior and market trends
        - Active participant in marketing case competitions and industry seminars

        ---

        ### 🎓 Ningbo University
        **Bachelor of Economics in International Trade** (Sep 2015 - Jun 2019)
        - Major Courses: International Trade Theory & Practice, Economic Principles, International Finance, Business English
        - GPA: 88.12/100, Major Ranking: Top 3.37%
        - English-taught program, developed solid professional knowledge and English proficiency
        - Active participation in campus activities and student organizations, served as Academic Representative
        """
    )

    st.markdown("---")

    # Netherlands Exchange Experience
    st.markdown(
        """
        ### 🌍 University of Applied Sciences, Netherlands
        **Exchange Program** (Feb 2017 - Jun 2017)
        - Major Courses: Strategic Business Decision Making, Cross-cultural Management, International Marketing
        - Participated in multiple cross-cultural team projects, enhancing international perspective and teamwork abilities
        - Completed field market research projects, developing practical skills and problem-solving capabilities
        """
    )

    st.markdown("---")

    # Key Course Projects
    st.markdown(
        """
        ### 📚 Key Academic Projects
        1. **Consumer Behavior Research Project at CUHK**
           - Conducted comprehensive analysis of digital consumer behavior patterns
           - Applied advanced statistical methods for data analysis
           - Presented findings at department research seminar

        2. **Marketing Analytics Case Study**
           - Developed data-driven marketing strategies for real business cases
           - Utilized Python and SPSS for customer segmentation analysis
           - Received excellent feedback from industry professionals

        3. **International Trade Practice Project**
           - Led a team in simulating international trade operations
           - Managed documentation and cross-border transaction processes
           - Achieved Best Team Performance recognition
        """
    )

    # Certificates
    st.markdown(
        """
        ### 🏆 Professional Certifications
        - **College English Test Band 6 (CET-6)**
          *National standardized test for English proficiency*
        - **National Computer Rank Examination Level 2**
          *Professional certification in computer application skills*
        - **Online Learning Achievements**
          *Continuous education in data analytics and digital marketing*
        """
    )
import streamlit as st
from PIL import Image
import os
from components.project_card import create_project_card

def home_page():
    # 创建两列布局
    left_col, right_col = st.columns(2)
    
    # Personal information on the left
    left_col.markdown(
        """
        <h2>Jiaqi Wu</h2>
        <p style='font-size: 1.2em;'>
        Influencer｜Digital Nomad｜INTJ<br>
        Phone: +86 18888642329<br>
        Email: <a href="mailto:jessicawoo1122@gmail.com">jessicawoo1122@gmail.com</a>
        </p>
        """,
        unsafe_allow_html=True
    )

    # Profile photo on the right
    image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "images", "IMG_9341.JPG")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile photo not found")

    st.markdown("---")

    # Personal Profile
    st.markdown(
        """
        ### About Me
        I am a passionate Marketing graduate student at The Chinese University of Hong Kong with a solid background in International Trade and Economics. 
        Currently focusing on data-driven marketing strategies and consumer behavior analysis, I combine academic knowledge with practical marketing skills. 
        I am proficient in various data analysis tools and marketing research methods, capable of conducting in-depth market analysis and deriving 
        meaningful insights from data.

        With strong analytical and communication skills developed through international education experiences, I excel at adapting to new environments 
        and working in cross-cultural settings. I maintain a keen interest in digital marketing trends and consumer behavior patterns, actively engaging 
        in research projects and case competitions to enhance my professional capabilities.
        """
    )

    st.markdown("---")

    # Core Skills with Progress Bars
    st.markdown("### 🎯 Core Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Technical Skills")
        for skill, level in [
            ("Marketing Analytics", 90),
            ("Data Analysis", 85),
            ("Research Methods", 88),
            ("Digital Marketing", 92)
        ]:
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
    
    with col2:
        st.markdown("#### Language & Soft Skills")
        for skill, level in [
            ("English", 95),
            ("Chinese", 100),
            ("Communication", 90),
            ("Leadership", 85)
        ]:
            st.markdown(f"""
            <div style="margin-bottom: 10px;">
                <div style="margin-bottom: 5px;">{skill}</div>
                <div style="background-color: #f0f2f6; border-radius: 10px; height: 20px;">
                    <div style="width: {level}%; height: 100%; background-color: #2ca02c; 
                                border-radius: 10px; transition: width 0.5s ease;">
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Featured Projects
    st.markdown("### 🚀 Featured Projects")

    # Project 1
    create_project_card(
        "Consumer Behavior Analysis Platform",
        "Developed a comprehensive platform for analyzing digital consumer behavior patterns using advanced analytics tools.",
        ["Python", "Data Analysis", "Machine Learning", "Marketing Analytics"],
        "Achieved 92% accuracy in consumer behavior prediction"
    )

    # Project 2
    create_project_card(
        "Social Media Marketing Campaign",
        "Led a successful digital marketing campaign across multiple social media platforms.",
        ["Digital Marketing", "Content Strategy", "Analytics", "Social Media"],
        "Increased engagement by 150% and reached over 1M users"
    )

    st.markdown("---")

    # Academic Achievements
    st.markdown("""
    ### 🏆 Academic Achievements
    - Dean's List at The Chinese University of Hong Kong (2023)
    - Outstanding Performance in Marketing Case Competition (2023)
    - Third-class Scholarship of Ningbo University (2016)
    """)
import streamlit as st
from components.project_card import create_project_card

def create_experience_timeline(date, company, role, description):
    st.markdown(f"""
    <div style="position: relative; padding-left: 30px; margin-bottom: 20px; border-left: 2px solid #ccc;">
        <div style="position: absolute; left: -8px; top: 0; width: 16px; height: 16px; 
                    background-color: #1f77b4; border-radius: 50%;"></div>
        <div style="margin-bottom: 5px; color: #666;">{date}</div>
        <div style="font-weight: bold; margin-bottom: 5px;">{role} | {company}</div>
        <div style="color: #444;">{description}</div>
    </div>
    """, unsafe_allow_html=True)

def experience_page():
    st.title("Work Experience")

    # Work Experience Timeline
    st.markdown("### 💼 Professional Experience")

    # Kujiale Experience
    create_experience_timeline(
        "Jul. 2021 - Mar. 2022",
        "Hangzhou Manycore Information Co., Ltd. (Kujiale)",
        "Senior Product Operations Specialist",
        """• Content Marketing:
          - Built and managed Kujiale video account
          - Implemented comprehensive digital marketing strategy through short videos, live broadcasts, and articles
          - Achieved over 300,000 accumulated exposure
          - Generated transaction amount of 300,000 yuan in one quarter

• Product Operations:
          - Led operations for 3 major products
          - Implemented SEO strategies and conducted online/offline training
          - Achieved annual product revenue of 2 million yuan (↑54% YoY)
          - Increased WAU to 70,000 (↑56% YoY)

• Solution Building:
          - Independently developed 2 product solutions
          - Conducted thorough market research, competitive analysis, and user behavior analysis
          - Generated revenue of 300,000 yuan"""
    )

    # Alibaba Group Experience
    create_experience_timeline(
        "Feb. 2019 - Jul. 2021",
        "Xiuhua Zhiyun Technology Co., Ltd., Alibaba Group",
        "Senior Operations Specialist",
        """• User Operations:
          - Implemented RFM model for user segmentation and behavior analysis
          - Provided data-driven feedback for product optimization
          - Supported technology team in product iteration

• Product Operations:
          - Managed short video automation production platform
          - Implemented platform analytics and monitoring systems
          - Achieved 135% monthly user growth rate post-launch

• Event Operations:
          - Led cooperative project with Jiangsu Province Ministry of Propaganda and Tencent Video
          - Achieved 50% user recall rate
          - Successfully attracted significant new user base
          - Managed New Year's greeting card campaign with Xiuhua News Agency
          - Launched "Sound Photo Studio" C-side app in 6 weeks
          - Achieved over 10,000 daily video synthesis volume
          - Acquired over 40,000 users in a single month"""
    )
    

    st.markdown("---")

    # Entrepreneurship Experience
    st.markdown("### 🚀 Entrepreneurship")

    # Self-Media Project
    create_project_card(
        "Influencer",
        "Operating a successful social media account focused on workplace knowledge and experience sharing.",
        ["Content Creation", "Video Production", "Social Media", "Marketing"],
        "200,000+ followers, 2M+ cumulative views, 200,000+ views on top videos"
    )

    # ME+ Accessories
    create_project_card(
        "ME+ Accessories - Retail Business",
        "Founded and managing a successful retail business through brand franchising.",
        ["Retail Management", "Team Leadership", "Marketing", "Operations"],
        "300,000 yuan average monthly turnover, managing team of 4 employees"
    )

    # Homie Tech
    create_project_card(
        "Hangzhou Homie Tech Co., Ltd.",
        "Co-founded a social media platform for international students in China.",
        ["Entrepreneurship", "Marketing Operations", "Event Management", "Social Media"],
        "30,000+ WeChat followers, 300+ articles published, successful international events"
    )
    

    st.markdown("---")

    # Professional Skills with Visual Representation
    st.markdown("### 🛠 Professional Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; height: 100%;">
            <h4 style="color: #1f77b4;">Marketing Planning</h4>
            <ul style="list-style-type: none; padding-left: 0;">
                <li>✓ Market Research and Analysis</li>
                <li>✓ Marketing Strategy Development</li>
                <li>✓ Campaign Planning and Execution</li>
                <li>✓ Brand Promotion</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; height: 100%;">
            <h4 style="color: #1f77b4;">Digital Marketing</h4>
            <ul style="list-style-type: none; padding-left: 0;">
                <li>✓ Social Media Operations</li>
                <li>✓ Content Marketing</li>
                <li>✓ SEO Optimization</li>
                <li>✓ Data Analytics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; height: 100%;">
            <h4 style="color: #1f77b4;">Tools Proficiency</h4>
            <ul style="list-style-type: none; padding-left: 0;">
                <li>✓ Data Analysis: Excel, Python</li>
                <li>✓ Design: PS, PR, AE</li>
                <li>✓ Office Suite</li>
                <li>✓ Marketing Tools</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
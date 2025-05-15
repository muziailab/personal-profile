import streamlit as st
import os
import sys

# 添加页面内容目录到系统路径
sys.path.append(os.path.dirname(__file__))

# 导入页面模块
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.contact import contact_page

# Set page configuration
st.set_page_config(
    page_title="Jiaqi Wu's Personal Website",
    page_icon="👩‍💼",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Navigation Menu")
page = st.sidebar.radio(
    "Select Page",
    ["Home", "Work Experience", "Education", "Contact"],
    index=0
)

# Page routing
if page == "Home":
    home_page()
elif page == "Work Experience":
    experience_page()
elif page == "Education":
    education_page()
else:
    contact_page()

# Add footer
st.sidebar.markdown("---")
st.sidebar.markdown(
    """<div style='text-align: center'>
    © 2024 Jiaqi Wu. All rights reserved.
    </div>""",
    unsafe_allow_html=True
)
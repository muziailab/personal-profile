import streamlit as st

def create_project_card(title, description, skills, achievements):
    st.markdown(f"""
    <div style="
        border: 1px solid #e1e4e8;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: box-shadow 0.2s ease-in-out;
        cursor: pointer;
    " onmouseover="this.style.boxShadow='0 4px 8px rgba(0,0,0,0.2)'" onmouseout="this.style.boxShadow='0 2px 4px rgba(0,0,0,0.1)'">
        <h3 style="color: #1f77b4; margin-bottom: 10px;">{title}</h3>
        <p style="color: #444; margin-bottom: 15px;">{description}</p>
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 15px;">
            {' '.join([f'<span style="background-color: #e1e4e8; padding: 4px 8px; border-radius: 15px; font-size: 0.9em;">{skill}</span>' for skill in skills])}
        </div>
        <div style="border-top: 1px solid #e1e4e8; padding-top: 15px;">
            <p style="color: #666; font-style: italic;">{achievements}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
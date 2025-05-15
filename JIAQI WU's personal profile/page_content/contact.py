import streamlit as st

def create_contact_card(icon, title, content):
    st.markdown(f"""
    <div style="
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        transition: transform 0.2s ease-in-out;
        &:hover {{
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
    ">
        <div style="font-size: 24px; margin-bottom: 10px;">{icon}</div>
        <div style="font-weight: bold; color: #1f77b4; margin-bottom: 5px;">{title}</div>
        <div style="color: #444;">{content}</div>
    </div>
    """, unsafe_allow_html=True)

def contact_page():
    st.title("Contact Me")

    # Contact Information Cards
    col1, col2 = st.columns(2)
    
    with col1:
        create_contact_card(
            "📱",
            "Phone",
            "+86 18888642329"
        )
    
    with col2:
        create_contact_card(
            "📧",
            "Email",
            "<a href='mailto:jessicawoo1122@gmail.com' style='color: #1f77b4; text-decoration: none;'>jessicawoo1122@gmail.com</a>"
        )

    st.markdown("---")

    # Enhanced Contact Form
    st.markdown("""
    <h3 style="color: #1f77b4;">✉️ Leave a Message</h3>
    <p style="color: #666; margin-bottom: 20px;">I'd love to hear from you! Please fill out the form below and I'll get back to you as soon as possible.</p>
    """, unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Your Name", placeholder="Enter your name")
        with col2:
            email = st.text_input("Your Email", placeholder="Enter your email")
        
        subject = st.text_input("Subject", placeholder="What is your message about?")
        message = st.text_area("Message", placeholder="Type your message here...", height=150)
        
        col1, col2, col3 = st.columns([1,1,2])
        with col2:
            submit_button = st.form_submit_button("Send Message", use_container_width=True)

        if submit_button:
            if name and email and subject and message:
                st.success("✅ Thank you for your message! I will get back to you soon.")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields.")

    # Social Media Links
    st.markdown("---")
    st.markdown("""
    <h3 style="color: #1f77b4;">🌐 Connect with Me</h3>
    <div style="display: flex; gap: 20px; margin-top: 20px;">
        <a href="https://linkedin.com" target="_blank" style="text-decoration: none;">
            <div style="background-color: #0077B5; color: white; padding: 10px 20px; border-radius: 5px; transition: opacity 0.2s;">
                LinkedIn
            </div>
        </a>
        <a href="https://twitter.com" target="_blank" style="text-decoration: none;">
            <div style="background-color: #1DA1F2; color: white; padding: 10px 20px; border-radius: 5px; transition: opacity 0.2s;">
                Twitter
            </div>
        </a>
        <a href="https://github.com" target="_blank" style="text-decoration: none;">
            <div style="background-color: #333; color: white; padding: 10px 20px; border-radius: 5px; transition: opacity 0.2s;">
                GitHub
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)
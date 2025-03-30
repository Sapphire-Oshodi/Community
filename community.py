import streamlit as st

# Image paths
COMMUNITY_SUPPORT_IMAGE_PATH = "image2.jpg"

# Community & Support groups
SUPPORT_GROUPS = """
### Local PCOS Support Groups You Can Join in Nigeria

- **Cysters Advocate**: [Join WhatsApp Group](https://chat.whatsapp.com/F9mezTC19kFFajwjGneSGb)  
- **That.PCOS.Chick**: [Follow on Instagram](https://www.instagram.com/that.pcos.chick?igsh=MXNqdWQ5cW9ybXI2cQ==)  
- **PCOS Conquerors**: [Follow on Instagram](https://www.instagram.com/pcosconquerors?igsh=cnphY3l0eWdicDBp)  
- **The Fit Priest** (aka Selema ‘That’ PCOS Babe): [Follow on Instagram](https://www.instagram.com/thefitpriest?igsh=bHY0YjFodGd5dXoz)  
- **PCOS Awareness Association**: [Visit Official Website](https://www.pcosaa.org/)
"""

# Define the Streamlit app
def main():
    st.set_page_config(
        page_title="CycleCare AI - Community & Support",
        layout="wide",
    )

    # Page header
    st.title("Lifestyle Recommendations Management")
    st.caption("Empowering Women with Knowledge and Support")

    # Community & Support Section
    st.header("Community & Support")

    # Center and resize the image using st.image()
    st.image(
        COMMUNITY_SUPPORT_IMAGE_PATH,
        caption="Connecting the PCOS Community",
        width=800,
        use_column_width="auto"
    )

    st.markdown("#### Explore and Connect")
    with st.expander("**PCOS Support Groups**"):
        st.markdown(SUPPORT_GROUPS, unsafe_allow_html=True)

    # Footer
    st.write("---")
    st.caption("Your community is here to support you. Together, we thrive!")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
from PIL import Image

# --------- Page Config ---------
st.set_page_config(page_title="InstaQlean", layout="centered")

# --------- Custom Styling ---------
st.markdown("""
    <style>
    .main-title {
        font-size: 48px;
        font-weight: 800;
        color: white;
        margin-bottom: 0px;
    }
    .highlight-q {
        color: #00C9A7;
    }
    .subtext {
        font-size: 18px;
        color: #CCCCCC;
        margin-top: 0px;
        margin-bottom: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# --------- Header ---------
st.markdown("""
    <div class='main-title'>
        Insta<span class='highlight-q'>Q</span>lean 🔍
    </div>
    <div class='subtext'>
        The no-login-needed tool that reveals who really engages with you on Instagram by analyzing your downloaded data.
    </div>
""", unsafe_allow_html=True)

# --------- File Upload ---------
uploaded_file = st.file_uploader("Upload your Instagram data (.json or .zip)", type=["json", "zip"])

if uploaded_file:
    st.success("File uploaded successfully! 📂")
else:
    st.info("Waiting for file upload...")

st.divider()

# --------- Connections Breakdown (Fake Data) ---------
st.subheader("👥 Connections Breakdown")

mutuals = pd.DataFrame({
    "Username": ["@jane_doe", "@coolguy42", "@bestie123"]
})

fans = pd.DataFrame({
    "Username": ["@followeronly", "@fanaccount"]
})

ghosts = pd.DataFrame({
    "Username": ["@ghostuser1", "@ghostuser2", "@ghostuser3"]
})

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### ✅ Mutuals")
    st.dataframe(mutuals, use_container_width=True)

with col2:
    st.markdown("### 🧍‍♀️ Fans")
    st.dataframe(fans, use_container_width=True)

with col3:
    st.markdown("### ❌ Ghosts")
    st.dataframe(ghosts, use_container_width=True)

st.divider()

# --------- Engagement Word Cloud ---------
st.subheader("💬 Engagement Word Cloud")

# Show static word cloud image
try:
    image = Image.open("sample_wordcloud.png")
    st.image(image, caption="Top Engagers", use_column_width=True)
except:
    st.warning("⚠️ Word cloud image not found. Add 'sample_wordcloud.png' to the project folder.")

st.divider()

# --------- Fake Follower Detector ---------
st.subheader("🧟 Fake Follower Detector")

fake_followers = pd.DataFrame({
    "Username": ["@ghostuser1", "@fakiee12345", "@bot_789"],
    "Flagged Reason": [
        "No profile picture",
        "Suspicious username (random numbers)",
        "Zero followers / Zero following"
    ]
})

st.dataframe(fake_followers, use_container_width=True)

# --------- Footer ---------
st.markdown("---")
st.caption("📅 Built for Senior Capstone | Demo v1")

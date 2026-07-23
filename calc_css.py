import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Stylish Calculator",
    page_icon="🧮",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#334155);
}

.main-title{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:white;
    background: linear-gradient(90deg,#00F5A0,#00D9F5);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:10px;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:30px;
}

div[data-testid="stVerticalBlock"]{
    border-radius:20px;
}

.stButton>button{
    width:100%;
    height:55px;
    background:linear-gradient(90deg,#00F5A0,#00D9F5);
    color:black;
    border:none;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#00D9F5,#00F5A0);
    transform:scale(1.02);
}

.result{
    padding:20px;
    border-radius:15px;
    background:#1e293b;
    color:#00F5A0;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    border:2px solid #00F5A0;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<h1 class='main-title'>🧮 Trendy Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Simple • Fast • Beautiful</p>", unsafe_allow_html=True)

# ---------- Inputs ----------
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("🔢 First Number", value=0.0)

with col2:
    num2 = st.number_input("🔢 Second Number", value=0.0)

operation = st.selectbox(
    "✨ Select Operation",
    ["➕ Add", "➖ Subtract", "✖ Multiply", "➗ Divide"]
)

# ---------- Calculate ----------
if st.button("🚀 Calculate"):

    if operation == "➕ Add":
        ans = num1 + num2

    elif operation == "➖ Subtract":
        ans = num1 - num2

    elif operation == "✖ Multiply":
        ans = num1 * num2

    elif operation == "➗ Divide":
        if num2 == 0:
            st.error("❌ Cannot divide by zero.")
            st.stop()
        ans = num1 / num2

    st.markdown(
        f"<div class='result'>🎯 Result: {ans}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")

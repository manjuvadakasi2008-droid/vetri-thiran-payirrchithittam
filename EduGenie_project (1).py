import streamlit as st
from google import genai

# EduGenie - Learning Assistant

st.set_page_config(
    page_title="EduGenie",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 EduGenie")
st.subheader("Google Gemini Powered Learning Assistant")

st.write(
    "Ask any academic question and EduGenie will explain it "
    "in a simple and student-friendly way."
)

api_key = st.text_input(
    "🔑 Enter your Gemini API Key",
    type="password"
)

subject = st.selectbox(
    "📚 Select Subject",
    [
        "General",
        "Mathematics",
        "Physics",
        "Chemistry",
        "Computer Science",
        "English"
    ]
)

question = st.text_area(
    "✏️ Enter your question",
    placeholder="Example: Explain Newton's second law in simple words..."
)

if st.button("🚀 Ask EduGenie"):

    if api_key.strip() == "":
        st.warning("Please enter your Gemini API key.")

    elif question.strip() == "":
        st.warning("Please enter a question.")

    else:
        try:
            client = genai.Client(api_key=api_key)

            prompt = f"""
You are EduGenie, a friendly learning assistant.

Subject: {subject}

Student Question:
{question}

Instructions:

1. Explain the answer clearly.
2. Use simple student-friendly language.
3. Give step-by-step explanation when necessary.
4. Use examples if useful.
5. Do not make the answer unnecessarily complicated.
6. If it is a calculation, show the steps.
7. If the question is unclear, explain what information is needed.
"""

            with st.spinner("EduGenie is thinking..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

            st.success("Answer generated successfully!")
            st.markdown("### 📖 EduGenie's Answer")
            st.write(response.text)

        except Exception as e:
            st.error("Something went wrong.")
            st.error(str(e))

st.divider()

st.caption("🎓 EduGenie | Learn • Understand • Grow")

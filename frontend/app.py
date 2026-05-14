import streamlit as st
import requests

st.title("Advanced Agentic Actor-Critic GraphRAG")

query = st.text_input("Ask a question")

if st.button("Run System"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"question": query},
    )

    st.write("Status Code:", response.status_code)

    try:
        data = response.json()

        st.subheader("Planner Output")
        st.write(data.get("plan"))

        st.subheader("Answer")
        st.write(data.get("answer"))

        st.subheader("Critic Review")
        st.write(data.get("review"))

    except Exception:
        st.error("Backend returned invalid response")
        st.text(response.text)

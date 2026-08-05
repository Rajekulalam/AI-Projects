import streamlit as st
import ollama

st.set_page_config(
    page_title="Local AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Local AI Assistant")
st.caption("Powered by Ollama")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    model = st.selectbox(
        "Choose Model",
        [
            "gemma3:4b",
            "qwen3:4b",
            "llama3.2:3b"
        ]
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.spinner("🤖 Thinking..."):

            response = ollama.chat(
                model=model,
                messages=st.session_state.messages,
                stream=False
            )

            answer = response["message"]["content"]

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            with st.chat_message("assistant"):
                st.markdown(answer)

    except Exception as e:
        st.error(f"❌ Error: {e}")
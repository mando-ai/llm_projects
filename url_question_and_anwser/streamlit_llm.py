import streamlit as st
from llm_q_and_a import main as q_a_main

if __name__ == "__main__":
    st.runtime.legacy_caching.clear_cache()
    st.set_page_config(layout="wide")
    st.title("Question and Answers ✍️")
    st.sidebar.header(
        "It's time to master Question and Anwsers using openAI GPT 3.5 turbo LLM model + Langchain Query retrievals"
    )
    st.sidebar.subheader("Enter below details👇🏻: ")
    url = st.sidebar.text_input("Blog URL to do question and answer")
    api_key = st.sidebar.text_input("Enter OpenAI API KEY")
    query = st.sidebar.text_input("Enter Question to Answer based on Blog URL")
    st.sidebar.write("----")
    st.sidebar.subheader("About this app:")
    st.sidebar.write(
        "Designed by **Shubham Mandowara** to showcase Questions and Answers using ChatGPT 3.5 and Langchain \n"
        "I hope this is helpful. Please feel free to contact me if you have any queries."
    )
    st.sidebar.write("----")
    st.sidebar.subheader(
        "🚀 Follow me for the latest insights on AI, ML, DL, Generative AI, Deployment, and MLOps! Stay ahead of the curve. 📊🤖 #AI #MachineLearning #DeepLearning #Tech"
    )

    with st.sidebar:
        column1, column2 = st.columns(2)
        column1.markdown(
            "[![Linkedin](https://img.icons8.com/material-outlined/48/000000/linkedin.png)](https://www.linkedin.com/in/shubhammandowara/)"
        )
        column2.markdown(
            "[![Github](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/ShubhamMandowara)"
        )

    st.info(
        """**Hit Enter** to get summary after URL and OpenAI API Key""",
        icon="ℹ️",
    )
    VIDEO_DATA = 'https://youtu.be/8ae8JAfW4rY?si=BhCGmqiMAin7pwe5'
    width = 20
    width = max(width, 0.01)
    side = max((100 - width) / 2, 0.01)

    other, container = st.columns([side, width])
    container.video(data=VIDEO_DATA)
    other.write(f"**Given blog link**:- {url}")
    other.write(f"**Question** : {query}")
    if url != "" and api_key != "" and query!="":
        with st.spinner("Wait for it..."):
            output = None
            while output == None:
                output = q_a_main(url=url, openai_api_key=api_key, query=query)
        other.write(output)
    else:
        other.write("Enter details...")

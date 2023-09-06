import streamlit as st
from llm_langchain_summary import main as llm_main

if __name__ == "__main__":
    st.runtime.legacy_caching.clear_cache()
    st.set_page_config(layout="wide")
    st.title("Text Summarization ✍️")
    st.sidebar.subheader(
        "It's time to master Summarization using openAI GPT 3.5 turbo model + Langchain"
    )
    st.sidebar.subheader("Enter below details👇🏻: ")
    url = st.sidebar.text_input("Blog URL to create summary")
    api_key = st.sidebar.text_input("Enter OpenAI API KEY")
    st.sidebar.write("----")
    st.sidebar.subheader("About this app:")
    st.sidebar.write(
        "Designed by **Shubham Mandowara** to showcase text summarization using various techniques. You can select the model, and add text to summarize."
    )
    st.sidebar.write(
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
        """**Press Enter** to get summary after URL and OpenAI API Key""",
        icon="ℹ️",
    )
    st.write(f"Given blog link:- {url}")
    summary = st.write("**Summary:**")
    if url != "" and api_key != "":
        with st.spinner("Wait for it..."):
            output = None
            while output == None:
                output = llm_main(url=url, open_api_key=api_key)
        st.write(output)
    else:
        st.write("Enter details...")

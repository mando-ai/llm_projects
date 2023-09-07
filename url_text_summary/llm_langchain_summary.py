from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain
from typing import List


def load_data_from_website(url: str) -> List:
    """Load data from url and return a list of Document

    Arguments:
        url (str): URL to load
    Returns:
        List: List of Document
    """
    loader = WebBaseLoader(url)
    docs = loader.load()
    return docs


def main(
    url: str,
    open_api_key: str,
    temperature: int = 0,
    model_name: str = "gpt-3.5-turbo-16k",
):
    """Main function to load data from website, create openai object and use langchain load summarize chain to get summary of the data"""
    docs = load_data_from_website(url=url)
    llm = ChatOpenAI(
        temperature=temperature, model_name=model_name, openai_api_key=open_api_key
    )
    chain = load_summarize_chain(llm, chain_type="stuff")
    summary = chain.run(docs)
    return summary

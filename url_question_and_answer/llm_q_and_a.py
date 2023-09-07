
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
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



def main(url:str, query:str, openai_api_key:str, model_name:str='gpt-3.5-turbo', temperature=0):
    """Main function to load data from website, create openai embedding object, split data  and use langchain 
        Things to consider
        1. Loading data
        2. Splitting data into documents of a specific size
        3. Storage of vector data to local or a vector data provider
        4. Retrieval: App retrieve splits from storage
        5. Generation: An LLM produces questions and answers
        6. Conversation: Multi turn conversition by adding memory to QA
        Arguments:
            url (str): URL link
            query (str): Query
    """
    docs = load_data_from_website(url=url)
    # here on text splitter chunk size is size of chunk and 
    # overlap is good to have to get small context of data same in next chunk
    # example 1-10 words are in 1st chunk and on next chunk 9-19 words chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    documents = text_splitter.split_documents(docs)
    db = FAISS.from_documents(documents=documents, embedding=OpenAIEmbeddings(openai_api_key=openai_api_key))
    llm = ChatOpenAI(model_name=model_name, temperature=temperature, openai_api_key=openai_api_key)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=db.as_retriever())
    result = qa_chain({"query": query})
    return result['result']
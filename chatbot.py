import os
import pandas as pd
import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain_mistralai.chat_models import ChatMistralAI
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from tqdm import tqdm
load_dotenv()
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.warn = lambda *args,**kwargs: None
# Set API key for Mistral AI (Replace with your actual key)
key = os.environ["MISTRAL_API_KEY"]

# Load and preprocess CSV
def load_and_process_csv(csv_path):
    loader = CSVLoader(csv_path)
    docs = loader.load()
    
    # Split large text into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)
    
    return split_docs

# Persist ChromaDB with HuggingFace embeddings
def create_or_load_vector_db(docs, persist_directory="chroma_db", batch_size=5000):
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Check if the database exists and has embeddings
    if os.path.exists(persist_directory):
        db = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)
        if len(db.get()["documents"]) > 0:
            print("✅ Embeddings found. Loading existing database...")
            return db  # Load and return existing DB

    # If embeddings don't exist, proceed with insertion
    print("⚠️ No embeddings found. Generating embeddings now...")
    
    if not os.path.exists(persist_directory):
        os.makedirs(persist_directory)
    
    db = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)
    
    print(f"Inserting {len(docs)} documents in batches of {batch_size}...\n")
    for i in tqdm(range(0, len(docs), batch_size), desc="Embedding Progress", unit="batch"):
        batch = docs[i : i + batch_size]
        db.add_documents(batch)
    
    db.persist()  # Ensure persistence
    print("✅ Embeddings successfully stored and loaded!")
    
    return db

# Initialize chat model
def create_qa_chain(vector_db):
    llm = ChatMistralAI(model="mistral-large-2407", temperature=0.2,api_key=key)
    retriever = vector_db.as_retriever(search_kwargs={"k": 10})

    # Maintain chat history
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=retriever, memory=memory
    )
    
    return qa_chain

# Run chatbot
def chat(qa_chain):
    print("\nChatbot Ready! Type 'exit' to stop.\n")
    
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("Goodbye!")
            break
        
        response = qa_chain.invoke({"question": query})
        print(f"Bot: {response['answer']}")

def check_chroma_db(vector_db):
    data_info = vector_db.get()
    print(f"\n✅ Total documents in ChromaDB: {len(data_info['documents'])}")

# Main Execution
if __name__ == "__main__":
    csv_path = "dataset/cleaned/dataset_cleaned.csv"  # Replace with actual CSV file
    docs = load_and_process_csv(csv_path)
    
    vector_db = create_or_load_vector_db(docs)
    check_chroma_db(vector_db)  # Add this to confirm data insertion
    qa_chain = create_qa_chain(vector_db)
    
    chat(qa_chain)

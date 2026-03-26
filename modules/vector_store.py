# from langchain_community.vectorstores import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings

# # 🔥 Load embedding ONLY ONCE
# embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# # 🔥 Load ChromaDB ONLY ONCE
# db = Chroma(
#     persist_directory="vector_db",
#     embedding_function=embedding
# )

# print("✅ Embedding + DB loaded once")


# # 🔍 Retrieve data (used in RAG)
# def retrieve_data(query):
#     docs = db.similarity_search(query, k=2)

#     # Debug print
#     print("🔍 Retrieved Context:\n", docs)

#     return "\n".join([doc.page_content for doc in docs])


# # 📥 Add data to DB (run only once via ingest.py)
# def add_data():

#     # ✅ Prevent duplicate insertion
#     if db._collection.count() > 0:
#         print("⚠️ Data already exists in DB")
#         return

#     texts = [
#         "Photosynthesis converts sunlight into energy in plants.",
#         "Water cycle includes evaporation condensation precipitation.",
#         "Gravity attracts objects toward Earth."
#     ]

#     db.add_texts(texts)
#     db.persist()

#     print("✅ Documents added successfully!")


from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# ✅ ADD THESE IMPORTS (FIX)
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 🔥 Load embedding ONLY ONCE
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 🔥 Load ChromaDB ONLY ONCE
db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding
)

print("✅ Embedding + DB loaded once")


# 🔍 Retrieve data (used in RAG)
def retrieve_data(query):
    docs = db.similarity_search(query, k=2)

    # Debug print
    print("🔍 Retrieved Context:\n", docs)

    return "\n".join([doc.page_content for doc in docs])


# 📥 Add data to DB (run only once via ingest.py)
def add_data():

    # ✅ Prevent duplicate insertion
    if db._collection.count() > 0:
        print("⚠️ Data already exists in DB")
        return

    texts = [
        "Photosynthesis converts sunlight into energy in plants.",
        "Water cycle includes evaporation condensation precipitation.",
        "Gravity attracts objects toward Earth."
    ]

    db.add_texts(texts)

    print("✅ Documents added successfully!")


# 🔥 PDF INGESTION FUNCTION (NEW FEATURE)
def add_pdf(pdf_path):

    print(f"📄 Processing PDF: {pdf_path}")

    reader = PdfReader(pdf_path)
    full_text = ""

    # 🔹 Extract text from PDF
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text

    # 🔹 Split into chunks (IMPORTANT)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50
    )

    chunks = splitter.split_text(full_text)

    print(f"📊 Total chunks created: {len(chunks)}")

    # 🔹 Store in DB
    db.add_texts(chunks)

    print("✅ PDF added to DB successfully!")


# 🧪 Debug function (ONLY ONCE)
def check_db():
    count = db._collection.count()
    print(f"📊 Total documents in DB: {count}")
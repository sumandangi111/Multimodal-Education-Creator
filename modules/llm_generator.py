from groq import Groq
from config import GROQ_API_KEY
from modules.vector_store import retrieve_data

client = Groq(api_key=GROQ_API_KEY)

def generate_explanation(topic):

    # 🔥 Step 1: Retrieve context
    context = retrieve_data(topic)

    # ✅ ADD DEBUG LINE RIGHT HERE 👇
    print("🔍 Retrieved Context:\n", context)

    # 🔥 Step 2: Prompt
    prompt = f"""
    You are a helpful teacher.

    Context:
    {context}

    Question:
    {topic}

    Explain in simple language and give 3 flashcards.
    """

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant"
    )

    text = response.choices[0].message.content
    text = text.replace("*", "")

    return text
import dotenv
import langchain_groq
import os

dotenv.load_dotenv()

llm = langchain_groq.ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="openai/gpt-oss-120b"
)

if __name__ == "__main__":
    response = llm.invoke("")
    print(response.content)
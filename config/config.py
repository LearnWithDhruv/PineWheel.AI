import os
from dotenv import load_dotenv

load_dotenv()  

class Config:
    DATABASE_URI = os.getenv("DATABASE_URI", "mongodb+srv://dhruvkhatter2003:<db_password>@cluster0.vaz62.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    # VECTOR_DB_URI = os.getenv("VECTOR_DB_URI", "localhost:5000")
    LLM_API_KEY = os.getenv("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")
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")  

config = Config()

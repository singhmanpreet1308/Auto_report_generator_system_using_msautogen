"""
Configuration file for the report generation system
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()

# EURI API_KEY
EURI_API_KEY  = os.getenv("EURI_API_KEY", "").strip()
EURI_BASE_URL = os.getenv("EURI_BASE_URL", "").strip()


# ChromaDB Configuration
CHROMA_DB_PATH = "./chroma_db"
COLLECTION_NAME = "sales_marketing_data"

# AutoGen Configuration
AUTOGEN_CONFIG = {
    "config_list": [
        {
            "model": "gpt-4o-mini",
            "api_key": EURI_API_KEY ,
            "base_url": EURI_BASE_URL,

         
        }
    ],
    "temperature": 0.7,
}

# Email Configuration
GMAIL_USER = os.getenv("GMAIL_USER", "")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "")

# Scheduler Configuration
SCHEDULE_TIME = "09:00"  # 9 AM BST
TIMEZONE = "Europe/London"

# Telegram Configuration
TELEGRAM_API_ID = int(os.getenv("TELEGRAM_API_ID", "20369351"))
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH", "e93ba614d87f2a1ef5ba4caa8b5fc908")
TELEGRAM_PHONE = os.getenv("TELEGRAM_PHONE", "+919540797834")


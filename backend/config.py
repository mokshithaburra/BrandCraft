from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

STABILITY_API_KEY = os.getenv("STABILITY_API_KEY", "")
STABILITY_ENGINE = os.getenv("STABILITY_ENGINE", "stable-diffusion-xl-1024-v1-0")

ALLOWED_ORIGINS = [origin.strip() for origin in os.getenv("ALLOWED_ORIGINS", "").split(",") if origin.strip()]

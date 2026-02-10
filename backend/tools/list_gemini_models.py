import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY", "")
if not api_key:
    raise SystemExit("GEMINI_API_KEY is not set")

genai.configure(api_key=api_key)

for model in genai.list_models():
    methods = ", ".join(model.supported_generation_methods or [])
    print(f"{model.name} | {methods}")
